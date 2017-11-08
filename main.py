import math
from random import random


class NQueen(object):

    def __init__(self, N):
        self.N = N
        self.table = [[0] * N for _ in range(N)]

    def print_table(self):
        # for i in range(self.N):
        #     for j in range(self.N):
        #         self.table[i][j] = i + j
        print(self.table)

    def put_queen(self, solution):
        for s in solution:
            self.table[s[0]][s[1]] = 1

    def cost(self, solution):
        # cost of the solution is the number of non hitting queen
        # eg. n = 4 & cost = 2 mean non hitting is 2
        #     n = 4 & cost = 0 mean correct ans

        pass


def neighbor(solution):
    pass


def acceptance_probability(old_cost, new_cost, T):
    # a = e^(c_new-c_old)/ T
    return math.exp(new_cost - old_cost) / T


def anneal(solution):

    old_cost = cost(solution)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9

    while T > T_min:
        i = 1
        while i <= 100:
            new_solution = neighbor(solution)
            new_cost = cost(new_solution)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                solution = new_solution
                old_cost = new_cost

            i += 1
        T = T * alpha
    return solution, old_cost

if __name__ == '__main__':
    s = [(0, 0), (1, 1), (2, 2)]
    n_queen = NQueen(4)
    n_queen.print_table()
    # n_queen.put_queen(s)

    # solution format [(x1,y1),(x2,y2),(x3,y3)]
