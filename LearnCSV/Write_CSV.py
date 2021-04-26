import csv

with open('data.csv', 'w', newline="") as file:
    write = csv.writer(file)
    header = ['f_name', 'l_name', 'email']
    write.writerow(header)

    rows = [
        ['Gopi', 'J', 'gopithri@gmail.com'],
        ['sarath', 'm', 'sarath@gmail.com'],
        ['balaji', 'm', 'balaji@gmail.com']
    ]

    write.writerows(rows)