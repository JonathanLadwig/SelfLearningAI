import numpy as np # helps with the math

class NeuralNet:

    #initialising the variables
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        #initialise weights
        self.weights = np.array([])
        self.error_history = []
        self.epoch_list = []

    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    def learn(self, epoch):
        for epoch in range(epoch):
            # generate random learning set
            self.feed_forward()
            # learn from the learning set
            self.backpropagation()
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    def selfLearn(self, epoch):
        #plays against itself to train the network
        pass