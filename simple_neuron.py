import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 1.11],
          [-1, 2.0, 1.5, 2.7],
          [-0.8, 1, 1.4, -1.3]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
layer2.forward(layer1.output)

print(layer2.output)
