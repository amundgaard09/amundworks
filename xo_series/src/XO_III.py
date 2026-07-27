"""
Third Iteration - XO Neural Net Series

Matrix-Based MNIST Classification Neural Net
"""

import time

import keras
import numpy as np

from durapy import unicogni

ACTIVATIONS = {
    "relu": (lambda Z: np.maximum(0, Z), lambda Z: (Z > 0).astype(float)),
    "linear": (lambda Z: Z, lambda Z: np.ones_like(Z)),
    "sigmoid": (unicogni.sigmoid, unicogni.d_sigmoid),
    "softmax": (
        unicogni.softmax,
        None,
    ),  # Softmax derivative is handled differently in backpropagation, so we set it to None here.
}


class DenseLayer:
    def __init__(self, n_in: int, n_out: int, act: str):
        """Initializes a dense layer with given input and output sizes and activation function."""
        self.weight: np.ndarray = np.random.randn(n_in, n_out) * np.sqrt(
            2.0 / n_in
        )  # He Initialization for weights.
        self.bias: np.ndarray = np.zeros(n_out)  # New bias array filled with zeros.
        self.act, self.dact = ACTIVATIONS[act]

    def Forward(self, in_arr: np.ndarray) -> np.ndarray:
        """Forward pass for the layer. Computes the output based on the input and current weights and biases."""
        self.in_arr = in_arr
        self.Z = (
            in_arr @ self.weight + self.bias
        )  # Z ->      Post transformation - Pre activation.
        self.out = self.act(self.Z)
        return self.out

    ### GOL / dX > Gradient of Loss. ### Reshaping > "Verification" of array dimensions ### .T > Transposing ###
    def Backward(self, dA: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass for the layer. Calculates gradients and updates weights and biases."""
        dZ: np.ndarray = dA * self.dact(self.Z)  # type: ignore | double declaration of dZ
        X: np.ndarray = (
            self.in_arr if self.in_arr.ndim > 1 else self.in_arr.reshape(1, -1)
        )  # X  -> Reshaped input.
        dZ: np.ndarray = dZ if dZ.ndim > 1 else dZ.reshape(1, -1)  # dZ -> Reshaped dZ.
        dW: np.ndarray = (
            X.T @ dZ / X.shape[0]
        )  # dW -> Weight GOL. Batch averaged. X.T @ dZm computes the sum of gradients for each weight across the batch, and dividing by X.shape[0] gives the average.
        dB: np.ndarray = dZ.mean(axis=0)  # dB -> Bias   GOL, Batch averaged.
        dI: np.ndarray = (
            dZ @ self.weight.T
        )  # dI -> Input  GOL. For backpropagation to previous layers.

        self.weight -= learning_rate * dW
        self.bias -= learning_rate * dB

        return dI.reshape(self.in_arr.shape)


class NeuralNetwork:
    def __init__(
        self,
        n_in: int,
        n_layers: int,
        n_layer_neuronDotProducts: int,
        n_out: int,
        acts: list[str],
        learning_rate: float,
    ):

        self.n_in = n_in
        self.n_layers = n_layers
        self.n_out = n_out
        self.learning_rate = learning_rate
        self.layers: list[DenseLayer] = []

        prev_n_neurons = n_in

        for idx in range(n_layers):
            layer = DenseLayer(prev_n_neurons, n_layer_neurons, acts[idx])
            self.layers.append(layer)
            prev_n_neurons = n_layer_neurons

        # Output layer
        self.layers.append(DenseLayer(prev_n_neurons, n_out, acts[-1]))

    def Forward(self, input_arr: np.ndarray) -> np.ndarray:
        """_Forward pass for the entire network._

        Args:
            Input (list[float]): An array of input values to the network, where each value corresponds to the input of an input neuron.

        Returns:
            Output (list[float]): An array of output values from the network, where each value corresponds to the output of an output neuron.
        """
        x = input_arr
        for layer in self.layers:
            x = layer.Forward(x)
        return x

    def Backward(self, out_target: np.ndarray):
        """
        Backward pass for the entire network. Computes gradients and updates weights and biases based on the target output.

        Args:
            TargetOutput (np.ndarray): The expected output values for the given input, used to calculate the loss and update the network's parameters during backpropagation.
            OutputPrediction (np.ndarray): The predicted output values from the network's forward pass, used to calculate the loss and update the network's parameters during backpropagation.
        """
        out_pred: np.ndarray = self.layers[-1].out
        batch_size = out_target.shape[0] if out_target.ndim > 1 else 1
        initial_GOL = (unicogni.softmax(out_pred) - out_target) / batch_size

        for layer in reversed(self.layers):
            initial_GOL = layer.Backward(initial_GOL, self.learning_rate)

    def Train(self, X: np.ndarray, y: np.ndarray, epochs: int):
        """Training loop for the network.

        Args:
            X (np.ndarray): Input data.
            y (np.ndarray): Target labels.
            epochs (int): Number of training epochs.
        """
        lastloss = float("inf")

        BATCHCOUNT = X.shape[0] // BATCHSIZE

        for epoch in range(epochs):
            shuffle_indices = np.random.permutation(X.shape[0])
            X = X[shuffle_indices]
            y = y[shuffle_indices]

            epochloss = 0.0

            for batches in range(0, X.shape[0], BATCHSIZE):
                X_batch = X[batches : batches + BATCHSIZE]
                y_batch = y[batches : batches + BATCHSIZE]

                self.Forward(X_batch)
                self.Backward(y_batch)

                epochloss += unicogni.cross_entropy_loss(y_batch, self.layers[-1].out)

            epochloss /= X.shape[0] / BATCHCOUNT

            marker = (
                "\033[92m ### \033[0m"
                if epochloss < lastloss
                else "\033[91m ### \033[0m"
            )
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {epochloss:.6f} {marker}")
            lastloss = epochloss

    def Predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions on new data.

        Args:
            X (np.ndarray): Input data.

        Returns:
            np.ndarray: Predictions.
        """
        return self.Forward(X)

    @staticmethod
    def NormalizeData(X: np.ndarray) -> np.ndarray:
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        std = np.where(std == 0, 1, std)
        return (X - mean) / std


MNISTNET = NeuralNetwork(
    n_in=784,
    n_layers=2,
    n_layer_neurons=256,
    n_out=10,
    acts=["relu", "relu", "linear"],
    learning_rate=0.1,
)

#### -- DATA PREPROCESSING -- ####

# data set
((x_train, y_train), (x_test, y_test)) = keras.datasets.mnist.load_data()

x_train, y_train, x_test, y_test = (
    np.array(x_train),
    np.array(y_train),
    np.array(x_test),
    np.array(y_test),
)

# reshaping and normalizing
x_train = np.reshape(x_train, (x_train.shape[0], -1))
x_test = np.reshape(x_test, (x_test.shape[0], -1))
x_train = x_train / 255.0
x_test = x_test / 255.0

# one-hot encoding of labels
train_labels = np.zeros((y_train.size, y_train.max() + 1))
test_labels = np.zeros((y_test.size, y_test.max() + 1))

train_rows = np.arange(y_train.size)
test_rows = np.arange(y_test.size)

train_labels[train_rows, y_train] = 1
test_labels[test_rows, y_test] = 1

X = x_train
Y = train_labels

#### -- TRAINING LOOP -- ####

epochs = 200
start_time = time.time()

BATCHSIZE = 128
MNISTNET.Train(X, Y, epochs=epochs)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"\nTotal Training Time: {elapsed_time:.2f} seconds")
print(f"Time per Epoch: {elapsed_time / epochs:.4f} seconds")

correct_preds = np.zeros(10, dtype=int)

raw_preds = MNISTNET.Predict(x_test)
preds = np.argmax(raw_preds, axis=1)
test_label_idxs = np.argmax(test_labels, axis=1)

bool_arr = test_label_idxs == preds

correct_precentage = np.sum(bool_arr) / len(bool_arr) * 100
correct_preds = np.bincount(test_label_idxs[bool_arr], minlength=10)

for digit in range(10):
    print(
        f"Digit {digit}: {correct_preds[digit]}/{np.sum(test_labels[:, digit])} correct"
    )

print(f"\nOverall Accuracy: {correct_precentage:.2f}%")
