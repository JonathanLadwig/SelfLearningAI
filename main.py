from StacTacToe import StacTacToe
import numpy as np # helps with the math

epoch = 100000
firstMove = [0]*9
secondMove = np.zeros((9,9))
game = StacTacToe(epoch)
inputArrays = game.getInputs()
outputArrays = game.getOutputs()
for i in range(epoch):
    inputs = inputArrays[i]
    if outputArrays[i] == 1:
        firstMove[inputs[0]] += 1
        secondMove[inputs[0]][inputs[1]] -= 1
    elif outputArrays[i] == -1:
        firstMove[inputs[0]] -= 1
        secondMove[inputs[0]][inputs[1]] += 1

print("First Move Array: ", firstMove)
print("Second Move Array: ")
print(secondMove)
