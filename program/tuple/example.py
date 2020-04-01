# from collections import Counter
# lis= [2 ,3 ,4 ,5 ,6 ,8 ,7 ,6 ,5 ,18]
# b=Counter(lis)
# print(b)
#
# m = [[6,1],[6,1],[6,2]]
# print(*m)
# sum = 0
# for i in m:
#     for j in i:
#         if j == b.keys():
#             sum = sum+j[1]
# print(sum
from collections import Counter

num_of_shoes = int(input())
shoes_size = Counter(map(int, input().split()))
num_of_customer = int(input())

income = 0

for i in range(num_of_customer):
    size, price = map(int, input().split())
    if shoes_size[size]:
        income += price
        shoes_size[size] -= 1

print (income)