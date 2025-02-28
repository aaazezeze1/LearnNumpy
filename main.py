import numpy as np

# one dimensional array
# a = np.array([1, 2, 3], dtype='int16')
# a = np.array([1, 2, 3], dtype='int32')
# print(a)
# print()

# 2d array of floats
# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)
# print()

# get the dimension of the array https://youtu.be/QUT1VHiLmmI?si=phtSnpKYK5VQqKdM&t=788
# print(a.ndim)
# print(b.ndim)
# print()

# Get Shape (show rows and columns of the array)
# print(a.shape)
# print(b.shape)

# Get Type and Size of the Array
# print()
# int 16 or 32
# print(a.dtype)

# 4 bytes and 8 bytes
# print(a.itemsize)
# print(b.itemsize)
# print()

# Total Size
# print(a.size)

# print number of bytes
# print(a.nbytes)

# or do print(a.size * a.itemsize)
# print(a.size * a.itemsize)

# 2 by 7 array
a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
# print(a.shape)

# Get a specific element [row index, column index]
# print(a[1, 5])
# print(a[1, -2])

# Get everything in the row
# print(a[0, :])

# Get a specific column
# print(a[:, 2])

# using [start index:end index: step element]
# prints 2, 4, 6
# print(a[0, 1:6:2])
# print(a[0, 1:-1:2])

# Modify element on the list
# a[1, 5] = 20
# print(a)

# print all but replace the 3, 10 ccolumn because of index 2
# a[:, 2] = 5
# print(a)

# change it into two different numbers
# a[:, 2] = [1, 2]
# print(a)

# 3D array example
# this array has a shape of 2 blocks, 2 rows, 2 elements
# first dimension = 1, 2, 3, 4
# second dimension = 5, 6, 7, 8
b = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
# print(b)

# Get specific element from 3D array
# print(b[0, 1, 1])

# Replace element in 3D array
# print 3, 4, 7, 8
# select all blocks:select the second row in each block: select all elements in the selected rows
# row1 = b[:, 1, :]  
# row2 = b[:, 3, :]  

# Concatenate and flatten the result (convert 2D array into 1D)
# result = np.concatenate([row1, row2]).flatten()
# print(result)

'''The array b has three levels of nesting: The outermost level: [[[1, 2], [3, 4], [5, 6], [7, 8]]]
This is a single block (or "matrix") containing 4 rows. The middle level: [[1, 2], [3, 4], [5, 6], [7, 8]]
Each of these is a row in the block. The innermost level: [1, 2], [3, 4], etc. Each of these is a row element (or "column").
Step 2: Determine the Shape To find the shape of b, we count the number of elements along each dimension:
Outermost dimension (blocks): There is 1 block in b. So, the size of this dimension is 1.
Middle dimension (rows): Each block has 4 rows. So, the size of this dimension is 4.
Innermost dimension (columns): Each row has 2 elements. So, the size of this dimension is 2.
Thus, the shape of b is (1, 4, 2).'''

# Replace rows 1 and 3 with [[9, 9], [8, 8]]
# 9,9,8,8 have a shape of 1,2,2 
b[:, [1, 3], :] = [[[9, 9], [8, 8]]]
print(b)
print("Shape of b:", b.shape)

# Initialize different types of arrays