from random import random
from typing import List


class Net:

    def __init__(self):
        self.size = 5
        self.node = [[0 for x in range(4)] for y in range(7)]
        self.edge = [[[0 for x in range(7)] for y in range(7)] for h in range(3)]
        self.decision = [self.node[0][3], self.node[1][3]]  # we need only 2
        self.calculateDecision(self.sampleEnterValue())
        self.randomEdge()

    def randomEdge(self):
        for w in range(len(self.edge)):
            for x in range(len(self.edge[w])):
                for y in range(len(self.edge[w][x])):
                    self.edge[w][x][y] = random() - 1 / 2

    def whyNotWork(self):

        for w in self.edge:
            for x in w:
                for y in x:
                    print(y)
                    y = random()
                    self.edge[w][x][y] = y
                    print("y=", y)

    print("random")

    def showEdge(self):
        for x in self.edge:
            print(x)

    def showNode(self):
        print("node")
        for x in self.node:
            print(x)

    def calculateDecision(self, enterNode) -> List:
        sum: float = 0
        for n in range(len(self.node)):
            self.node[n][0] = enterNode[n]
        for w in range(len(self.edge)):
            for x in range(len(self.edge[w])):
                for y in range(len(self.edge[w][x])):
                    sum += self.node[y][w] * self.edge[w][x][y]
                self.node[x][w + 1] = sum
                sum = 0
        self.decision[0] = self.node[0][3]
        self.decision[1] = self.node[1][3]
        return self.decision

    def sampleEnterValue(self):
        sample = [1 for x in range(7)]
        return sample

    def setEdge(self, tab):
        self.edge = tab
