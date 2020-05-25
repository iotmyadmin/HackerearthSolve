for _ in range(int(input())):
    n,m = map(int,input().split())
    arr= list(map(int,input().split()))+list(map(int,input().split()))
    arr.sort(reverse= True)
    for element in arr:
        print(element,end=" ")
    print()
