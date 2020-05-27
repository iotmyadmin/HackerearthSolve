for _ in range(int(input())):
    s = input()
    for i in range(int(input())):
        L,R = map(int,input().split())
        count  = 0
        for j in range(L-1,R):
            if s[j] == s[j+1] == s[j+2]:
                count+=1
        print(count)
