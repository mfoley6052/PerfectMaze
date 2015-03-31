import random
import turtle
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
            return True
        else:
            return False

class Builder():

    def __init__(self,m,n,start):
        random.seed()
        self.maze = m
        self.position = start
        self.cell = maze[start[0]][start[1]]
        self.n = n
        self.path = myStack([(1,1)])
        self.turt = turtle.Turtle()
        self.turt.ht()
        self.turt.title = "Maze Builder Path"
        self.turt.goto(1,1)
        self.turt.home = (1,1)
        
        
        

    def step(self,y,x):
        self.cell = maze[y][x]
        i = random.choice(tuple(self.cell.neighbours))
        if maze[self.cell.neighbours[i][0]][self.cell.neighbours[i][1]].visited == False:
            self.cell = maze[self.cell.neighbours[i][0]][self.cell.neighbours[i][1]]
            self.path.push((self.cell.y,self.cell.x))
            self.position=(self.cell.y,self.cell.x)
            self.cell.visited = True
            maze[self.position[0]][self.position[1]].visited = True
            print (self.position)
        return self.position
        
                

    def draw(self):
        self.scr = turtle.Screen()
        for p in self.path.stack:
            if p[0] > 0 and p[0] <= self.n and p[1] > 0 and p[1] <= self.n:
                self.turt.pendown()
            else:
                self.turt.penup()

            self.turt.setposition(50*p[1],50*p[0])   
            

                
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
        numNeighbours = len(self.neighbours)
        try:
            if (x-1) < 1:
                del(self.neighbours['W'])
            if (x+1) > self.n:
                del(self.neighbours['E'])
            if (y-1) < 1:
                del(self.neighbours['S'])
            if (y+1) > self.n:
                del(self.neighbours['N'])
            temp = self,neighbours
            for i in {'N','E','W','S'}:
                if maze[self.neighbours[i][0]][self.neighbours[i][1]].visited == True or self.neighbours[i][0] > self.n or self.neighbours[i][0] < 0 or self.neighbours[i][1] > self.n or self.neighbours[i][1] < 0 :
                    del(self.neighbours[i])
            print(self.neighbours)
            if self.neighbours == {}:
                return True
            else:
                self.neighbours = temp
                return False
        except:
            pass
        if numNeighbours <= 0:
            return True
        else:
            return False
    

n = int(input("Enter maze size: "))
maze = []
for y in range(n+2):
    C = []
    for x in range(n+2):
        C.append(cell(y,x,n))
    maze.append(C)
maze[1][1].visited = True
Cam = Builder(maze,n,(1,1))
working = True
y=1
x = 1
isStuck = False
while working:
    isStuck = maze[y][x].refreshNeighbours()
    p = Cam.step(y,x)
    y = p[0]
    x = p[1]
    print(isStuck,maze[y][x].neighbours)
    if isStuck:
        working = False
print (Cam.path.stack)


