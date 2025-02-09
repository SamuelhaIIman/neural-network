import numpy as np

def mysigmoid(x):
    return 1/(1+np.exp(-x))

class MultiLayerNetwork:
    def __init__(self, layer_sizes):
        self.weights = []
        self.biases = []

        for i in range(len(layer_sizes)-1):
            self.weights.append(np.random.rand(layer_sizes[i + 1], layer_sizes[i]))
            self.biases.append(np.random.rand(layer_sizes[i + 1], 1))

    def feedforward(self, inputs):
        activations = inputs
        for W, b in zip(self.weights, self.biases):
            z = np.dot(W, activations) + b
            activations = mysigmoid(z)
        return activations
    
layer_sizes = [3, 10, 5]

network = MultiLayerNetwork(layer_sizes)

x = np.array([[3], [4], [1]])

output = network.feedforward(x)
print("Network Output: ", output)
