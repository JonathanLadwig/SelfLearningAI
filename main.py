import numpy as np # helps with the math
import random

def randLearn(epoch):
    # randomly generates moves to train the network
    inputs = [] * epoch  # an array made up of moveorder lists
    outputs = [] * epoch #an array made up , either win for X(1), win for O(-1) or draw(0)
    for i in range(epoch):
        print("New input array")
        over = False
        moveorder = [-1] * 9  # tracks the moves, stores tile number moved to and uses the index as the order. Even numbers are X, Odd numbers are O.
        movelist = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # all possible tiles at the start of the game
        counter = 0
        while not over:
            move = random.choice(movelist)  # makes a move to a random remaining tile
            print('Move to ', move)
            movelist.remove(move)  # removes tile from the list
            print('Possible moves:', movelist)
            moveorder[counter] = move  # adds that move to the list
            print('MoveOrder:', moveorder)
            counter = counter + 1  # adds 1 to the counter
            #over = gameOver(moveorder)  # checks to see if the game is over
            print("   ")
            if counter == 9:
                over = True
        inputs[i] = moveorder #adding the moveorder array to the inputs array
        #result = gameResult(moveorder)  # result is either win for X(1), win for O(-1) or draw(0)

def gameOver():
    pass


def gameResult():
    pass


class NeuralNet:

    #initialising the variables
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        #initialise weights
        self.weights = np.array([[.50], [.50], [.50]])
        self.error_history = []
        self.epoch_list = []

    def selfLearn(self, epoch):
        #plays against itself to train the network
        pass

randLearn(3)