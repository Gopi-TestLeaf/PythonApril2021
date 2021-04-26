with open('text2.txt', mode='r') as file:
    data = file.read()
    print(data)

with open('text3.txt', 'r') as file:
    data = file.readlines()
    print(data)

with open('text1.txt') as file:
    data = file.read()
    print(data)