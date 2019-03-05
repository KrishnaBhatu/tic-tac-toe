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
# @file    TicTacToeGameLogic.py
# @author  Krishna Bhatu
# @version 1.0
# @brief TicTacToe game implementation
#
# @section DESCRIPTION
#
# Code for Game Logic with user interraction

from TicTacToeClass import TicTacToe
import random

## Function for saving the computer from loosing(checking if the player has a chance of winning in the next move and countering it with filling that position)
# @param boardPosition The current positions of all the moves played
# @param theirMove The player which is -1 for X and 1 for
# @result zeroPosition The position to fill in to avoid the computer from loosing(it is -1 if there is no loosing condition)
def checkWinningCondition(boardPosition, theirMove):
    i = 0
    zeroPosition = -1
    for p in range(0,3):
        if(boardPosition[i] == theirMove and boardPosition[i+1]== theirMove and boardPosition[i+2] == 0):
            zeroPosition = i+2
        elif(boardPosition[i] == theirMove and boardPosition[i+2]== theirMove and boardPosition[i+1] == 0):
            zeroPosition = i+1
        elif(boardPosition[i+2] == theirMove and boardPosition[i+1]== theirMove and boardPosition[i] == 0):
            zeroPosition = i
        i += 3
        
    for i in range(0,3):
        if(boardPosition[i] == theirMove and boardPosition[i+3]== theirMove and boardPosition[i+6]== 0):
            zeroPosition = i+6
        elif(boardPosition[i] == theirMove and boardPosition[i+6]== theirMove and boardPosition[i+3]== 0):
            zeroPosition = i+3
        elif(boardPosition[i+6] == theirMove and boardPosition[i+3]== theirMove and boardPosition[i]== 0):
            zeroPosition = i
            
    if(boardPosition[0]==theirMove and boardPosition[4]==theirMove and boardPosition[8] == 0):
        zeroPosition = 8
    elif(boardPosition[0]==theirMove and boardPosition[8]==theirMove and boardPosition[4] == 0):
        zeroPosition = 4
    elif(boardPosition[8]==theirMove and boardPosition[4]==theirMove and boardPosition[0] == 0):
        zeroPosition = 0
            
    if(boardPosition[2]== theirMove and boardPosition[4]== theirMove and boardPosition[6] == 0):
        zeroPosition = 6
    elif(boardPosition[2]== theirMove and boardPosition[6]== theirMove and boardPosition[4] == 0):
        zeroPosition = 4
    elif(boardPosition[6]== theirMove and boardPosition[4]== theirMove and boardPosition[2] == 0):
        zeroPosition = 2

    return zeroPosition

#Code implementing game logic and human interracton
start = raw_input("Do you want to start first say Y or N! \n")
print("What is your Notation X or O? \n")
opponentNotation = input("Enter -1 for X and 1 for O:\n")
print("Enter the Position in this format!\n")
p = -1
for i in range(0,9):
    if(i%3 == 0):
        p += 1
        print("\n")
        print("------------------")
    if(i%3 == 0):
        print("  " + str(3*p) + "  | "),
    elif((i-1)%3 == 0):
        print("  " + str(3*p+1) + "  | "),
    else:
        print("  " + str(3*p+2) + "  | "),
print("\n")
yourMove = opponentNotation
computerMove = opponentNotation * (-1)
boardPosition = [0,0,0,0,0,0,0,0,0] #Initialize the board position to all empty(0)
if(start == 'Y' or start == 'y'):
    parent = None
    currentLayer = 1
    currentOpponentPlacement = input("What's your move?")
    boardPosition[currentOpponentPlacement] = yourMove 
    currentMove = TicTacToe(boardPosition, yourMove, currentLayer, parent)
    print(currentMove.printMe())
    nodeToSearch = []
    nodesSearched = []
    nodeToSearch.append(currentMove)
    tempFlag = True
    turnsPlayed = 1

    #Loop until all the moves are exhausted or if there is a winner
    while(tempFlag):
        #Check if all the positions are exhausted
        if(len(nodeToSearch[0].findEmptyPosition()) == 0):
            tempFlag = False
            break
        stopWin = checkWinningCondition(nodeToSearch[0].boardPosition, yourMove) #Check winning condition of player
        myWinChance = checkWinningCondition(nodeToSearch[0].boardPosition, computerMove) #Check winning condition of computer
        #Check if there is no winning chance for both player and computer
        if(stopWin == -1 and myWinChance == -1):
            #p is the current layer number
            #q is the number of future steps to search for best possible step using cost function
            p = nodeToSearch[0].layerNumber
            if(nodeToSearch[0].layerNumber < 6):
                q= 4 
            elif(nodeToSearch[0].layerNumber >= 6):
                q = 9 - nodeToSearch[0].layerNumber
            
            while(nodeToSearch[0].layerNumber != p + q ):
                nodeToSearch[0].extractNode()
                for i in nodeToSearch[0].children:
                    nodeToSearch.append(i)
                nodesSearched.append(nodeToSearch[0])
                del nodeToSearch[0]

            maxNodeGain = -64 #Set the maximum gain to the minimum value it can take which is -64
            del nodesSearched[0]
            
            #Calculate the best move selecting the higest cost node
            for i in nodesSearched:
                if(i.layerNumber == (p + q-1)):
                    if(i.calcMyCost() > maxNodeGain):
                        maxNodeGain = i.calcMyCost()
                        maxNode = i
            

            print("This is my move!!\n")
            while(maxNode.layerNumber != (p+1)):
                maxNode = maxNode.parent
            maxNode.printMe()
            if(maxNode.checkWin()):
                print("I am the winner")
                break

            print("Your turn now! \n")
            emptyPositions = maxNode.findEmptyPosition()
            currentOpponentPlacement = input("What's your move?")
            #Check if the user has not entered any invalid input
            while((currentOpponentPlacement not in emptyPositions) or (8 < currentOpponentPlacement < 0)):
                print("Invalid Position\n")
                currentOpponentPlacement = input("What's your move?")
            
            boardPosition = maxNode.getMyCopy()
            boardPosition[currentOpponentPlacement] = yourMove

        elif(myWinChance != -1):
            print("This is my move!!\n")
            boardPosition = nodeToSearch[0].getMyCopy()
            boardPosition[myWinChance] = computerMove
            currentMove = TicTacToe(boardPosition, computerMove, 1)
            currentMove.printMe()
            print("I am the winner!")
            break

        elif(stopWin != -1):
            print("This is my move!!\n")
            boardPosition = nodeToSearch[0].getMyCopy()
            boardPosition[stopWin] = computerMove
            currentMove = TicTacToe(boardPosition, computerMove, 1)
            currentMove.printMe()
            if(currentMove.checkWin()):
                print("I am the winner")
                break

            print("Your turn now! \n")
            emptyPositions = currentMove.findEmptyPosition()
            currentOpponentPlacement = input("What's your move?")
            while((currentOpponentPlacement not in emptyPositions) or (8 < currentOpponentPlacement < 0)):
                print("Invalid Position!\n")
                currentOpponentPlacement = input("What's your move?")
            boardPosition = currentMove.getMyCopy()
            boardPosition[currentOpponentPlacement] = yourMove
        
        turnsPlayed += 2 #Update the number if turns played

        currentMove = TicTacToe(boardPosition, yourMove, turnsPlayed, parent)
        currentMove.printMe()
        if(currentMove.checkWin()):
            print("You are the new Master!")
            break
        del nodeToSearch[:]
        del nodesSearched[:]
        nodeToSearch.append(currentMove)
        
elif(start == 'N' or start == 'n'):
    parent = None
    currentLayer = 1
    currentOpponentPlacement = random.randint(0,8)
    boardPosition[currentOpponentPlacement] = computerMove 
    currentMove = TicTacToe(boardPosition, computerMove, currentLayer, parent)
    print("This is My Move!")
    currentMove.printMe()
    currentLayer += 1
    boardPosition = currentMove.getMyCopy()
    emptyPositions = currentMove.findEmptyPosition()
    currentOpponentPlacement = input("What's your move?")
    #Check if the user has not entered any invalid input    
    while((currentOpponentPlacement not in emptyPositions) or (8 < currentOpponentPlacement < 0)):
            print("Invalid Position\n")
            currentOpponentPlacement = input("What's your move?")
    boardPosition[currentOpponentPlacement] =  yourMove
    currentMove = TicTacToe(boardPosition, yourMove, currentLayer, parent)
    nodeToSearch = []
    nodesSearched = []
    nodeToSearch.append(currentMove)
    tempFlag = True
    turnsPlayed = 2

    #Loop until all the moves are exhausted or if there is a winner
    while(tempFlag):
        #Check if all the positions are exhausted
        if(len(nodeToSearch[0].findEmptyPosition()) == 1):
            tempFlag = False
            break
        stopWin = checkWinningCondition(nodeToSearch[0].boardPosition, yourMove)
        myWinChance = checkWinningCondition(nodeToSearch[0].boardPosition, computerMove)
        #Check if there is no winning chance for both player and computer
        if(stopWin == -1 and myWinChance == -1):
            #p is the current layer number
            #q is the number of future steps to search for best possible step using cost function
            p = nodeToSearch[0].layerNumber
            if(nodeToSearch[0].layerNumber < 6):
                q= 4 
            elif(nodeToSearch[0].layerNumber >= 6):
                q = 9 - nodeToSearch[0].layerNumber
            nodeToSearch[0].printMe()

            while(nodeToSearch[0].layerNumber != p + q ):
                nodeToSearch[0].extractNode()
                for i in nodeToSearch[0].children:
                    nodeToSearch.append(i)
                nodesSearched.append(nodeToSearch[0])
                del nodeToSearch[0]
            maxNodeGain = -64
            del nodesSearched[0]

            #Calculate the best move selecting the higest cost node
            for i in nodesSearched:
                if(i.layerNumber == (p + q-1)):
                    if(i.calcMyCost() > maxNodeGain):
                        maxNodeGain = i.calcMyCost()
                        maxNode = i
            
            print("This is my move!!\n")
            while(maxNode.layerNumber != (p+1)):
                maxNode = maxNode.parent
            maxNode.printMe()
            if(maxNode.checkWin()):
                print("I am the winner")
                break

            print("Your turn now! \n")
            emptyPositions = maxNode.findEmptyPosition()
            currentOpponentPlacement = input("What's your move?")
            #Check if the user has not entered any invalid input
            while((currentOpponentPlacement not in emptyPositions) or (8 < currentOpponentPlacement < 0)):
                print("Invalid Position\n")
                currentOpponentPlacement = input("What's your move?")
            boardPosition = maxNode.getMyCopy()
            boardPosition[currentOpponentPlacement] = yourMove

        elif(myWinChance != -1):
            print("This is my move!!\n")
            boardPosition = nodeToSearch[0].getMyCopy()
            boardPosition[myWinChance] = computerMove
            currentMove = TicTacToe(boardPosition, computerMove, 1)
            currentMove.printMe()
            print("I am the winner!")
            break

        elif(stopWin != -1):
            print("This is my move!!\n")
            boardPosition = nodeToSearch[0].getMyCopy()
            boardPosition[stopWin] = computerMove
            currentMove = TicTacToe(boardPosition, computerMove, 1)
            currentMove.printMe()
            if(currentMove.checkWin()):
                print("I am the winner")
                break

            print("Your turn now! \n")
            emptyPositions = currentMove.findEmptyPosition()
            currentOpponentPlacement = input("What's your move?")
            while((currentOpponentPlacement not in emptyPositions) or (8 < currentOpponentPlacement < 0)):
                print("Invalid Position!\n")
                currentOpponentPlacement = input("What's your move?")
            boardPosition = currentMove.getMyCopy()
            boardPosition[currentOpponentPlacement] = yourMove
        
        turnsPlayed += 2 #Update the number if turns played
        currentMove = TicTacToe(boardPosition, yourMove, turnsPlayed, parent)
        currentMove.printMe()
        if(currentMove.checkWin()):
            print("You are the new Master!")
            break
        del nodeToSearch[:]
        del nodesSearched[:]
        nodeToSearch.append(currentMove)
        
    
print("\nWell Played\n")
if(tempFlag == False):
    print("It's a Draw")
