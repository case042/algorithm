n = int(input())

for i in range(n):
    cnt = 0
    user_input = list(map(int, input().split()))
    scores_cnt,scores = user_input[0],user_input[1:]
    avg = sum(scores)/scores_cnt

    for score in scores:
        if score > avg:
            cnt += 1
    x = cnt/scores_cnt*100
    print("%0.3f"%x + "%")