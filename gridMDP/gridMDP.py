import numpy as np
import matplotlib.pyplot as plt

"""

0: up: (r-1, c)
1: down: (r+1, c)
2: left: (r, c-1)
3: right: (r, c+1)

"""
class Environment:

    def __init__(self, grid, p):

        self.grid = grid
        self.p = p
        self.m = len(grid)
        self.n = len(grid[0])
    
    def prob(self, r, c, r_d, c_d, a):
        
        count = 0
        if r - 1 >= 0 and self.grid[r-1][c] == '#':
            count += 1
        if r + 1 < self.m and self.grid[r+1][c] == '#':
            count += 1
        if c - 1 >= 0 and self.grid[r][c-1] == '#':
            count += 1
        if c + 1 < self.n and self.grid[r][c+1] == '#':
            count += 1

        if self.grid[r][c] == 'g' and r_d == r and c_d == c:
            return 1

        if (count == 4 or (count == 3 and (r == 0 or c == 0 or r == self.m-1 or c == self.n-1)) or (count == 2 and ((r == 0 and c == 0) or (r == 0 and c == self.n-1) or (r == self.m-1 and c == 0) or (r == self.m-1 and c == self.n-1)))):
            if r_d == r and c_d == c:
                return 1
            else:
                return 0

        if ((r_d == r-1 and c_d == c) or (r_d == r+1 and c_d == c) or (r_d == r and c_d == c-1) or (r_d == r and c_d == c+1)) == False:
            return 0
        
        if self.grid[r_d][c_d] == '#' or self.grid[r][c] == 'g':
            return 0
        
        if self.grid[r][c] == '#':
            return 0
        
        if r-1 >= 0 and self.grid[r-1][c] == 'g':
            if a == 0 and r_d == r-1:
                return 1
            else:
                return 0

        if r+1 < self.m and self.grid[r+1][c] == 'g':
            if a == 1 and r_d == r+1:
                return 1
            else:
                return 0

        if c-1 >= 0 and self.grid[r][c-1] == 'g':
            if a == 2 and c_d == c-1:
                return 1
            else:
                return 0

        if c+1 < self.n and self.grid[r][c+1] == 'g':
            if a == 3 and c_d == c+1:
                return 1
            else:
                return 0
        
        if a == 0:

            if r == 0:
                if c == 0 or c == self.n-1:
                    return 1.0 / 2.0
                else:
                    return 1.0 / 3.0
            elif r == self.m-1:
                if r_d == r - 1:
                    return self.p
                else:
                    if c == 0 or c == self.n-1:
                        return (1.0 - self.p)
                    else:
                        return (1.0 - self.p) / 2.0
            else:
                if r_d == r - 1:
                    return self.p
                else:
                    if c == 0 or c == self.n-1:
                        return (1.0 - self.p) / 2.0
                    else:
                        return (1.0 - self.p) / 3.0
        elif a == 1:

            if r == self.m-1:
                if c == 0 or c == self.n-1:
                    return 1.0 / 2.0
                else:
                    return 1.0 / 3.0
            elif r == 0:
                if r_d == r + 1:
                    return self.p
                else:
                    if c == 0 or c == self.n-1:
                        return (1.0 - self.p)
                    else:
                        return (1.0 - self.p) / 2.0
            else:
                if r_d == r + 1:
                    return self.p
                else:
                    if c == 0 or c == self.n-1:
                        return (1.0 - self.p) / 2.0
                    else:
                        return (1.0 - self.p) / 3.0

        elif a == 2:

            if c == 0:
                if r == 0 or r == self.m-1:
                    return 1.0 / 2.0
                else:
                    return 1.0 / 3.0
            elif c == self.n-1:
                if c_d == c - 1:
                    return self.p
                else:
                    if r == 0 or r == self.m-1:
                        return (1.0 - self.p)
                    else:
                        return (1.0 - self.p) / 2.0
            else:
                if c_d == c - 1:
                    return self.p
                else:
                    if r == 0 or r == self.m-1:
                        return (1.0 - self.p) / 2.0
                    else:
                        return (1.0 - self.p) / 3.0
        
        else:

            if c == self.n-1:
                if r == 0 or r == self.m-1:
                    return 1.0 / 2.0
                else:
                    return 1.0 / 3.0
            elif c == 0:
                if c_d == c + 1:
                    return self.p
                else:
                    if r == 0 or r == self.m-1:
                        return (1.0 - self.p)
                    else:
                        return (1.0 - self.p) / 2.0
            else:
                if c_d == c + 1:
                    return self.p
                else:
                    if r == 0 or r == self.m-1:
                        return (1.0 - self.p) / 2.0
                    else:
                        return (1.0 - self.p) / 3.0
    def reward(self, r, c, a):
        
        if self.grid[r][c] == '#':
            return 0
        
        if a == 0:

            if r-1 < 0 or self.grid[r-1][c] == '#':
                return -100
            if self.grid[r-1][c] == 'g':
                return 100

        elif a == 1:

            if r+1 >= self.m or self.grid[r+1][c] == '#':
                return -100
            if self.grid[r+1][c] == 'g':
                return 100
        
        elif a == 2:

            if c-1 < 0 or self.grid[r][c-1] == '#':
                return -100
            if self.grid[r][c-1] == 'g':
                return 100

        elif a == 3:
            
            if c+1 >= self.n or self.grid[r][c+1] == '#':
                return -100
            if self.grid[r][c+1] == 'g':
                return 100
        
        return 0
    
    def return_data(self):
        return self.m, self.n, 4


def BellmanOp(env, Q, m, n, a_size, gamma = 0.9):

    TQ = np.zeros(Q.shape)

    for r in range(m):
        for c in range(n):
            for a in range(a_size):
                TQ[r][c][a] = env.reward(r, c, a)
                for r_d in range(m):
                    for c_d in range(n):
                        TQ[r][c][a] += gamma * env.prob(r, c, r_d, c_d, a) * np.max(Q[r_d][c_d])
    return TQ

def valueIter(env, iters):

    m, n, a_size = env.return_data()
    Q = np.zeros((m, n, a_size))

    for t in range(iters):
        Q = BellmanOp(env, Q, m, n, a_size)
    
    V = np.zeros((m, n))
    pred = np.zeros((m, n))

    for r in range(m):
        for c in range(n):
            V[r][c] = np.max(Q[r][c])
            pred[r][c] = np.argmax(Q[r][c])
    
    return V, pred

def print_ans(pred, grid):

    for i in range(len(grid)):
        s = ""
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                s += '#'
            else:
                if pred[i, j] == 0:
                    s += 'u'
                elif pred[i, j] == 1:
                    s += 'd'
                elif pred[i, j] == 2:
                    s += 'l'
                else:
                    s += 'r'
        print(s)



def main():

    p = 0.5

    with open('grid', 'r') as fl:
        grid = []
        for line in fl.readlines():
            row = []
            for x in line:
                if x == '\n':
                    continue
                row.append(x)
            grid.append(row[:])
    
    env = Environment(grid, p)
    V, pred = valueIter(env, 70)
    print_ans(pred, grid)



if __name__ == '__main__':
    main()