from numpy import *

arr1 = array([1,2,3,4])
arr2 = array([5,6,7,8])
print(concatenate([arr1,arr2]))

a3 = arr1.copy()
print(a3)
print(type(a3))
print('----------------------------')
# Multidimantional array

A = array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(A)
# dtype return the data type
print(A.dtype)
# ndim return the dimantion
print(A.ndim)
# shape return the row and column number
print(A.shape)
# flatten convert the multidimantion array into one dimantion
B = A.flatten()
print(B)
print(B.ndim)
print(B.shape)
print('--------------------------------')

C = array([
    [1,2,3,4,5,6],[3,2,6,8,7,9]
])

D = C.flatten()
# reshape convert the one dimantion array into multidimantion

E = D.reshape(3,4)
print(E)

F = D.reshape(2,2,3)
print(F)

print('-----------------------------')
# convert 2-D array into matrices
G = array([
    [1,2,3,4,5,6],[3,2,6,8,7,9]
])

mat = matrix(G)
print(mat)
print('--------------------------')

m = matrix('1 2 3;4 5 6;7 8 9')
print(m)
print('Diagonal elements is: ')
print(diagonal(m))
print(m.min())
print(m.max())
print('----------------------------')
# multiplication two matrix
m1 = matrix('1 2 3;4 5 6;7 8 9')
m2 = matrix('1 4 3;8 5 6;10 8 9')

m3 = m1*m2
print(m3)
print(diagonal(m3))
