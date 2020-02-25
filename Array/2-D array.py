from numpy import *
# input from use for 1-D array in numpy
""" size = int(input('Enter the size of array: '))
#arr = ones(size,int)
arr = zeros(size,int)
print('Enter the elements of array: ')
for i in range(len(arr)):
    x = int(input())
    arr[i]=x
print(arr) """
# input from use for 2-D array in numpy
row = int(input('Enter the number of row: '))
col = int(input('Enter the number of column: '))
arr = zeros((row,col),int)
#row_len = len(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        x = int(input())
        arr[i][j] = x
print(arr)