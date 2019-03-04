import numpy as np
import copy

class TicTacToe:

    def __init__(self, boardPosition, move, layerNumber, parent = None):
        self.boardPosition = boardPosition
        self.parent = parent
        self.myMove = move
        self.layerNumber = layerNumber
        
    def findEmptyPosition(self):
        return 0

    def extractNode(self):
        self.children = []

    def gainFunction(self):
        return 0
            
    def getMyCopy(self):
        stubList = [0,0,0,0,0,0,0,0,0]
        return stubList

    def checkWin(self):
        return False

    def calcMyCost(self):
        return 0
