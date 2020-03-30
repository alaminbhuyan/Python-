
# lis = list(map(int,input().split()))
# print(lis)
# lis = list(int(i) for i in input().split())
# print(lis)

# com , val, pos = input().split(' ')
# print(com,val,pos)
# a,b,c = map(int,input().split())
# print(a,b,c)

lis = [1,2,3,4,5,6,7,8]
lis2 = [x*2 for x in lis if x%2==0]
print(lis2)

l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
l2 = [y for x in l for y in x]
print(l2)

l3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
l4 = [z for x in l3 for y in x for z in y]
print(l4)

l5 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#print(len(l5))
l6 =[[row[i] for row in l5] for i in range(3)]
print(l6)