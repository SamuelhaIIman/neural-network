import numpy as np

def sigmoidZeroToOneNumber(x):
    return 1/(1+np.exp(-x)) # This makes the input numbers from neurons into 0-1 decimal number

sigmoidZeroToOneNumber(6.7)

class MyNeuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs) + self.bias
        return sigmoidZeroToOneNumber(total)
    
weights = np.array([[0.5,0.8], [0.1, 0.3]])
biases = np.array([2, -1])
neurons = MyNeuron(weights,biases)

x = np.array([3,4]) # Neuron weights
outputs = neurons.feedforward(x)
print(outputs)
