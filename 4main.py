# Miscellaneous Things
# Load Data from file
import numpy as np

# get all the text number as an array and turn in into a float
# delimiter is what slits the data
filedata = np.genfromtxt('data.txt', delimiter=',')
# print(filedata)

# turn it into integers
filedata = filedata.astype('int32')
# print(filedata)

# Boolean Masking and Advanced Indexing
# where in file data the value is greater than 50 output is false and true
# print(filedata>50)

# where in file data the value is greater then 50 outputs the numbers
# print(filedata[filedata > 50])

# you can index with a list in numpy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a[[1, 2, 8]])

# check the columns for one element that is greater than 50
# print(np.any(filedata>50, axis=0))

# check if all columns are greater than 50
# print(np.all(filedata>50, axis=0))

# check the rows
# print(np.all(filedata>50, axis=1))

# greater than 50 but less than 100
# print((filedata > 50) & (filedata < 100))

# not greater than 50 and less than 100
# print(~(filedata > 50) & (filedata < 100))

'''
Solution for the last activity
a[2:4, 0:2]
a[[0,1,2,3],[1,2,3,4]]
a[[0,4,5],3]
'''

arr = np.arange(1, 31)  # 1 to 30 (31 is exclusive)
# print(arr)

matrix = arr.reshape(5, 6)  # Reshape into 5 rows and 6 columns
# print(matrix)

# indexing using slicing
'''1:3 selects rows 1 and 2.

3:5 selects columns 4 and 5.'''
submatrix = matrix[1:3, 3:5]
print(submatrix)

# indexing 11, 12, 16, 17
# Access 11 (Row 1, Column 4)
# print(matrix[1, 4])  # Output: 11

# Access 12 (Row 1, Column 5)
# print(matrix[1, 5])  # Output: 12

# Access 16 (Row 2, Column 3)
# print(matrix[2, 3])  # Output: 16

# Access 17 (Row 2, Column 4)
# print(matrix[2, 4])  # Output: 17