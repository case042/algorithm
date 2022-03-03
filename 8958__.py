n = int(input())
ox_data = []
for i in range(n):
    ox_data.append(input())

for score in ox_data:
    x_split = score.split("X")
    result = 0
    for data in x_split:
        cnt = data.count("O")
        answer = 0
        for i in range(1,cnt+1):
            answer += i
        result += answer

    print(result)