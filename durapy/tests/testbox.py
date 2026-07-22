print("START")

from src.unimath.linalg import Matrix, NDVector # type: ignore

print("IMPORT OK")

vec = NDVector(components=[1, 2, 3])
print("VECTOR CREATED")
print(vec)

mat = Matrix(array=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("MATRIX CREATED")
print(mat)

print("STARTING CALCULATION")
res = mat @ vec
print("CALCULATION OK")

print(res)

print("END")
