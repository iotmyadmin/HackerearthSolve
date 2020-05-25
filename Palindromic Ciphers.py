for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        print("Palindrome")
    else:
        total = 1
        for c in s:
            num=ord(c)-96
            total = total*num
        print(total)
