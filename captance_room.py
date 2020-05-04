#
# n , lis = int(input()), list(map(int,input().split()))
#
# for i in lis:
#     x = lis.count(i)
#     if x == 1:
#         print(i)
k = int(input())
L = str(input()).split(" ")
print(L)
family = L
print("family",family)
total = set(L)
print("total: ",total)
for r in set(L):
    try:
        family.remove(r)
    except:
        pass
print("again family",family)
print ("".join((total - set(family))))