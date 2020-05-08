
num = input("Enter a number: ")
print("True") if sum(pow(int(i),len(num)) for i in num) == int(num) else print("False")

