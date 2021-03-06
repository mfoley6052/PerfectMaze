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
    def __init__(self,x,y,isStart = False,isEnd = False,visited=False):
        self.x = x
        self.y = y
        self.visited = visited
        self.isStart =isStart
        self.isEnd = isEnd
        
#nxn Perfect Maze               
class PerfectMaze():

    def __init__(self,n):
        self.north,self.east,self.south,self.west = [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2), [[None]*(n+2)]*(n+2)
        self.maze = [[None]*(n+2)]*(n+2)
        self.steps = [0,0]
        self.ends = [None,None]
        self.n = n
        self.stuck = False

    def display(self):
        M = []
        for x in range(self.n+2):
            N = []
            for y in range(self.n+2):
                N.append(((x,y),self.maze[x][y].visited))
            M.append(N)
            print (M[x])
    
    def displayWalls(self):
        for a in range(len(self.maze)):
            for i in [self.maze[a],self.north[a],self.east[a],self.south[a],self.west[a]]:
                print(i)                                       

    def build(self):
        
        def checkDone(self):
            if self.steps[0]+1 == 2*self.n**2:
                return True
            else:
                return False

        def walk(self,x,y,p):
            #print("(x,y): ",(x,y),"  increment: ",(px,py),"  next: ", (x+px,y+py))
            if self.maze[p[0]][p[1]]  != None:
#                print ("Visited: ",self.maze[x+px][y+py].visited)
                if self.maze[p[0]][p[1]].visited == False:
                    self.maze[p[0]][p[1]].visited = True
                    self.steps[0] += 1
                    if (p[0]-x,p[1]-y) == (0,1):
                        self.north[x][y],self.south[p[0]][p[1]] = False,False
                    elif (p[0]-x,p[1]-y) == (1,0):
                        self.east[x][y],self.west[p[0]][p[1]] = False,False
                    elif (p[0]-x,p[1]-y) == (0,-1):
                        self.south[x][y],self.north[p[0]][p[1]] = False,False
                    elif (p[0]-x,p[1]-y) == (-1,0):
                        self.west[x][y],self.east[p[0]][p[1]] = False,False
                    #else:

        def pickDirection(bad=None,dirs={0,1,2,3}):
            pick = random.randint(0,3)
            dirs = {0,1,2,3}
            if bad != None:
                if type(bad) == int:
                    dirs.remove(bad)
                else:
                    for i in bad:
                        dirs.remove(i)
            print("Dir pick: ",pick,"      Available Dirs: ", dirs, "     bad dir:  ",bad)
            while pick not in dirs and dirs != {}:
                print ("pick: ",pick,"     dirs: ",dirs)
                if pick in dirs:
                    dirs.remove(pick)
                if type(bad) == list:
                    pick = pickDirection(bad.append(pick),dirs)
                else:
                    pick = pickDirection([bad].append(pick),dirs)
                
            if dirs != {}:
                 return pick
            else:
                return -1
            
        def moveInDirection(self,curr,direction):
            choices = [(0,1),(1,0),(0,-1),(-1,0)]
            if direction == -1:
                self.stuck = True
            nextCell = [curr[0] + choices[direction][0],curr[1] + choices[direction][1]]
#            print("next Cell: ",nextCell)
           # if self.maze[choices[direction][0]][choices[direction][1]].visited == False:
            if nextCell[0] > 0 and nextCell[0] < self.n+1:
#                print("Next x value is good: ",nextCell[0])
                if nextCell[1] > 0 and nextCell[1] < self.n+1:
#                    print("Next y value is good: ",nextCell[1])
                    walk(self,curr[0],curr[1],[choices[direction][0],choices[direction][1]])
#                    print("direction: ",direction)
                    print("Walking from ", curr , " to ", nextCell)
#                    print("nextCell: ",nextCell)
                    return nextCell
                else:
#                    print("Bad y direction!")
                    direction = pickDirection(direction)
#                    print("direction: ",direction)
                    return moveInDirection(self,curr,direction)
                    
            else:
#                print("Bad x direction!")
                direction = pickDirection(direction)
#                print("direction: ",direction)
                return moveInDirection(self,curr,direction)
                
##            else:
##                print("Next direction has been visited!")
##                direction = pickDirection(direction)
##                print("direction: ",direction)
##                moveInDirection(self,curr,direction)
                
        point = [0,1]
        prog = False

        while prog == False:
#                print("point: ",point)
#                print("Currently at: ",point)
                point = moveInDirection(self,point,pickDirection())                       
                prog = checkDone(self)               

        
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
        random.seed()
        for x in range((self.n+2)):
            for y in range(self.n+2):
                    self.maze[x][y] = cell(x,y)
                    self.north[x][y],self.east[x][y],self.south[x][y],self.west[x][y] = True,True,True,True
        self.maze[1][1].visited = True


A = PerfectMaze(eval(input("Enter maze size: ")))
A.fresh()
A.build()
