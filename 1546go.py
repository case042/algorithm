n = int(input())

w = list(map(int, input().split()))

w.sort()

result = []
for i in range(len(w)):
    result.append(w[i]/w[-1]*100)

print(sum(result)/len(result))