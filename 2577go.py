a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

arr = []
numbers = list(map(str, [0,1,2,3,4,5,6,7,8,9]))

for number in numbers:
    cnt = 0
    for value in result:
        if number == value:
            cnt = cnt+1
    arr.append(cnt)

for data in arr:
    print(data)