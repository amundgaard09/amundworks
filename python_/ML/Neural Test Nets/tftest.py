
import math

# --- Initialisering --

INPUTVECTORS = [[0,0], 
     [0,1], 
     [1,0], 
     [1,1]] # Input data for XOR-problemet

GOAL = [0, 1, 1, 0] # Målverdier for XOR-problemet

eta = float(input("Læringsrate (eta): "))

HiddenInputWeights = [[0.5, 0.5], [0.5, 0.5]]  # 2x2 matrise for input til hidden layer
HiddenBias = [0.5, 0.5]  # Bias for hidden layer
HiddenOutputWeights = [[0.5], [0.5]]  # 2x1 matrise for hidden til output layer
OutputBias = [0.5]  # Bias for output layer
 
def FloatDot(a, b) -> float:
    return sum(x * y for x, y in zip(a, b))

def VectorDot(a, b) -> float:
    return sum(x * y for x, y in zip(a, b))
    
def DerivativeActivation(x, function: str) -> float:
    if function == "sigmoid":
        s = 1 / (1 + math.exp(-x))
        return s * (1 - s)
    elif function == "relu":
        return 1 if x > 0 else 0

def Activation(x, function: str) -> float:
    if function == "sigmoid":
        return 1 / (1 + math.exp(-x))
    elif function == "relu":
        return max(0, x)

# --- Læringssyklus (epoker) ---
for epoch in range(1000):  # Antall epoker
    for x_i, y_i in zip(INPUTVECTORS, GOAL):
        
        print(x_i)
        
        # --- Forward pass ---
        HiddenInputs = Dot(x_i, HiddenInputWeights) + HiddenBias # x_i er input, HiddenInputWeights er vektene, HiddenBias er bias for hidden layer
        HiddenOutput = Activation(HiddenInputs, function="sigmoid") # Aktiveringsfunksjon for hidden layer

        OutputInput = Dot(HiddenOutput, HiddenOutputWeights) + OutputBias
        OutputPrediction = Activation(OutputInput, function="sigmoid")

        # --- Loss / feil ---
        Error = OutputPrediction - y_i

        # --- Backward pass ---
        # Output-lag gradient
        GradientOutput = Error * DerivativeActivation(OutputInput, function="sigmoid")

        # Hidden-lag gradient
        HiddenGradient = [GradientOutput * HiddenOutputWeights[i][0] * DerivativeActivation(HiddenInputs[i], "sigmoid") for i in range(len(HiddenInputs))]
        
        # --- Oppdater weights ---
        HiddenOutputWeights -= eta * FloatDot(HiddenOutput, GradientOutput)
        OutputBias[0] -= eta * GradientOutput

        for i in range(len(HiddenInputWeights)):
            for j in range(len(HiddenInputWeights[0])):
                HiddenInputWeights[i][j] -= eta * x_i[j] * HiddenGradient[i]
        
        HiddenBias -= eta * HiddenGradient