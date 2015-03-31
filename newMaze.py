class myStack():

    def __init__(self,initial = []):
        self.stack = initial

    def push(self,item):
        self.stack.append(item)

    def pop(self):

        a,b = self.stack[:(len(self.stack)-2)],self.stack[len(self.stack)-1]
        self.stack = a
        return b

    def isEmpty(self):

        if len(self.stack) == 0:
            return true
        else:
            return False
    

class cell():

    def __init__(self,y,x,n):
        self.x = x
        self.y = y
        self.n = n
        self.neighbours = {'N':(y+1,x),'E':(y,x+1),'W':(y,x-1),'S':(y-1,x)}
        if (x-1) < 1:
            del(self.neighbours['W'])
        if (x+1) > self.n:
            del(self.neighbours['E'])
        if (y-1) < 1:
            del(self.neighbours['S'])
        if (y+1) > self.n:
            del(self.neighbours['N'])
        self.visited = False

    def refreshNeighbours(self):
        x = self.x
        y = self.y
        if (x-1) < 1:
            del(self.neighbours['W'])
        if (x+1) > self.n:
            del(self.neighbours['E'])
        if (y-1) < 1:
            del(self.neighbours['S'])
        if (y+1) > self.n:
            del(self.neighbours['N'])
    

n = int(input("Enter maze size: "))
maze = []
for y in range(n+2):
    C = []
    for x in range(n+2):
        C.append(cell(y,x,n))
    maze.append(C)

class Builder():

    def __init__(self,m,n):
        self.maze = m
        self.n = n
        self.path = myStack((1,1))

    def step(self):
        for y in range(
    
