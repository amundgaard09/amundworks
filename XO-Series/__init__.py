
# Older models are specified by their generation and architecture, Newest by their model name
from .src.XO_I import NeuralNetwork as XOI_MLP
from .src.XO_II import NeuralNetwork as XOII_MLP
from .src.XO_III import NeuralNetwork as XOIII_MLP
from .src.XO_IV import SequentialMLP as SequentialMLP
#from .src.XO_V

__all__ = [
    "XOI_MLP",
    "XOII_MLP",
    "XOIII_MLP",
    "SequentialMLP",
]
