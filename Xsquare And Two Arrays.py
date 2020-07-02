n,q = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for _ in range(q):
    arr,l,r = map(int,input().split())
    res=0
    if arr == 1:
        res+=sum(a[l-1:r:2])
        res+=sum(b[l:r:2])
    else:
        res+=sum(b[l-1:r:2])
        res+=sum(a[l:r:2])
        
    print(res)
