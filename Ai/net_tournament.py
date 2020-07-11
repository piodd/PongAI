from Ai.net import Net
from Ai import net_menager
from Ai.net_and_score import NetAndScore
import random


class Tournament:
    def __init__(self, number_of_ai, number_of_rounds):
        self.number_of_ai = number_of_ai
        self.number_of_rounds = number_of_rounds
        self.ai_list = []
        for x in range(number_of_ai):
            self.ai_list.append(NetAndScore(Net(), x))
        self.ai_list.sort(key=value, reverse=False)
        self.rounds_counter = 0
        self.game_in_round_counter = 0
        self.generation_counter = 0

    def compere_net(self, net1: NetAndScore, net2: NetAndScore) -> int:
        if net1.score < net2.score:
            return 1
        if net1.score > net2.score:
            return -1
        else:
            return 0

    def next_pair(self):
        print("nr==", self.game_in_round_counter)
        self.game_in_round_counter += 1
        if self.game_in_round_counter >= self.number_of_ai:
            self.next_round()
        return [self.ai_list[self.game_in_round_counter],
                self.ai_list[(self.game_in_round_counter + 1) % self.number_of_ai]]

    def next_round(self):
        self.ai_list.sort(key=value, reverse=True)
        for net_score in self.ai_list:
            print(net_score.score)
        self.game_in_round_counter = 0
        self.next_gen()
        return 0

    def next_gen(self):
        temp_list = self.ai_list.copy()
        the_best_net_list = []
        temp_net_list = []
        for x in range(self.number_of_ai // 3):
            the_best_net_list.append(self.ai_list[x].net)
            print(the_best_net_list[x])
        for x in range(self.number_of_ai):
            temp_net_list.append(net_menager.childNet(the_best_net_list[x % len(the_best_net_list)],
                                                      0.001 + 0.1 * (
                                                                  self.generation_counter + 2 / (self.generation_counter + 1))))
        self.ai_list.clear()
        for n in temp_net_list:
            self.ai_list.append(NetAndScore(n, 0))
        random.shuffle(self.ai_list)


def value(net1: NetAndScore) -> int:
    return net1.score
