#file_obj = open('text1.txt', mode='w')
#file_obj.write("hello everyone")
#file_obj.close()

# Way 01
file = open('text2.txt', mode='w')
for i in range(1, 11):
    file.write(f"hello all, my id number is ID: {i} \n")
print(file.closed)
file.close()
print(file.closed)

# Way 02
with open('text3.txt', mode='w') as file:
    for i in range(1, 11):
        file.write(f"5 * {i} = {5 * i} \n")