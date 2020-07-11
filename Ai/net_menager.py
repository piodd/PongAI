from Ai.net import Net
from random import random


def childNet(net: Net, ratioOfChange) -> Net:
    edge = [[[0 for x in range(7)] for y in range(7)] for h in range(3)]
    for w in range(len(net.edge)):
        for x in range(len(net.edge[w])):
            for y in range(len(net.edge[w][x])):
                edge[w][x][y] = net.edge[w][x][y] + (random() - 1 / 2) * ratioOfChange
    newNet = Net()
    newNet.setEdge(edge)
    return newNet
