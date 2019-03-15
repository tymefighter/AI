import os
import show
import Queue
from math import sqrt

def print_mat(a):
    for row in a:
        s = ''
        for x in row:
            s += x
        print(s)
    print('\n')


def ed(r1, c1, r2, c2):

    return sqrt((r1 - r2)*(r1 - r2) + (c1 - c2)*(c1 - c2))

def DFS(grid, start_r, start_c, end_r, end_c):

    m = len(grid)
    n = len(grid[0])
    path_exists = False
    path_grid = [row[:] for row in grid]
    path = [[None for i in range(n)] for i in range(m)]
    dist = [[None for i in range(n)] for i in range(m)]
    pq = Queue.PriorityQueue()

    r = start_r
    c = start_c
    dist[r][c] = 0
    pq.put((dist[r][c] + ed(r, c, end_r, end_c), r, c, None, None))

    while pq.empty() == False:

        val, r, c, pred_r, pred_c = pq.get()
        if grid[r][c] == 'x':
            continue
        path[r][c] = (pred_r, pred_c)
        grid[r][c] = 'x'
        if r == end_r and c == end_c:
            path_exists = True
            break
        
          

        if r-1 >= 0 and (grid[r-1][c] == '.' or grid[r-1][c] == 'e'):
            dist[r-1][c] = dist[r][c] + 1
            pq.put((dist[r-1][c] + ed(r-1, c, end_r, end_c), r-1, c, r, c))
            
        if r+1 < m and (grid[r+1][c] == '.' or grid[r+1][c] == 'e'):
            dist[r+1][c] = dist[r][c] + 1
            pq.put((dist[r+1][c] + ed(r+1, c, end_r, end_c), r+1, c, r, c))
            
        if c-1 >= 0 and (grid[r][c-1] == '.' or grid[r][c-1] == 'e'):
            dist[r][c-1] = dist[r][c] + 1
            pq.put((dist[r][c-1] + ed(r, c-1, end_r, end_c), r, c-1, r, c))

        if c+1 < n and (grid[r][c+1] == '.' or grid[r][c+1] == 'e'):
            dist[r][c+1] = dist[r][c] + 1
            pq.put((dist[r][c+1] + ed(r, c+1, end_r, end_c), r, c+1, r, c))
            
        if r-1 >= 0 and c-1 >= 0 and (grid[r-1][c-1] == '.' or grid[r-1][c-1] == 'e'):
            dist[r-1][c-1] = dist[r][c] + 1
            pq.put((dist[r-1][c-1] + ed(r-1, c-1, end_r, end_c), r-1, c-1, r, c))  
        
        if r-1 >= 0 and c+1 < n and (grid[r-1][c+1] == '.' or grid[r-1][c+1] == 'e'):
            dist[r-1][c+1] = dist[r][c] + 1
            pq.put((dist[r-1][c+1] + ed(r-1, c+1, end_r, end_c), r-1, c+1, r, c))
        
        if r+1 < m and c-1 >= 0 and (grid[r+1][c-1] == '.' or grid[r+1][c-1] == 'e'):
            dist[r+1][c-1] = dist[r][c] + 1
            pq.put((dist[r+1][c-1] + ed(r+1, c-1, end_r, end_c), r+1, c-1, r, c))
        
        if r+1 < m and c+1 < n and (grid[r+1][c+1] == '.' or grid[r+1][c+1] == 'e'):
            dist[r+1][c+1] = dist[r][c] + 1
            pq.put((dist[r+1][c+1] + ed(r+1, c+1, end_r, end_c), r+1, c+1, r, c))
        show.printMat(grid)

       
    if path_exists:
        r = end_r
        c = end_c
        while r != None and c != None and path[r][c] != None:
            path_grid[r][c] = 'a'
            r, c = path[r][c]
            show.printMat(path_grid)
        path_grid[start_r][start_c] = 's'
        path_grid[end_r][end_c] = 'e'

def main():

    m = int(input("m: "))
    n = int(input("n: "))

    start_r = int(input("start row: "))
    start_c = int(input("start col: "))

    end_r = int(input("end row: "))
    end_c = int(input("end col: "))


    grid = [['.' for i in range(n)] for i in range(m)]
    grid[start_r][start_c] = 's'
    grid[end_r][end_c] = 'e'

 
    print("Enter obstacle locations: - (enter a negative value to exit)")

    r = c = 0
    while r >= 0 and c >= 0:
        r = int(input("r: "))
        c = int(input("c: "))

        if r >= 0 and c >= 0:
            grid[r][c] = '#'
    os.system('clear')
    DFS(grid, start_r, start_c, end_r, end_c)
if __name__ == '__main__':
    main()
