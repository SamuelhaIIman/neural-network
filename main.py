import numpy as np

def mysigmoid(x):
    return 1/(1+np.exp(-x)) # This makes the input numbers from nuerons into 0-1 decimal number

mysigmoid(6.7)

class MyNeuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs) + self.bias
        return mysigmoid(total)
    
weights = np.array([[0.5,0.8], [0.1, 0.3]])
biases = np.array([2, -1])
nuerons = MyNeuron(weights,biases)

x = np.array([3,4]) # Nueron weights
outputs = nuerons.feedforward(x)
print(outputs)
