result = []

for i in range(9):
    result.append(int(input()))

x = max(result)
for i in range(len(result)):
    if x == result[i]:
        print(x)
        print(i+1)
        break