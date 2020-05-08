# start,stop = map(int,input("Enter start and stop number...start number can't 1 or 0: ").split())
# lis = [x for x in range(start, stop+1) if all(x % y != 0 for y in range(start, x))]
# print(lis)
def prime_num_sequence(start,stop):
    lis = []
    for i in range(start,stop):
        count = 0
        for j in range(start,i+1):
            if i%j==0:
                count+=1
        if count==2:
            #print(i,end=" ")
            lis.append(i)
    return lis

x = prime_num_sequence(2,15)
print(x)
