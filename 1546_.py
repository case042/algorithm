n = int(input())

scores = list(map(int, input().split()))

scores.sort()

result = []
for i in range(len(scores)):
    result.append(scores[i]/scores[-1]*100)

final = 0
for i in result:
    final += i

print(final/len(result))