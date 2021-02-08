import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json

influence_data = pd.read_csv("influence_data.csv")
data_by_artist = pd.read_csv("data_by_artist.csv")
# print(influence_data)
graph_data = pd.DataFrame(influence_data, columns=['influencer_id', 'follower_id'])
# print(graph_data)
name = data_by_artist['artist_id'].drop_duplicates().values.tolist()
# print(name)

DG = nx.DiGraph()
DG.add_nodes_from(name)
for i in range(graph_data.shape[0]):
    tmp = graph_data.loc[i].values.tolist()
    DG.add_edge(tmp[0], tmp[1])
# nx.draw(DG, with_labels=True)
# plt.show()

b = nx.pagerank(DG)
# b1 = json.dumps(b)
# print(b1)
# f2 = open('pagerank.json', 'w')
# f2.write(b1)
# f2.close()
pd.DataFrame.from_dict(b, orient='index',columns=['fruits']).to_csv('11.csv')
