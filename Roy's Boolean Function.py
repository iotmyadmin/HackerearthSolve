from math import gcd

def isPrime(n):
    if n==1:
        return False
    elif n<=3:
        return True
    else:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                return False
    return True

def royBool(n):
    z=0
    for i in range(n+1):
        if gcd(i,n)==1:
            z+=1
    return isPrime(z)
    
for _ in range(int(input())):
    n = int(input())
    if n==1:
        print("FALSE")
    elif royBool(n):
        print("TRUE")
    else:
        print("FALSE")
