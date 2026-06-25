"""
XO Neural Net Series Revision IV
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
    def __init__(self, n_inputs: int, n_outputs: int, act: str) -> None:
        """Initializes a dense layer with given input and output sizes and activation function."""
        self.weights: xp.ndarray = xp.random.randn(n_inputs, n_outputs) * xp.sqrt(2.0 / n_inputs) # He Initialization for weights.
        self.bias = xp.zeros(n_outputs) # New bias array filled with zeros.
        self.act, self.d_act = ACTIVATIONS.get(act, "relu") # Default to ReLU
    
    def forward(self, input_arr: xp.ndarray) -> xp.ndarray:
        """Forward pass for the layer. Computes the output based on the input and current weights and biases."""
        self.input_arr = input_arr
        self.Z = input_arr @ self.weights + self.bias
        self.output = self.act(self.Z)
        return self.output
    
    def backward(self, dA: xp.ndarray, learning_rate: float) -> xp.ndarray:
        """Backward pass for the layer. Calculates gradients and updates weights and biases."""
        dZ = dA * self.d_act(self.Z)       # dA -> Output GOL. dZ -> Z GOL.
        X  = xp.atleast_2d(self.input_arr) # X  -> Ensures 2D shape for batch or single sample.
        dZ = xp.atleast_2d(dZ)             # dZ -> Ensures 2D shape for batch or single sample.
        dW = X.T @ dZ / X.shape[0]         # dW -> Weight GOL. Batch averaged. X.T @ dZm computes the sum of gradients for each weight across the batch, and dividing by X.shape[0] gives the average.
        dB = dZ.mean(axis=0)               # dB -> Bias   GOL, Batch averaged.
        dI: xp.ndarray = dZ @ self.weights.T # dI -> Input  GOL. For backpropagation to previous layers. 

        self.weights -= learning_rate * dW
        self.bias -= learning_rate * dB
        
        return dI.reshape(self.input_arr.shape)
    
class Sequential:
    def __init__(
        self, 
        input_neurons: int, 
        layer_count: int, 
        layer_neuron_count: int, 
        output_neurons: int,
        act_per_layer: list[str], 
        learning_rate: float
    ) -> None:
        
        self.input_neurons = input_neurons
        self.layer_count = layer_count
        self.output_neurons = output_neurons
        self.learning_rate = learning_rate
        self.layers: list[DenseLayer] = []
 
        prev_neuron_count = input_neurons
        
        for idx in range(layer_count):
            layer = DenseLayer(
                prev_neuron_count, 
                layer_neuron_count, 
                act_per_layer[idx]
            )
            self.layers.append(layer)
            prev_neuron_count = layer_neuron_count

        # Output layer
        self.layers.append(DenseLayer(prev_neuron_count, output_neurons, act_per_layer[-1]))
    
    def forward(self, input_arr: xp.ndarray) -> xp.ndarray:
        """Forward pass for the entire network."""
        
        x = input_arr
        for layer in self.layers:
            x = layer.forward(x)
        return x  
    
    def backward(self, out_target: xp.ndarray):
        """
        Backward pass for the entire network. Computes gradients and updates weights and biases based on the target output.

        Args
        ----
            out_target (np.ndarray): The expected output values for the given input, used to calculate the loss and update the network's parameters during backpropagation.
        Vars
        ----
            out_pred (np.ndarray): The predicted output values from the network's forward pass, used to calculate the loss and update the network's parameters during backpropagation.
        """
        out_pred: xp.ndarray = self.layers[-1].output
        batch_size = out_target.shape[0] if out_target.ndim > 1 else 1
        loss_gradient = (unicogni.softmax(out_pred) - out_target) / batch_size 
        
        for layer in reversed(self.layers):
            loss_gradient = layer.backward(loss_gradient, self.learning_rate)
    
    def train(self, x: xp.ndarray, y: xp.ndarray, epochs: int, batch_size: int) -> None:
        """Training loop for the network.
        
        Args:
            X (np.ndarray): Input data.
            y (np.ndarray): Target labels.
            epochs (int): Number of training epochs.
        """
        last_loss = float('inf')
        
        BATCHCOUNT = x.shape[0] // batch_size 
        
        for epoch in range(epochs):
            
            shuffle_indices = xp.random.permutation(x.shape[0])
            x = x[shuffle_indices]
            y = y[shuffle_indices]
            
            epoch_loss = 0.0
            
            for batches in range(0, x.shape[0], batch_size):
                X_batch = x[batches:batches+batch_size]
                y_batch = y[batches:batches+batch_size]
                
                self.forward(X_batch)
                self.backward(y_batch)
                
                epoch_loss += unicogni.cross_entropy_loss(y_batch, self.layers[-1].output)
                
            epoch_loss /= (x.shape[0] / BATCHCOUNT)
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss:.6f} {"\033[92m ### \033[0m" if epoch_loss < last_loss else "\033[91m ### \033[0m"}")
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