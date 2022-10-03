from StacTacToe import StacTacToe

game = StacTacToe(3)
inputArrays = game.getInputs()
outputArrays = game.getOutputs()
for i in range(3):
    array2D = game.convertTo2DArray(inputArrays[i])
    game.printBoard(array2D)
    print("")

