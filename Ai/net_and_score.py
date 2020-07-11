from Ai.net import Net


class NetAndScore:
    def __init__(self, net: Net, score: int):
        self.net = net
        self.score = score
