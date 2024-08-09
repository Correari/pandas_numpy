import numpy as np
#Cero Dimenesiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
#Una dimension
Vector = np.array([1, 2, 3])
print(Vector)
print(Vector.ndim)
#Dos dimensiones
Matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(Matrix) #imprime la matriz
print(Matrix.ndim)
#Más de dos dimensiones
Tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(Tensor)
print(Tensor.ndim)
#Agregar o Eliminar Dimensiones
Vector = np.array([1, 2, 3], ndmin=10)
print(Vector)
print(Vector.ndim)
#Expandir
expand=np.expand_dims(np.array([1, 2, 3]), axis=0)
print(expand)
print(expand.ndim)
#Eliminar dimensiones que no se están usando
print(Vector, Vector.ndim) 
vector_2 = np.squeeze(Vector)
print(vector_2, vector_2.ndim)

 
