import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json
import scipy.stats
import numpy as np

def pearson(p,q):
    n = len(p)
    #分别求p，q的和
    sumx = sum([p[i] for i in range(n)])
    sumy = sum([q[i] for i in range(n)])
    #分别求出p，q的平方和
    sumxsq = sum([p[i]**2 for i in range(n)])
    sumysq = sum([q[i]**2 for i in range(n)])
    #求出p，q的乘积和
    sumxy = sum([p[i]*q[i] for i in range(n)])
    # print sumxy
    #求出pearson相关系数
    up = sumxy - sumx*sumy/n
    down = ((sumxsq - pow(sumxsq,2)/n)*(sumysq - pow(sumysq,2)/n))**.5
    #若down为零则不能计算，return 0
    if down == 0 :return 0
    r = up/down
    return r

data_by_artist = pd.read_csv("data_by_artist.csv")
attribute = pd.DataFrame(data_by_artist, columns=['artist_id', 'danceability', 'energy', 'valence', \
    'tempo','loudness', 'acousticness', 'instrumentalness', 'liveness', 'speechiness', 'duration_ms', 'popularity'])
attribute_norm = (attribute - attribute.min()) / (attribute.max() - attribute.min())
attribute = attribute_norm.values.tolist()
# print(name)

p=np.array(attribute[0])
q=np.array(attribute[1])

print(pearson(p,q))