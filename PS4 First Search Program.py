# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]

        
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    closed = []
    open = []
    find = False
    resign = False
    open.append([0, init[0], init[1]])
    
    
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[i][k] == 1:
                closed.append([i, k])
    
    while not find and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        
        open.sort(key = lambda x: int(x[0]))
        
        current = open[0]
        closed.append(open[0][1:])
        del open[0]

        if current[1:] == goal:
            find = True
            return current 
            
        for i in range(len(delta)):
            x2 = current[1] + delta[i][0]
            y2 = current[2] + delta[i][1]
            g2 = current[0] + cost
            
            if 0 <= x2 <= len(grid)-1 and 0 <= y2 <= len(grid[0])-1 and [x2, y2] not in closed:
                open.append([g2, x2, y2])
                
            
path = search(grid,init,goal,cost)
print(path)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    