import csv

with open('data.csv') as file:
    data = csv.reader(file)
    for row in data:
        for cell in row:
            print(cell)
        print()

print('*'*25)
with open('data.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row[0].ljust(15), row[1].ljust(15), row[2])

print('*'*25)

with open('data.csv') as file:
    data = csv.DictReader(file)
    print(type(data))
    for row in data:
        print(row['f_name'].ljust(15), row['l_name'].ljust(15), row['email'])