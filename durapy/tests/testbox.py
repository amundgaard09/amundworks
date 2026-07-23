"""DuraPy Testbox I"""
from src.unimath.linalg import Matrix, Vector # type: ignore
import numpy as np

print("START")

vec1 = Vector(components=[1, 2, 3])
print("\nvec1")
print(vec1)

vec2 = np.array([1, 2, 3])
print("\nvec2")
print(vec2)

mat1 = Matrix(array=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nmat1")
print(mat1)

mat2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nmat2")
print(mat2)

matvec1 = mat1 @ vec1
print("\nmatvec1")
print(matvec1)

matvec2 = mat2 @ vec2
print("\nmatvec2")
print(matvec2)

matmat1 = mat1 @ mat1
print("\nmatmat1")
print(matmat1)

matmat2 = mat2 @ mat2
print("\nmatmat2")
print(matmat2)

vecvec1 = vec1 * vec1
print("\nvecvec1")
print(vecvec1)

vecvec2 = vec2 @ vec2
print("\nvecvec2")
print(vecvec2)

# VecMat multiplication needs to define if it is row- or column-based

vecmat1 = vec1 @ mat1
print("\nvecmat1")
print(vecmat1)

vecmat2 = vec2 @ mat2
print("\nvecmat2")
print(vecmat2)

print("END")
