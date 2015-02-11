#Mitchell Foley
#1316506
#foleymb
#Comp Sci 1XA3 Final Project Spring 2015

#Build and solve perfect mazes

#Dependencies
import random

#Stack Datatype
class myStack():

    def __init__(self,initial=[]):
        #some init vars
        self.stack = initial
        
    def push(self,item):
        #Add item to top of stack S
        self.stack.append(item)

    def pop(self):
        #Remove the top item from S and returns it
        a,b = self.stack[:(len(self.stack)-2)],self.stack[len(self.stack)-1]
        self.stack = a
        return b

    def isEmpty(self):
        #If S is empty, return true, otherwise False
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        #The size of the stack
        return len(self.stack)

#A single cell of the nxn grid        
class cell():
    #Setting up required properties of a cell
    def __init__(self,x,y,isStart = False,isEnd = False,cType='F',order=15,visited=False):
        self.x = x
        self.y = y
        self.cType = cType
        self.order = order
        self.visited = visited
        self.isStart =isStart
        self.isEnd = isEnd
        if (x == 1) or (y == 1):
            self.border = True
        else:
            self.border = False
        
#nxn Perfect Maze               
class PerfectMaze():

    def __init__(self,n):
        self.cells = range(16)
        self.cellTypes = ['O','T','R','L','B','TL','TR','BL','BR','LR','TB','TLB','TLR','BLR','TRB','F']
        self.north,self.east,self.south,self.west = [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2)
        self.maze = [[None]*(n+2)]*(n+2)
        self.steps = [0,0]
        self.ends = [None,None]
        self.n = n

    def display(self):
        for a in range(len(self.maze)):
            for i in [self.maze[a],self.north[a],self.east[a],self.south[a],self.west[a]]:
                print(i)
    
                
    
                                        

    def build(self):
        
        def checkDone(self):
            done = False
            s = 0
            for x in range(1,self.n+1):
                for y in range(1,self.n+1):
                    if self.maze[x][y].visited == True:
                        s += 1
            if s == self.n**2:
                done = True
            return done

        def walk(self,x,y,p):
            progress = self.steps[0]
            px = p[0]
            py = p[1]
            current = self.maze[x][y]
            current.visited = True
            self.maze[x][y] = current
            cNext = self.maze[x+px][y+py]
            
            if cNext != None:
                if cNext.border == False and cNext.visited == False:
                    current = cNext
                    current.visited = True                
                    if (px,py) == (0,1):
                        self.north[x][y],self.south[x][y+py] = False,False
                    elif (px,py) == (1,0):
                        self.east[x][y],self.west[x+px][y] = False,False
                    elif (px,py) == (0,-1):
                        self.south[x][y],self.north[x][y+py] = False,False
                    elif (px,py) == (-1,0):
                        self.west[x][y],self.east[x+px][y] = False,False
                    self.maze[x+px][y+py] = current
                    x += px
                    y += py
                else:
                    cNext.visited = True
                    self.maze[x+px][y+py] = cNext
                t=0
                for a in range(len(self.maze)):
                    for b in range(len(self.maze[a])):
                        if self.maze[a][b] != None:
                            if self.maze[a][b].visited == True:
                                t += 1
                if (t > progress):
                    self.steps[0] += abs(t-progress)
                    progress += t

        point = [1,1]
        steps = 1
        progress = checkDone(self)
        while progress == False:
                skip = False
                print("Currently at: ",point)
                pick = random.randint(0,3)
                print("Computer chose side ",pick+1)
                choices = [(0,1),(1,0),(0,-1),(-1,0)]
                if (point[0]+choices[pick][0]) > 0 and (point[1] + choices[pick][1]) > 0 and (point[0]+choices[pick][0]) <= self.n and  (point[1] + choices[pick][1]) <= self.n:
                    print("valid next cell")
                    nextCell = [point[0]+choices[pick][0],point[1] + choices[pick][1]]
                else:
                    skip = True
                if not(skip):
                    steps += 1
                    print("Walking from ", point , " to ", nextCell)
                    walk(self,point[0],point[1],choices[pick])
                    point[0] += choices[pick][0]
                    point [1] += choices[pick][1]
                progress = checkDone(self)               
                print("The maze is done: ", progress)

        
        def pickStarts(self):
            endsPick = [0,0]
            while endsPick[0] == endsPick[1]:
                endsPick[0] = random.randint(1,4*(self.n-1))
                endsPick[1] = random.randint(1,4*(self.n-1))
                
            f = [None,None]
            g = [None,None]
            
            for b in range(2):
                print(b,endsPick[b])
                for i in range(1,5):
                    if f[0] == None or f[1] == None or g[0] == None or g[1] == None:
                        print(endsPick[b], i*(self.n-1)) 
                        if endsPick[b] < i*(self.n-1):
                            print("Less than ^")
                            if i == 1:
                                print("i=",i)
                                f[b] = endsPick[b]
                                g[b] = self.n-1
                                
                            elif i ==2:
                                print("i=",i)
                                f[b] = self.n-1
                                g[b] = endsPick[b] - (self.n-1)
                                
                            elif i ==3:
                                print("i=",i)
                                f[b] = endsPick[b] -2*(self.n-1)
                                g[b] = 1
                                
                            elif i ==4:
                                print("i=",i)
                                f[b] = 1
                                g[b] = endsPick[b] -3*(self.n-1)
                                
            self.ends[0] = self.maze[f[0]][g[0]]
            self.ends[0].isStart = True
            self.ends[1] = self.maze[f[1]][g[1]]
            self.ends[1].isEnd = True
    
    def fresh(self):
        for x in range((self.n+2)):
            for y in range(self.n+2):
                    self.maze[x][y] = cell(x,y)
                    self.north[x][y],self.east[x][y],self.south[x][y],self.west[x][y] = True,True,True,True
                    if x == self.n or y ==self.n:
                        self.maze[x][y].border = True

 