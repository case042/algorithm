arr = []

while True:
    a,b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    arr.append(a+b)

for data in range(len(arr)):
    print(arr[data])