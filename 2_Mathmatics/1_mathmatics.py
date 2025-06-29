import numpy as np

A = np.array([[1, 2, 3],[4, 5, 6]]);
B = np.array([[10, 11, 12],[13, 14, 15]]);

print("Addition \n", A+B)
print("Subtraction \n", B-A)

C = 2* A
print("Scalar Multiplication \n", C)

D = np.array([[1,2], [3,4]])
E = np.array([[5,6], [7,8]])

result = np.dot(D, E)
print("Matrix Multiplication \n", result)


# Identity Matix
I = np.eye(5)
print("Identy Matrix  \n", I)

Z = np.zeros([10, 10])
print("Zero Matrix  \n", Z)

D = np.diag([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Diagonal Matrix  \n", D)


