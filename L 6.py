import csv
row = ['Ivanov', 'Ivan', 'Ivanovich']
row1 = ['Petrov', 'Petr', 'Petrovich']
row2 = ['Sergeev', 'Sergej', 'Srgeevich']
with open('users.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(row)
    writer.writerow(row1)
    writer.writerow(row2)

import csv
row = ['Oxota', 'Rubalka']
row1 = ['Strelba']
with open('hobby.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(row)
    writer.writerow(row1)

