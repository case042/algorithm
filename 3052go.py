arr = []
result = []
for i in range(10):
    x = int(input())
    arr.append(x)
    result.append(arr[i]%42)

result = list(set(result))

print(len(result))