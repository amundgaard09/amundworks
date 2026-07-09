"""
XO Neural Net Series Revision IV
 
Optimization ideas for MLPs (brief):
 - Weight initialization (He/Xavier) to improve convergence.
 - Activation functions: use ReLU/LeakyReLU, avoid saturating activations where possible.
 - Batch normalization to stabilize and accelerate training.
 - Dropout to reduce overfitting.
 - Learning rate schedules (step, exponential, cosine) or adaptive optimizers (Adam, RMSprop, Adagrad).
 - Gradient clipping to avoid exploding gradients.
 - Mini-batch training and shuffling for stable gradients.
 - Early stopping based on validation loss to prevent overfitting.
 - L1/L2 regularization on weights to reduce overfitting.
 - Use vectorized (batch) operations and avoid Python loops for speed.
 - Use mixed precision and GPU acceleration when available.
 - Use momentum or Nesterov accelerated gradient for faster convergence.
 - Hyperparameter search (grid/random/Bayesian) to find optimal architecture and training hyperparams.
 - Use softmax with cross-entropy combined derivative for numerical stability.
 - Reduce model size (pruning, quantization) for deployment efficiency.
"""

USE_GPU = False

if USE_GPU:
    import cupy as xp # type: ignore 
else:
    import numpy as xp # cross platform 

from durapy import unicogni

ACTIVATIONS = {
    "relu":    (lambda Z: xp.maximum(0, Z), lambda Z: (Z > 0).astype(float)),
    "linear":  (lambda Z: Z,                lambda Z: xp.ones_like(Z)),
    "sigmoid": (unicogni.sigmoid,           unicogni.d_sigmoid),
    "softmax": (unicogni.softmax,           None) # Softmax derivative is handled differently in backpropagation, so we set it to None here.
}

class DenseLayer:
    def __init__(
        self,
        n_inputs: int,
        n_outputs: int,
        act: str,
        weight_decay: float = 0.0,
        dropout_rate: float = 0.0
    ) -> None:
        """Initializes a dense layer with given input and output sizes and activation function."""
        self.weights: xp.ndarray = xp.random.randn(n_inputs, n_outputs) * xp.sqrt(2.0 / n_inputs)  # He Initialization for weights.
        self.bias = xp.zeros(n_outputs)  # New bias array filled with zeros.
        self.act, self.dact = ACTIVATIONS.get(act, ACTIVATIONS["relu"])  # Default to ReLU
        self.weight_decay = weight_decay
        self.dropout_rate = dropout_rate
        self.dropout_mask = None
    
    def forward(self, input_arr: xp.ndarray, training: bool = False) -> xp.ndarray:
        """Forward pass for the layer. Computes the output based on the input and current weights and biases."""
        self.input_arr = input_arr
        self.Z = input_arr @ self.weights + self.bias
        self.output = self.act(self.Z)

        if training and self.dropout_rate > 0.0:
            self.dropout_mask = xp.random.rand(*self.output.shape) > self.dropout_rate
            self.output *= self.dropout_mask
            self.output /= (1.0 - self.dropout_rate)

        return self.output
    
    def backward(self, dA: xp.ndarray, learning_rate: float) -> xp.ndarray:
        """Backward pass for the layer. Calculates gradients and updates weights and biases."""
        if self.dropout_rate > 0.0 and self.dropout_mask is not None:
            dA = dA * self.dropout_mask
            dA /= (1.0 - self.dropout_rate)

        if self.dact is None:
            dZ = dA
            
        else:
            dZ = dA * self.dact(self.Z)
            
        X  = xp.atleast_2d(self.input_arr) # X  -> Ensures 2D shape for batch or single sample.
        dZ = xp.atleast_2d(dZ)             # dZ -> Ensures 2D shape for batch or single sample.
        dW = X.T @ dZ / X.shape[0]         # dW -> Weight GOL. Batch averaged.
        dB = dZ.mean(axis=0)               # dB -> Bias   GOL, Batch averaged.
        dI: xp.ndarray = dZ @ self.weights.T # dI -> Input  GOL. For backpropagation to previous layers. 

        if self.weight_decay > 0.0:
            dW += self.weight_decay * self.weights

        self.weights -= learning_rate * dW
        self.bias -= learning_rate * dB
        
        return dI.reshape(self.input_arr.shape)
    
class Sequential:
    def __init__(
        self,
        neurons_in: int,
        neurons_out: int,
        layer_count: int,
        layer_neurons: int,
        layer_acts: list[str],
        learning_rate: float = 0.01,
        weight_decay: float = 0.0,
        dropout_rate: float = 0.0,
        lr_decay: float = 0.0,
    ) -> None:
        """Sequential model constructor. Initializes a feedforward neural network with the specified architecture and hyperparameters."""
        
        self.input_neurons = neurons_in
        self.layer_count = layer_count
        self.output_neurons = neurons_out
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.dropout_rate = dropout_rate
        self.lr_decay = lr_decay
        self.layers: list[DenseLayer] = []
 
        prev_neuron_count = neurons_in
        
        for idx in range(layer_count):
            layer = DenseLayer(
                prev_neuron_count,
                layer_neurons,
                layer_acts[idx],
                weight_decay=self.weight_decay,
                dropout_rate=self.dropout_rate
            )
            self.layers.append(layer)
            prev_neuron_count = layer_neurons

        # Output layer
        self.layers.append(
            DenseLayer(prev_neuron_count, neurons_out, layer_acts[-1], weight_decay=self.weight_decay)
        )
    
    def forward(self, input_arr: xp.ndarray, training: bool = False) -> xp.ndarray:
        """Forward pass for the entire network."""
        x = input_arr
        for layer in self.layers:
            x = layer.forward(x, training=training)
        return x  

    def backward(self, out_target: xp.ndarray, learning_rate: float = 0.01):
        """
        Backward pass for the entire network. Computes gradients and updates weights and biases based on the target output.

        Args
        ----
            out_target (np.ndarray): The expected output values for the given input, used to calculate the loss and update the network's parameters during backpropagation.
        Vars
        ----
            out_pred (np.ndarray): The predicted output values from the network's forward pass, used to calculate the loss and update the network's parameters during backpropagation.
        """
        
        # Get last layer's output and compute the loss gradient
        out_pred: xp.ndarray = self.layers[-1].output
        batch_size = out_target.shape[0] if out_target.ndim > 1 else 1

        # Compute the loss gradient based on the output layer's activation function
        if self.layers[-1].dact is None:
            loss_gradient = (out_pred - out_target) / batch_size
        else:
            loss_gradient = (unicogni.softmax(out_pred) - out_target) / batch_size
        
        # Backpropagate through the layers in reverse order
        for layer in reversed(self.layers):
            loss_gradient = layer.backward(loss_gradient, learning_rate)
            
    def _get_learning_rate(self, epoch: int) -> float:
        """Compute current learning rate using a simple decay schedule."""
        if self.lr_decay <= 0.0:
            return self.learning_rate
        return self.learning_rate / (1.0 + self.lr_decay * epoch)
    
    def train(self, x: xp.ndarray, y: xp.ndarray, epochs: int, batch_size: int) -> None:
        """Training loop for the network.
        
        Args:
            X (np.ndarray): Input data.
            y (np.ndarray): Target labels.
            epochs (int): Number of training epochs.
        """
        
        # Initialize last_loss to infinity for tracking improvement
        last_loss = float('inf')
        
        # Calculate the number of batches based on the batch size and input data size
        BATCHCOUNT = max(1, (x.shape[0] + batch_size - 1) // batch_size)
        
        for epoch in range(epochs):
            learning_rate = self._get_learning_rate(epoch)
            random_idxs = xp.random.permutation(x.shape[0])
            x = x[random_idxs]
            y = y[random_idxs]
            
            epoch_loss = 0.0
            
            # Iterate over batches of data
            for batch_start in range(0, x.shape[0], batch_size):
                X_batch = x[batch_start:batch_start + batch_size]
                y_batch = y[batch_start:batch_start + batch_size]
                
                self.forward(X_batch, training=True)
                self.backward(y_batch, learning_rate)
                
                epoch_loss += unicogni.cross_entropy_loss(y_batch, self.layers[-1].output)
                
            epoch_loss /= BATCHCOUNT
            
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss:.6f} "f"{'\033[92m ### \033[0m' if epoch_loss < last_loss else '\033[91m ### \033[0m'}")
            
            last_loss = epoch_loss     

    def predict(self, x: xp.ndarray) -> xp.ndarray:
        """Make predictions on new data.
        
        Args:
            X (np.ndarray): Input data.
        
        Returns:
            np.ndarray: Predictions.
        """
        return self.forward(x) 
    
    @staticmethod
    def normalize_data(x: xp.ndarray) -> xp.ndarray:
        mean = xp.mean(x, axis=0)
        std  = xp.std(x, axis=0)
        std  = xp.where(std == 0, 1, std)
        return (x - mean) / std