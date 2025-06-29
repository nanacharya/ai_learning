
import numpy as np

A= np.array ([[1,2], [3,4]])
print(A)

determinant= np.linalg.det(A)
print("determinant  ad - bc \n", determinant)

inverse = np.linalg.inv(A)
print("inverse  \n", inverse)

