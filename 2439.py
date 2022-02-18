n = int(input())
for i in range(n):
    for j in range(n):
        key = (n-j)-1
        if i >= key:
            print("*",end="")
        
        else:
            print(" ",end="")
    print()

