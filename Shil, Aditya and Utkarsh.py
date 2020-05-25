n = int(input())
count = 0
for i in range(1,n):
    for j in range(3,n+1):
        for k in range(1,n):
            if i<j and j>k and i != k:
                count+=1
print(count)
