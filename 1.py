# def add_four_numbers(a,b,c,d):
#     return a+b+c+d

# print(add_four_numbers(1,2,3,4))

# def add_three_numbers(a,b,c):
# print(a+b+c)

# add_three_numbers(3,5,9)

# def plus_number():
#     return int(input())+1

# result = plus_number()
# print(result)

# def 느낌표_추가_함수():
#     print(input("문장을 입력 해 주세요:")+"!")

# 느낌표_추가_함수()

def add_list_value():
    user = input("숫자 세개를 한칸씩 띄어서 입력:")
    user = user.split(" ")
    user = list(map(int, user))
    sum = 0
    for 변수 in user:
        sum += 변수
    print(sum)
        


add_list_value()
