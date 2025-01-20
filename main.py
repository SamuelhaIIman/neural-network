import numpy as np

def mysigmoid(x):
    return 1/(1+np.exp(-x))

mysigmoid(6.7)

class MyNeuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs) + self.bias
        return mysigmoid(total)
    
weights = np.array([0.5,0.8])
bias = 2
nueron = MyNeuron(weights,bias)

x = np.array([3,4])
print(nueron.feedforward(x))
