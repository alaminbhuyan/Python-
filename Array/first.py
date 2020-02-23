from array import array
#from math import *
""" ['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
    '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'buffer_info', 'byteswap', 'count', 'extend', 'frombytes', 'fromfile', 'fromlist', 'fromstring', 'fromunicode', 'index', 'insert', 'itemsize', 'pop', 'remove', 'reverse', 'tobytes', 'tofile', 'tolist', 'tostring', 'tounicode', 'typecode'] """
#print(dir(array))
a= array('i',[1,2,3,4,5])
print(a)
a.append(6)
print(a)
a.insert(1,20)
print(a)
print('--------------------------')
b= array('i',[1,2,3,4,4,4,5])
total=b.count(4)
print(total)
pos = b.index(3)
print(pos)
b.extend([6,7,8,9,10])
print(b)
b.pop()
print(b)
b.remove(8)
print(b)
b.reverse()
print(b)
print('----------------------------------------')
c= array('i',[10,20,30,40,50])

for i in c:
    print(i,end=' ')
print('-----------------------------')
""" d= array('i',[])
size = int(input('Enter the size of array: '))
print('Enter the array elements: ')
for i in range(size):
    x = int(input())
    d.append(x)

print(f'The array is: {d}') """
print('--------------------------------')
e= array('i',[1,2,3,4,5])

size = len(e)
print(size)
#buffer_info return the address and size of an array
print(e.buffer_info())
#typecode return the type of the array
print(e.typecode)
print('------------------------')
#itemsize return the byte number
F = array('i',[1,2,3,4,5])
print(F.itemsize)
print('-------------------------------------')
#tolist convert the array into list
G = array('i',[1,2,3,4,5])
L= G.tolist()
print(L)
print(type(L))
print('-------------------------------------')
H= array('u',['a','l','a','m','i','n'])
#tostring convert the array into bytes
name = H.tostring()
print(name)
print('---------------------------')

I = array('i',[2,3,4,5])
I2 = array(I.typecode,(a*a for a in I))
print(I2)

i=0
while i<len(I2):
    print(I2[i])
    i=i+1
print('-----------------------')
J = array('i',[1,2,3,4,5])
Sum = sum(J)
print(Sum)
i=len(J)-1
while i>=0:
    print(J[i],end=' ')
    i=i-1
print()
print(J)
print('-----------------------------------')
arr=array('i',[10,20,30,40,50])
print(min(arr))
print(max(arr))
print('-----------------------------------')
arr = array('i', [20,40,10,30,50,5])
print(min(arr))
print(max(arr))
print('-----------------------------------')
arr2 = array('i', [10, 20, 30, 40, 50])
arr3 = array('i', [60,70,80])
arr4 = arr2+arr3
print(arr4)
print('------------------------------------')

print('Hello,I am alamin.')
