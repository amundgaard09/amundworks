
# Older models are specified by their generation, Newest by their model name
from .src.XO_I import NeuralNetwork as XOI_NeuralNet
from .src.XO_II import NeuralNetwork as XOII_NeuralNet
from .src.XO_III import NeuralNetwork as XOIII_NeuralNet
from .src.XO_IV import Sequential as Sequential
#from .src.XO_V

__all__ = [
    "XOI_NeuralNet",
    "XOII_NeuralNet",
    "XOIII_NeuralNet",
    "Sequential",
]
