# Neural Networks in Pure Python

This project is a simple implementation of a neural network using **only Python and NumPy**. The goal is to understand the inner workings of a neural network by building it from scratch without using any deep learning libraries like PyTorch or TensorFlow.

---

## Project Goals

- To create a functional neural network using only Python and NumPy.
- To understand the core concepts of neural networks:
  - **Feedforward propagation**
  - **Weighted sums**
  - **Activation functions (e.g., Sigmoid)**
- To experiment with multi-neuron and multi-layer architectures.
- To provide a stepping stone for learning advanced concepts like backpropagation and training.

---

## Features

1. Single Neuron Implementation:
- Simulates the behavior of a single neuron with inputs, weights, and a bias.
- Applies the sigmoid activation function to calculate the output.

2. Multi-Neuron Layer:
- Adds support for multiple neurons in a single layer.
- Computes outputs for all neurons simultaneously.

3. Multi-Layer Network:
- Supports creating networks with multiple layers.
- Performs forward propagation across all layers.

4. Fully Customizable:
- You can modify the network's architecture by specifying the number of neurons in each layer.

---

## Dependencies

- Python 3.7+
- NumPy (for matrix operations)

To install NumPy, use:
`pip install numpy`

---

##Learning Objectives

By working with this project, you will:

- Learn how to manually implement the building blocks of a neural network.
- Develop an intuition for concepts like weighted sums, biases, and activation functions.
- Understand how forward propagation works in a neural network.
- Lay the groundwork for more advanced topics like backpropagation and gradient descent.

---

##Future Work

- Add support for different activation functions (ReLU, Tanh, etc.).
- Implement backpropagation for training the network.
- Add examples of training the network on simple datasets (e.g., XOR problem).
- Extend the network to support custom loss functions.
