import numpy as np

# Be careful when copying arrays
# a = np.array([1, 2, 3])

# copy function copies the array and makes sure that a values is still the same
# after using b to print and change element to 100
# b = a.copy()
# b[0] = 100
# print(b)
# print(a)

# Mathematics
# a = np.array([1, 2, 3, 4])
# print(a)

# add 2 to each number in a
# print(a+2)

# subtract numbers in a
# print(a-2)

# multiply numbers in a
# print(a*2)

# divide numbers in a
# print(a/2)

# b = np.array([1, 0, 1, 0])

# add elements of a to b
# print(a+b)

# a raise to the power of 2
# print(a ** 2)

# sin, cos and tan
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))

# Linear Algebra

# create a 2 by 3 matrix of ones
a = np.ones((2,3))
# print(a)

# create a 3 row 2 column matrix
b = np.full((3, 2), 2)
# print(b)

# multiply the matrices of a and b together using matmul
# output will be a 2x2 matrix with 6 inside
# print(np.matmul(a, b))

# create a 3 by 3 identity matrix
'''
An identity matrix is a square matrix where:
All the elements on the main diagonal are 1.
All the elements off the main diagonal are 0.

c looks like this:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

 np.linalg.det(c) computes the determinant of the matrix c.
An identity matrix is a special square matrix that acts as the multiplicative identity in linear algebra.
When you multiply any matrix by the identity matrix, the result is the original matrix.
The determinant is a scalar value that can be computed for a square matrix.

It provides important information about the matrix, such as:
Whether the matrix is invertible (a matrix is invertible if its determinant is not zero).
The scaling factor of the linear transformation represented by the matrix.
'''

# find the determinant
c = np.identity(3)
# print(np.linalg.det(c))

# Statistics with numpy

stats = np.array([[1,2,3],[4,5,6]])
# print(stats)

# take the min number
# print(np.min(stats))

# take the max number
# print(np.max(stats))

# take the minimum number based on the row
# give the min of the first and second row of arrays which is 1 and 4
# print(np.min(stats, axis=1))

# get all the min values of all the rows which outputs 1, 2, 3
# print(np.min(stats, axis=0))

# get the biggest value on the arrays which is 3 and 6
# print(np.max(stats, axis=1))

# get the sum of all the elements in the array
print(np.sum(stats))

# add up all the terms going downwards or in the column which is 5, 7, 9
'''because 
[1, 2, 3]
 +  +  +
[4, 5, 6]

then add it together to get 5, 7, 9
'''
print(np.sum(stats, axis=0))
