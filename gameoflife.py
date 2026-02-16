import random
import copy

gameArray = [[0]]

def isAlive(x,y):
    if y >= len(gameArray) or x >= len(gameArray[y]) or x < 0 or y < 0:
        return False
    return gameArray[y][x] == 1

def setDead(x,y,l=gameArray):
    l[y][x] = 0

def setAlive(x,y,l=gameArray):
    l[y][x] = 1

def createGrid(length, width):
    return [([0] * width) for x in range(length)]

def prettyprint():
    for x in gameArray:
        for y in x:
            print(y,end="")
        print()


def populate():
    for x in gameArray:
        for y in range(0,len(x)): #Get the index of each item rather than the value
            if random.randint(1,3) == 1:
                x[y] = 1

def numNeighbors(x,y):
    number = 0
    if isAlive(y-1,x-1):
        number+=1
    if isAlive(y-1,x)== 1:
        number+=1
    if isAlive(y-1,x+1)== 1:
        number+=1
    if isAlive(y,x-1)== 1:
        number+=1
    if isAlive(y,x+1)== 1:
        number+=1
    if isAlive(y+1,x-1)== 1:
        number+=1
    if isAlive(y+1,x)== 1:
        number+=1
    if isAlive(y+1,x+1)== 1:
        number+=1

    return number

