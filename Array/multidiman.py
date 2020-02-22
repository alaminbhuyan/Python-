from numpy import *

a = array([1,2,3,4,5])
print(a)
print(type(a))
a2 = array([1,2,3,4,5])

a3= a+a2
print(a3)
print(type(a3))
print('-------------------------------------------')
arr = array([1,2,3,4.5,5])
print(arr.dtype)
print(arr)
print('--------------------------------')
A= linspace(0,15,16)
print(A)
print('---------------------------------')
B = arange(0,10,2)
print(B)
C= zeros(5,int)
print(C)
D=ones(5,int)
print(D)