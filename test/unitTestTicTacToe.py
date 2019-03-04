## @package unitTestTicTacToe
# Documentation for this module
#
# This is the unit test script for the TicTacToe game software

import unittest
from TicTacToeClass import TicTacToe

## Documentation for class

class TestTicTacToeGameFunctions(unittest.TestCase):

    ## Documentation for a function
    def test_constructor(self):
        boardPosition = [0,0,0,0,0,0,0,0,0]
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.boardPosition,boardPosition)
        self.assertEqual(testObject.myMove,move)
        self.assertEqual(testObject.layerNumber,layerNumber)
        self.assertEqual(testObject.parent,None)

    ## Documentation for a function
    def test_finding_zero_positions(self):
        boardPosition = [0,1,0,1,1,0,1,0,0]
        desiredZeroPosition = [0,2,5,7,8]
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.findEmptyPosition(),desiredZeroPosition)
        
    ## Documentation for a function
    def test_deep_copy_function(self):
        boardPosition = [0,1,0,-1,1,0,-1,0,0]
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.getMyCopy(), boardPosition)

    ## Documentation for a function
    def test_branch_creation(self):
        boardPosition = [0,1,0,-1,1,0,-1,0,0]
        #Number of branches(children) created should be equal to the number of empty spaces which is zeros
        desiredNumberOfChildren = 5
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        testObject.extractNode()
        numberOfChildren = len(testObject.children)
        self.assertEqual(numberOfChildren, desiredNumberOfChildren)

    ## Documentation for a function
    def test_objects_parent(self):
        boardPosition = [0,1,0,-1,1,0,-1,0,0]
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        testObject.extractNode()
        self.assertEqual(testObject.children[0].parent, testObject)

    ## Documentation for a function
    def test_gain_function(self):
        boardPosition = [0,0,0,0,1,0,0,0,0]
        #Gain function determines the possible ways the player can win which is 8 for this case
        # as all the possible cases are open for a player to win at this point
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.gainFunction(), 8)
        boardPosition = [0,1,0,-1,1,0,-1,0,0]
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.gainFunction(), 4)

    ## Documentation for a function
    def test_check_total_nodeCost(self):
        boardPosition = [0,0,0,0,1,0,0,0,0]
        #All moves are possible so we will get max cost of 8 
        #This calculates the sum of gain functions of the path(from the current node to its root node)
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertEqual(testObject.calcMyCost(), 8)
    
    ## Documentation for a function
    def test_winning_condition(self):
        boardPosition = [0,1,0,-1,1,0,-1,0,0]
        #Win condition is determined is three move of same kind are in a row, colum or diagonal
        move = 1
        layerNumber = 1
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertFalse(testObject.checkWin())
        boardPosition = [1,1,1,-1,1,0,0,-1,0]
        testObject = TicTacToe(boardPosition, move, layerNumber)
        self.assertTrue(testObject.checkWin())

if __name__ == '__main__':
    unittest.main()
