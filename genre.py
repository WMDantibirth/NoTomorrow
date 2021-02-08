import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json

influence_data = pd.read_csv("influence_data.csv")
# data_by_artist = pd.read_csv("data_by_artist.csv")
# print(influence_data)
# graph_data = pd.DataFrame(influence_data, columns=['influencer_name', 'follower_name'])
# print(graph_data)
# name = data_by_artist['artist_name'].drop_duplicates().values.tolist()
# print(name)

# DG = nx.DiGraph()
# DG.add_nodes_from(name)
# for i in range(graph_data.shape[0]):
#     tmp = graph_data.loc[i].values.tolist()
#     DG.add_edge(tmp[0], tmp[1])

# nx.draw(DG, with_labels=True)
# plt.show()

# a, b = nx.hits(DG)
# b1 = json.dumps(b)
# # print(b1)
# f2 = open('authorities_json.json', 'w')
# f2.write(b1)
# f2.close()
genre1 = pd.DataFrame(influence_data, columns=['influencer_id', 'influencer_main_genre'])
genre2 = pd.DataFrame(influence_data, columns=['follower_id', 'follower_main_genre'])
genre2.columns = ['influencer_id', 'influencer_main_genre']
genre = pd.concat([genre1, genre2],axis=0)
dic = {}
genre = genre.drop_duplicates().values.tolist()
# print(genre)
for i in genre:
    if not i[0] in dic: dic[i[0]] = i[1]
    elif dic[i[0]] != i[1]:
        print(i[0], dic[i[0]], i[1])
        dic[i[0]] = i[1]

print(len(genre))
b1 = json.dumps(dic)
print(b1)
f2 = open('genre.json', 'w')
f2.write(b1)
f2.close()
