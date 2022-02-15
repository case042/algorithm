n = int(input())
number = input()
arr = []

for v in number:
    arr.append(v)

arr2 = list(map(int, arr))

print(sum(arr2))
