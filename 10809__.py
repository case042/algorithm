user = input()
arr = []
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for alphabet in alphabets:
    for char in user:
        if alphabet == char:
            arr.append(user.find(char))
            break
    if user.find(alphabet) == -1:
        arr.append(-1)

for data in arr:
      print(data,end=" ")  