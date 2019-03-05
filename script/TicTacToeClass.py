## License
# BSD 3-Clause License
# @copyright (c) 2018, Krishna Bhatu
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# @file    TicTacToeClass.py
# @author  Krishna Bhatu
# @version 1.0
# @brief TicTacToe class implementation
#
# @section DESCRIPTION
#
#  python implementation for TicTacToe class which describes a node of possible game board position

## @package TicTacToeClass
# Documentation for TicTacToe Class
# This class defines a node which is a particular tic-tac-toe board setting

import numpy as np
import copy

## TicTacToe Class
class TicTacToe:

    ## Class Constructor
    # This method initializes the board positions for the node along with other node parameters
    # @param self Object pointer
    # @param boardPosition The current positions of all the moves played
    # @param move The move of the current node which is -1 for X and 1 for O
    # @param layerNumber The position of the node which is the number of moves played before the node arrived
    # @param parent The node object from which the current node is derived
    def __init__(self, boardPosition, move, layerNumber, parent = None):

        self.boardPosition = boardPosition
        self.parent = parent
        self.myMove = move
        self.layerNumber = layerNumber
        self.children = [] #List of all derived nodes
        if(parent == None):
            self.myCost = 0
        else:
            self.myCost = self.calcMyCost()

    ## Method to find the empty positions on the tic-tac-toe board
    # @param self Object pointer
    # @return emptyPositionList A list of location of empty positions
    def findEmptyPosition(self):
        emptyPositionList = []
        for i in range(0, len(self.boardPosition)):
            if(self.boardPosition[i] == 0):
                emptyPositionList.append(i)

        return emptyPositionList

    ## Method to expand the branches of the node (Deriving all the possible next moves)
    # @param self Object pointer
    # @return None
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

    ## Method to find the maximum possible ways for winning for the particular node
    # @param self Object Pointer
    # @return count The number of possible victory ways (Max = 8)
    def gainFunction(self):
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

    ## Method to print the boardPosition of the node
    # @param self Object Pointer
    # @return None
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

    ## Method to get the deep copy of the boardPOsition 
    # @param self
    # @return Deepcopy of boardPosition
    def getMyCopy(self):
        return copy.deepcopy(self.boardPosition)

    ## Method to check if the current node has a winning configuration
    # @param self Object pointer
    # @return flag Flag is a boolean which is Ture if the node has a winning configuration
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

    ## Method to calculate the total cost to reach the node
    # @param self Object pointer
    # @return cost The integer cost that requires to reach the node from the root node(We maximize the cost to win)
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
