import numpy as np # helps with the math

class Neural_Network(object):
    def __init__(self):
        #parameters
        self.inputSize = 9
        self.outputSize = 9
        self.hiddenSize = 17 #this size was determined by the general rule saying "If you have multiple output nodes or you believe that the required input–output relationship is complex, make the hidden-layer dimensionality equal to the input dimensionality plus the output dimensionality (but keep it less than twice the input dimensionality)"

        #weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # weight matrix from input to hidden layer
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # weight matrix from hidden to output layer

    def forward(self, inPut):
        #forward propagation through the network
        self.z = np.dot(inPut, self.W1) # dot product of X (input) and first set of weights
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of weights
        yHat = self.sigmoid(self.z3) # final activation function
        return yHat

    def sigmoid(self, s):
        # activation function
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, inPuts, actualOutput, predictedOutput):
        # backward propgate through the network
        self.o_error = actualOutput - predictedOutput # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(predictedOutput) # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += inPuts.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

    def train(self, inPut, actualOutput):
        #should only require inputs and then wait for the outcome before backpropagation runs
        predictedOutput = self.forward(inPut)
        self.backward(inPut, actualOutput, predictedOutput)

    def learn(self, inPut, outPut, outcome):
        # learns from the random game generator
        self.backward(inPut, outPut, outcome)

    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s")
        np.savetxt("w2.txt", self.W2, fmt="%s")
