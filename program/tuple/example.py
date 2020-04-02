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