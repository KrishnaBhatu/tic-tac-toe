import numpy as np
import copy

class TicTacToe:

    def __init__(self, boardPosition, move, layerNumber, parent = None):

        self.boardPosition = boardPosition
        self.parent = parent
        self.myMove = move
        self.layerNumber = layerNumber
        self.children = []
        if(parent == None):
            self.myCost = 0
        else:
            self.myCost = self.calcMyCost()

    def findEmptyPosition(self):
        emptyPositionList = []
        for i in range(0, len(self.boardPosition)):
            if(self.boardPosition[i] == 0):
                emptyPositionList.append(i)

        return emptyPositionList

    def extractNode(self):
        emptyPositionList = self.findEmptyPosition()
        for i in emptyPositionList:
            boardPositionTemp = self.getMyCopy()
            if(self.myMove == 1):
                boardPositionTemp[i] = -1
                child = TicTacToe(boardPositionTemp, self.myMove * (-1), self.layerNumber + 1, self)
                self.children.append(child)
            else:
                boardPositionTemp[i] = 1
                child = TicTacToe(boardPositionTemp, self.myMove * (-1), self.layerNumber + 1, self)
                self.children.append(child)

    def gainFunction(self):
        #find the cost of the possible combinations to win
        #we have to choose the maximum gain path
        #check row
        count = 0
        i = 0
        for p in range(0,3):
            if(self.boardPosition[i]!= -1*self.myMove and self.boardPosition[i+1]!= -1*self.myMove and self.boardPosition[i+2]!= -1*self.myMove):
                count +=1
            i += 3
        for i in range(0,3):
            if(self.boardPosition[i]!= -1*self.myMove and self.boardPosition[i+3]!= -1*self.myMove and self.boardPosition[i+6]!= -1*self.myMove):
                count +=1
        if(self.boardPosition[0]!= -1*self.myMove and self.boardPosition[4]!= -1*self.myMove and self.boardPosition[8]!= -1*self.myMove):
            count += 1
        if(self.boardPosition[2]!= -1*self.myMove and self.boardPosition[4]!= -1*self.myMove and self.boardPosition[6]!= -1*self.myMove):
            count += 1
        return count
        #check column
        #check diagonal

    def printMe(self):
        p = 0
        for i in self.boardPosition:
            if(p%3 == 0):
                print("\n")
                print("------------------")
            if(i == -1):
                print("  " + "X " + " | "),
            elif(i == 1):
                print("  " + "O " + " | "),
            else:
                print("  " + "  " + " | "),
            p += 1
        print("\n")
    
    def getMyCopy(self):
        return copy.deepcopy(self.boardPosition)

    def checkWin(self):
        flag = False
        i = 0
        for p in range(0,3):
            if(self.boardPosition[i] == self.boardPosition[i+1]== self.boardPosition[i+2] == self.myMove):
                flag = True
                break
            i += 3
        for i in range(0,3):
            if(self.boardPosition[i]== self.boardPosition[i+3]== self.boardPosition[i+6]== self.myMove):
                flag = True
                break
        if(self.boardPosition[0]==  self.boardPosition[4]== self.boardPosition[8]== self.myMove):
            flag = True
        if(self.boardPosition[2]== self.boardPosition[4]== self.boardPosition[6]== self.myMove):
            flag = True
        
        return flag

    def calcMyCost(self):
        cost = 0
        cost = cost + self.gainFunction()
        parentNode = self.parent
        while(parentNode != None):
            if(parentNode.myMove != self.myMove):
                cost = cost - parentNode.gainFunction()
            else:
                cost = cost + parentNode.gainFunction()
            parentNode = parentNode.parent
        return cost
