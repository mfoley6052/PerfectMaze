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
            return true
        else:
            return False

class Builder():

    def __init__(self,m,n,start):
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
        
        
        

    def step(self):
        for y in range(1,self.n+2):
            for x in range(1,self.n+2):
                self.cell = maze[y][x]
                i = random.choice(tuple(self.cell.neighbours))
                self.cell = maze[self.cell.neighbours[i][0]][self.cell.neighbours[i][1]]
                self.path.push((y,x))
                self.position=(y,x)
                self.cell.visited = True
                maze[self.position[0]][self.position[1]].visited = True
            
                

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

Cam = Builder(maze,n,(1,1))
Cam.step()
print (Cam.path.stack)


