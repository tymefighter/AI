import numpy as np
import math

"""

0: (r-1, c): up
1: (r+1, c): down
2: (r, c-1): left
3: (r, c+1): right

"""

def print_mat(a):

    for row in a:
        s = ''
        for x in row:
            s += ' ' + str(x)
        print(s)

def print_grid(grid):

    for row in grid:
        s = ''
        for x in row:
            s += x
        print(s)

def reward(grid, r, c, a):
    m = len(grid)
    n = len(grid[0])

    if grid[r][c] == '#':
        return 0

    if a == 0:
        # up
        if r-1 < 0 or grid[r-1][c] == '#':
            return -100
        
        if grid[r-1][c] == 'g':
            return 100

    elif a == 1:
        # down
        if r + 1 >= m or grid[r+1][c] == '#':
            return -100
        
        if grid[r+1][c] == 'g':
            return 100     
    
    elif a == 2:
        # left
        if c - 1 < 0 or grid[r][c-1] == '#':
            return -100
        
        if grid[r][c-1] == 'g':
            return 100

    elif a == 3:
        # right
        if c + 1 >= n or grid[r][c+1] == '#':
            return -100
        
        if grid[r][c+1] == 'g':
            return 100
    
    return 0

def prob(p, grid, a, r, c, r_d, c_d):
    m = len(grid)
    n = len(grid[0])
    if ((r_d == r and c_d == c) or (r_d == r-1 and c_d == c) or (r_d == r+1 and c_d == c) or (r_d == r and c_d == c-1) or (r_d == r and c_d == c+1)) == False:
        return 0

    count = 0
    up = False
    down = False
    left = False
    right = False

    if r-1 < 0 or grid[r-1][c] == '#':
        count += 1
        up = True
    
    if r+1 >= m or grid[r+1][c] == '#':
        count += 1
        down = True

    if c-1 < 0 or grid[r][c-1] == '#':
        count += 1
        left = True
    
    if c+1 >= n or grid[r][c+1] == '#':
        count += 1
        right += True

    

    if r_d == r and c_d == c:
        if grid[r][c] == 'g' or count == 4 or grid[r][c] == '#':
            return 1
        else:
            return 0
    
    if grid[r][c] == 'g' or count == 4 or grid[r][c] == '#':
        return 0
    #print(str(count) + " " + str(up) + " "  +str(down)+" "+str(left) +" "+str(right))


    if a == 0:

        if up:
            if r_d == r-1:
                return 0
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                return 1.0 / (4.0 - count)
        else:
            if r_d == r-1:
                if count == 3:
                    return 1.0
                else:
                    return p
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                if count == 3:
                    return 0
                else:
                    return (1.0 - p) / (3.0 - count)
    elif a == 1:

        if down:
            if r_d == r+1:
                return 0
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                return 1.0 / (4.0 - count)
        else:
            if r_d == r+1:
                if count == 3:
                    return 1.0
                else:
                    return p
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                if count == 3:
                    return 0
                else:
                    return (1.0 - p) / (3.0 - count)
    elif a == 2:

        if left:
            if c_d == c-1:
                return 0
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                return 1.0 / (4.0 - count)
        else:
            if c_d == c-1:
                if count == 3:
                    return 1.0
                else:
                    return p
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                if count == 3:
                    return 0
                else:
                    return (1.0 - p) / (3.0 - count)
    else:

        if right:
            if c_d == c+1:
                return 0
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                return 1.0 / (4.0 - count)
        else:
            if c_d == c+1:
                if count == 3:
                    return 1.0
                else:
                    return p
            elif grid[r_d][c_d] == '#':
                return 0
            else:
                if count == 3:
                    return 0
                else:
                    return (1.0 - p) / (3.0 - count)

def BellmanOp(Q, p, grid, gamma = 0.9):

    TQ = np.zeros(Q.shape)
    m = len(grid)
    n = len(grid[0])

    for r in range(m):
        for c in range(n):
            for a in range(4):
                TQ[r][c][a] = reward(grid, r, c, a)
                for r_d in range(m):
                    for c_d in range(n):
                        TQ[r][c][a] += gamma * prob(p, grid, a, r, c, r_d, c_d) * np.max(Q[r_d][c_d])
    
    return TQ

def valueIter(p, grid, iters, gamma = 0.9):

    m = len(grid)
    n = len(grid[0])
    Q = np.zeros((m, n, 4))
    V = np.zeros((m, n))
    pred = np.zeros((m, n))

    for i in range(iters):
        Q = BellmanOp(Q, p, grid, gamma)
    
    for r in range(m):
        for c in range(n):
            V[r][c] = - math.inf
            for a in range(4):
                val = reward(grid, r, c, a)
                for r_d in range(m):
                    for c_d in range(n):
                        val += gamma * prob(p, grid, a, r, c, r_d, c_d) * np.max(Q[r_d][c_d])
                if val > V[r][c]:
                    pred[r][c] = a
                    V[r][c] = val
    return V, pred


def main():
    p = 0.8
    with open('grid', 'r') as fl:
        grid = []
        for line in fl.readlines():
            arr = []
            for x in line:
                if x != '\n':
                    arr.append(x)
            grid.append(arr)
            
        print_grid(grid)

    V, pred = valueIter(p, grid, 20)
    print_mat(V)
    print_mat(pred)
    #print(prob(p, grid, 3, 4, 2, 4, 3))
if __name__ == '__main__':

    main()