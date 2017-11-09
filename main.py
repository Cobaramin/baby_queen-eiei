import math
# import random as random
from random import random
from random import randint
from random import sample

class NQueen(object):

    def __init__(self, N):
        self.N = N
        self.table = [[0] * N for _ in range(N)]

    def print_table(self):
        print("-------------")
      
        for row in self.table:
            print(row)
        print("-------------")

    def put_queen(self, solution):
        self.table = [[0] * self.N for _ in range(self.N)]
        for i,s in enumerate(solution):
            self.table[s[1]][s[0]] = i+1

    def check_overlap(self, posi1, posi2):
        same_colum = posi1[0] == posi2[0]
        same_row = posi1[1] == posi2[1]
        same_dec_m = posi1[0]-posi1[1] == posi2[0]-posi2[1]
        same_inc_m = posi1[0]+posi1[1] == posi2[0]+posi2[1]
        return same_colum or same_row or same_dec_m or same_inc_m

    def cost(self, solution): 
        # cost of the solution is the number of queen that isn't overlap other queen(correct postion)
        # eg. n = 4 & cost = 2 mean there are 2 queen that are correct position
        #     n = 4 & cost = 0 mean all queen is overlap
        overlap = [False] * self.N
        for i in range(self.N-1):
            for j in range(i+1, self.N):
                if self.check_overlap( solution[i], solution[j] ):
                    overlap[i] = True
                    overlap[j] = True
        return overlap.count(False)#, overlap, solution

    def checkTable_true(self):  # for check bug
        sum_ = 0
        for t in self.table:
            sum_ += t.count(0) 
        return sum_ == (self.N*self.N - self.N)

    def neighbor(self, state):    
        difX = [0, 0, -1 ,1] # up, down, left, right
        difY = [-1, 1, 0, 0]
        random_queen_list = sample(range(n),n) # random queen array for next state
        finish = False

        for queen in random_queen_list:
            random_action_list = sample(range(4),4)  # random action array for next state

            for action in random_action_list:

                posiX = state[queen][0] + difX[action]
                posiY = state[queen][1] + difY[action]

                top_down_check = posiX >= 0 and posiX < self.N
                left_right_check = posiY >= 0 and posiY < self.N
                # empty_check = n_queen.table[posiY][posiX] == 0
                if top_down_check and left_right_check and (n_queen.table[posiY][posiX] == 0) :  #can move queen to this direction
                    new_state = list(state)
                    new_state[queen] = (posiX,posiY) 
                    return new_state
 

    def acceptance_probability(self, diff_cost, T):

        return math.exp( diff_cost / T  )


    def anneal(self, solution):

        old_cost = self.cost(solution)
        T = 1.0
        T_min = 0.001
        alpha = 0.99
        rounds = 0
        while rounds <= 200:
            i = 1
            # self.print_table()
            while i <= 5000:
                new_solution = self.neighbor(solution)
                new_cost = self.cost(new_solution)
                diff_cost = new_cost - old_cost
                ap = self.acceptance_probability( diff_cost , T)
                # ap = T
                # if diff_cost <= 0:
                #     print("     ap: "+str(T)+" "+str(ap)+" "+str(diff_cost))
                if diff_cost > 0 or ap > random():
                    old_solution = solution
                    solution = new_solution
                    old_cost = new_cost
                    n_queen.put_queen(solution)
                    

                    if not self.checkTable_true():
                        self.print_table()
                        print("fail")
                        print(old_solution)
                        print(solution)
                        break

                    if new_cost == self.N:
                        return solution, old_cost


                i += 1
            if T >= T_min:
                T = T * alpha
            rounds += 1
            # print("  Round : {} cost: {}".format(rounds, old_cost), end="\r")
            print(str(rounds)+" "+str(T)+" "+str(old_cost))
        return solution, old_cost

if __name__ == '__main__':
    start_state = [

        (0, 0),
        (1, 1), 
        (2, 2), 
        (3, 3), 
        (4, 4), 
        (5, 5), 
        (6, 6), 
        (7, 7)

        ]

    n = 5
    s = start_state[:n]
    n_queen = NQueen(n)

    n_queen.put_queen(s)
    solution, old_cost = n_queen.anneal(s)

    print(solution)
    print(old_cost)
    n_queen.put_queen(solution)
    n_queen.print_table()
