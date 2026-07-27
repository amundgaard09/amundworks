"""The first iteration of the Durendal XO Neural Network series."""

import math
import random
import time
from collections.abc import Callable

from durapy import unicogni


def dot(a: list, b: list) -> float:
    """Returns the dot product of two lists of the same length."""

    if len(a) != len(b):
        raise ValueError("Lists must be of the same length")

    return sum(x * y for x, y in zip(a, b))


def sigmoid(x: float) -> float:
    """Sigmoid activation function."""
    return 1 / (1 + math.exp(-x))


def d_sigmoid(x: float) -> float:
    """Derivative of the sigmoid function."""
    return sigmoid(x) * (1 - sigmoid(x))


class Neuron:
    """_Neuron class for individual neurons in the network, containing weights, bias, activation function, and methods for forward and backward passes._"""

    def __init__(
        self,
        n_in: int,
        act: Callable[[float], float],
        dact: Callable[[float], float],
    ):
        """Neuron Initialization with random weights and bias."""
        self.weights = [random.uniform(-1, 1) for _ in range(n_in)]
        self.bias = random.uniform(-1, 1)
        self.act = act
        self.dact = dact

    def forward(self, input: list) -> float:
        """Forward pass for the neuron."""
        self.input = input
        self.Z = dot(input, self.weights) + self.bias
        self.out = self.act(self.Z)
        return self.out

    def backward(self, dLoss_dOut: float, learning_rate: float):
        """_Backward pass for the neuron._
        Args:
            dLoss_dOut (float): The Gradient of Loss with respects to the output of this neuron
            LearningRate (float): The Learning Rate (aka rate of change) in the weights and biases of the neuron.
            Delta (float):
        """
        delta = dLoss_dOut * self.dact(self.Z)

        for idx in range(len(self.weights)):
            self.weights[idx] -= learning_rate * delta * self.input[idx]

        self.bias -= learning_rate * delta
        return [delta * weight for weight in self.weights]


class Layer:
    """_Layer class for NN Layers, containing multiple neurons and handling forward and backward passes for the layer._"""

    def __init__(
        self,
        n_in,
        n_neurons,
        act: Callable[[float], float],
        dact: Callable[[float], float],
    ):
        self.act, self.dact = act, dact
        self.neurons = [Neuron(n_in, act, dact) for _ in range(n_neurons)]

    def forward(self, input: list[float]) -> list[float]:
        """_Forward pass for the layer._

        Args:
            Input (list[float]): A vectorlist of input values to the layer, comprised of individual outputs from neurons of the previous layer.

        Returns:
            Output (list[float]): A vectorlist of output values from the layer, comprised of individual outputs from neurons of the current layer.
        """
        out = []
        for node in self.neurons:
            out.append(node.forward(input))
        return out

    def backward(self, gol: list[float], learning_rate: float) -> list[float]:
        """_Backward Pass for Layers_
        Args:
            dLoss_dOutList (list): The Gradient of Loss with respects to each output of the neurons in this layer.
            LearningRate (float): The Learning Rate (aka rate of change) in the weights and biases of the neuron.
        Returns:
            dLoss_dInput (list): The Gradient of Loss with respects to input for the next layer backwards.
        """
        dLoss_dInput = [0.0] * len(self.neurons[0].input)

        for neuron, dLoss_dOut in zip(self.neurons, gol):
            grads = neuron.backward(dLoss_dOut, learning_rate)

            for idx, grad in enumerate(grads):
                dLoss_dInput[idx] += grad

        return dLoss_dInput


class NeuralNetwork:
    def __init__(
        self,
        n_neurons_in: int,
        n_layers: int,
        n_layer_neurons: int,
        n_neurons_out: int,
        acts: list[Callable[[float], float]],
        dacts: list[Callable[[float], float]],
        learning_rate: float,
    ):

        self.n_in = n_neurons_in
        self.n_layers = n_layers
        self.n_out = n_neurons_out
        self.learning_rate = learning_rate

        self.layers: list[Layer] = []

        # Hidden layers
        n_prev_neurons = n_neurons_in
        for idx in range(n_layers):
            layer = Layer(
                n_prev_neurons,
                n_layer_neurons,
                acts[idx],
                dacts[idx],
            )
            self.layers.append(layer)
            n_prev_neurons = n_layer_neurons

        # Output layer
        self.layers.append(
            Layer(
                n_prev_neurons,
                n_neurons_out,
                acts[-1],
                dacts[-1],
            )
        )

    def forward(self, Input: list[float]) -> list[float]:
        """
        Forward pass for the entire network.

        Args:
            Input (list[float]): A vectorlist of input values to the network, comprised of individual input values for each input neuron.

        Returns:
            Output (list[float]): A vectorlist of output values from the network, comprised of individual output values from each output neuron.
        """
        x = Input
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, target_out: list[float]):
        out_layer = self.layers[-1]
        dLoss_dOut = []

        for neuron, target in zip(out_layer.neurons, target_out):
            dLoss_dOut.append(neuron.out - target)

        for layer in reversed(self.layers):
            dLoss_dOut = layer.backward(dLoss_dOut, self.learning_rate)


# XOR
X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
Y = [0.0, 1.0, 1.0, 0.0]

XORnet = NeuralNetwork(
    n_neurons_in=2,
    n_layers=1,
    n_layer_neurons=8,
    n_neurons_out=1,
    acts=[sigmoid, sigmoid],
    dacts=[d_sigmoid, d_sigmoid],
    learning_rate=0.01,
)

while True:
    try:
        n_epochs = int(input("Epoch Count: "))
        break

    except ValueError:
        print("Invalid Variables!")
        continue

start_time = time.time()

for epoch in range(n_epochs):
    total_loss = 0

    for x_i, y_i in zip(X, Y):
        out = XORnet.forward(x_i)[0]

        loss = unicogni.mse(out, y_i)
        total_loss += loss

        XORnet.backward([y_i])

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Loss = {total_loss / 4}")

end_time = time.time()
elapsed = end_time - start_time

print("\nPredicted XOR outputs after training:")

correct_preds, preds = 0, 0

for x_i, y_i in zip(X, Y):
    raw_output = XORnet.forward(x_i)[0]
    predicted = 1 if raw_output > 0.5 else 0

    print(f"Input: {x_i}, Predicted: {predicted}, Actual: {y_i}, Raw: {raw_output:.4f}")

    preds += 1

    if predicted == y_i:
        correct_preds += 1

print(f"\nTotal Training Time: {elapsed:.2f} seconds")
print(f"Time per Epoch: {elapsed / epoch:.4f} seconds")

if correct_preds == preds:
    print("\033[92m -- Successful Training! -- \033[0m")

else:
    print("\033[91m -- Unsuccessful Training -- \033[0m")
