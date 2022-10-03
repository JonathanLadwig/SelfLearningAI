import numpy as np # helps with the math
import random

class StacTacToe:

    inputs = []
    outputs = []

    def __init__(self, epoch):
        self.randLearn(epoch)
        self.inputs = self.inputs
        self.outputs = self.outputs

    def getInputs(self):
        return self.inputs

    def getOutputs(self):
        return self.outputs

    def randLearn(self, epoch):
        # randomly generates moves to train the network
        #inputs = [] * epoch  # an array made up of moveorder lists
        #outputs = [] * epoch  # an array made up , either win for X(1), win for O(-1) or draw(0)
        for i in range(epoch):
            # print("New input array")
            over = False
            moveorder = [
                            -1] * 9  # tracks the moves, stores tile number moved to and uses the index as the order. Even numbers are X, Odd numbers are O.
            movelist = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # all possible tiles at the start of the game
            counter = 0
            while not over:
                move = random.choice(movelist)  # makes a move to a random remaining tile
                # print('Move to ', move)
                movelist.remove(move)  # removes tile from the list
                # print('Possible moves:', movelist)
                moveorder[counter] = move  # adds that move to the list
                # print('MoveOrder:', moveorder)
                counter = counter + 1  # adds 1 to the counter
                over = self.gameOver(moveorder)  # checks to see if the game is over
                # print("   ")
                if counter == 9:
                    over = True
            self.inputs.append(moveorder)  # adding the moveorder array to the inputs array
            self.outputs.append(self.gameResult(moveorder))  # adds the result to the list of results

    def gameOver(self, moveOrder):
        # Was this piece of code unnecessary? A bit, but it makes it easier for others to understand
        over = False
        if self.gameResult(moveOrder) != 2:
            over = True
        return over

    def gameResult(self, moveOrder):
        winner = 2  # -1 means O won, 1 mean s X won, 0 is a draw, 2 is undecided
        array2D = self.convertTo2DArray(moveOrder)
        # checks rows
        for x in range(3):
            if array2D[x][0] != 0:
                token = array2D[x][0]
            else:
                break
            if array2D[x][1] == token and array2D[x][2] == token:
                winner = token
        # checks columns
        for y in range(3):
            if array2D[0][y] != 0:
                token = array2D[0][y]
            else:
                break
            if array2D[1][y] == token and array2D[2][y] == token:
                winner = token
        # checks diagonal right
        if array2D[0][0] != 0:
            token = array2D[0][0]
            if array2D[1][1] == token and array2D[2][2] == token:
                winner = token
        # checks diagonal left
        if array2D[0][2] != 0:
            token = array2D[0][2]
            if array2D[1][1] == token and array2D[2][0] == token:
                winner = token
        if winner == 2 and moveOrder[8] != -1:
            winner = 0
        return winner

    def convertTo2DArray(self, inputArray):
        array2D = [[0 for x in range(3)] for y in range(3)]

        for i in range(9):
            if inputArray[i] != -1:
                column = int(inputArray[i] % 3)
                row = int((inputArray[i] - column) / 3)
                if i % 2 == 0:
                    array2D[row][column] = 1
                else:
                    array2D[row][column] = -1
            else:
                break

        return array2D

    def printBoard(self, array2D):
        linePrint = ""
        for y in range(3):
            for x in range(3):
                if array2D[x][y] == 0:
                    linePrint += "[ ]"
                elif array2D[x][y] == 1:
                    linePrint += "[X]"
                elif array2D[x][y] == -1:
                    linePrint += "[O]"
            print(linePrint)
            linePrint = ""