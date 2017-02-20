from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


petri_id = 695218
dor_id = 132880

def get_colabs(u_id):
	index = 1
	colabs = {}
	output = {}

	while output != None:

		colabs = {**colabs, **output}

		if index == 1:
			page_number = 1
		else:
			page_number = 20*(index-1) + 1

		output = scrape_colab(u_id, page_number)
		index += 1


	return colabs


def scrape_colab(u_id, page_id):
	url = "http://www.ams.org/mathscinet/search/authors.html?coauth={0}&r={1}".format(u_id, page_id)

	try:
		page = urlopen(url)
	except:
		return None

	soup = BeautifulSoup(page, "lxml")
	forms = soup.find_all('form')
	co_author_form = forms[1]

	co_authors = co_author_form.find_all("a")

	authors = {}

	for item in co_authors:
		text = item.get_text()
		try:
			number = int(text)
		except:
			link = item['href']
			link_id = int(link.split("=")[1])
			authors[text] = link_id

	return authors


def make_net(u_id, u_name):

	colab_dict = get_colabs(u_id)
	names = list(colab_dict.keys())
	ids = list(colab_dict.values())

	names.append(u_name)
	ids.append(u_id)

	adj_mat = pd.DataFrame(0, index = names, columns = names)

	net = nx.Graph()
	net.add_nodes_from(names)

	for i in range(len(names)):

		print("Scraping {}".format(names[i]))
		i_colabs = get_colabs(ids[i])
		for j in range(i):

			if ids[j] in i_colabs.values():

				adj_mat[names[i]][names[j]] = 1
				adj_mat[names[j]][names[i]] = 1

				net.add_edges_from([(names[i], names[j])])


	clustering_coeffs = nx.clustering(net)
	print("Clustering Coefficient for {0}, {1}".format(u_name,clustering_coeffs[u_name]))
	pos=nx.spring_layout(net)

	pos_higher = {}
	y_off = .1  # offset on the y axis

	for k, v in pos.items():
		pos_higher[k] = (v[0], v[1] + y_off)


	fig, ax = plt.subplots()

	nx.draw(net, pos, ax = ax)
	nx.draw_networkx_labels(net, pos_higher, ax = ax)

	plt.show()
	return adj_mat


