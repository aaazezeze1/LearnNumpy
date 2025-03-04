# Reorganizing Arrays
import numpy as np

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)

# check the shape of before which is 2 by 4
# print(before.shape)

# make it 8 by 2
# after = before.reshape((8, 1))
# print(after)

# make it 4 by 2
# after = before.reshape((4, 2))
# print(after)

# reshape it to 2 by 2 by 2
# after = before.reshape((2, 2, 2))
# print(after)

# Vertical Stacks - vertically stacking vectors or matrices
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

# stack both in the same matrix
# print(np.vstack([v1, v2]))

# 2 copies of v1 and v2
# print(np.vstack([v1, v2, v1, v2]))

# 3 copies of v2
# print(np.vstack([v1, v2, v2, v2]))

# horizontal stacks
h1 = np.ones((2, 4))
h2= np.zeros((2, 2))

# print(h1)
# print(h2)

# put h2 at the back of h1
print(np.hstack([h1, h2]))