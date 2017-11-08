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
        # for i in range(self.N):
        #     for j in range(self.N):
        #         self.table[i][j] = i + j
        # print(self.table)
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
        # cost of the solution is the number of non hitting queen
        # eg. n = 4 & cost = 2 mean non hitting is 2
        #     n = 4 & cost = 0 mean correct ans
        # print("start")
        # print(solution)
        # print(range(self.N-1))
        overlap = [False] * self.N
        for i in range(self.N-1):
            for j in range(i+1, self.N):
                # print(str(i)+" "+str(j))
                # print(solution)
                
                if self.check_overlap( solution[i], solution[j] ):
                    overlap[i] = True
                    overlap[j] = True
        # print(overlap)
        return overlap.count(False)#, overlap, solution

    def checkTable_true(self):
        sum_ = 0
        for t in self.table:
            sum_ += t.count(0) 
        # print(str(sum_)+" "+str((self.N*self.N)))
        return sum_ == (self.N*self.N - self.N)

    def neighbor(self, state):    
        # random.sample(range(100), 10)
        difX = [0, 0, -1 ,1] # up, down, left, right
        difY = [-1, 1, 0, 0]
        random_queen_list = sample(range(n),n)
        # print("+++++++")
        # print(random_queen_list)
        # print("+++++++")
        finish = False

        for queen in random_queen_list:
            random_action_list = sample(range(4),4)
            # print(random_action_list)
            # print("*******")
            # print( str(state[queen][0])+" "+str(state[queen][1]) )
            for action in random_action_list:
                posiX = state[queen][0] + difX[action]
                posiY = state[queen][1] + difY[action]
                if (posiX >= 0 and posiX < self.N)and \
                    (posiY >= 0 and posiY < self.N)and \
                    (n_queen.table[posiY][posiX] == 0):
                    # self.table[ state[queen][0] ][ state[queen][1] ] = 0
                    # self.table[posiX][posiY] = queen + 1
                    new_state = list(state)
                    new_state[queen] = (posiX,posiY)
                    return new_state
 

    def acceptance_probability(old_cost, new_cost, T):
        # a = e^(c_new-c_old)/ T


        return math.exp(new_cost - old_cost) / T


    def anneal(self, solution):

        old_cost = self.cost(solution)
        T = 1.0
        T_min = 0.001
        alpha = 0.99
        rounds = 0
        while rounds <= 10000:
            i = 1
            # self.print_table()
            while i <= 100:
                new_solution = self.neighbor(solution)

               

                # if new_solution == None:
                #     # n_queen.put_queen(solution)
                #     self.print_table()

                new_cost = self.cost(new_solution)
                diff_cost = new_cost - old_cost
                # ap = acceptance_probability(old_cost, new_cost, T)
                ap = 0.1

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
                        # n_queen.put_queen(solution)
                        # print( "cost :"+str(old_cost) )
                        # self.print_table()
                        # print( str(rounds)+" "+str(T) )

                        
                        return solution, old_cost


                i += 1
            if T >= T_min:
                T = T * alpha
            rounds += 1
            # print("  Round : {} cost: {}".format(rounds, old_cost), end="\r")
            print(str(rounds)+" "+str(T))
        return solution, old_cost

if __name__ == '__main__':
    s = [
        
        (0, 0),
        (1, 1), 
        (2, 2), 
        (3, 3), 
        (4, 4), 
        (5, 5), 
        (6, 6), 
        (7, 7)

        ]

    n = 8
    n_queen = NQueen(n)

    n_queen.put_queen(s)
    # n_queen.print_table()
    solution, old_cost = n_queen.anneal(s)

    # for x in range(10):
    #     print("Progress {:2.1%}".format(x / 10), end="\r")
    # n_queen.print_table()
    print(solution)
    print(old_cost)
    n_queen.put_queen(solution)
    n_queen.print_table()
    # new_state = s

    # for i in range(1000):        
    #     cost_value = n_queen.cost(new_state)
    #     # if cost_value > 0:            
    #     #     n_queen.print_table()  
    #     #     print("cost :"+str(cost_value))
    #     #     print(overlap)
    #     #     print(solution)      
        
    #     new_state = n_queen.neighbor(new_state) 
    #     if not n_queen.checkTable_true():
    #         n_queen.print_table()
    #         print("fail")       
        


    # solution format [(x1,y1),(x2,y2),(x3,y3)]