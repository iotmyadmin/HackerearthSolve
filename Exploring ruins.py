s =  input()
n= len(s)
c=''
for i in range(n):
    if s[i]=='?':
        if i == 0:
            if n==1:
                c+='a'
            elif s[i+1]=='a':
                c+='b'
            else:
                c+='a'
        elif i==n-1:
            if s[i-1]=='a' or c[i-1]=='a':
                c+='b'
            else:
                c+='a'
        elif s[i-1]!='a' and s[i+1]!="a" and c[i-1]!='a':
            c+="a"
        else:
            c+="b"
    else:
        c+=s[i]
print(c)
