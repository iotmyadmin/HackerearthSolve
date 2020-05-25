for _ in range(int(input())):
    n,m = map(int,input().split())
    if n == m :
        print("YES")
    elif n/m == m/n :
        print("YES")
    else:
        print("NO")
