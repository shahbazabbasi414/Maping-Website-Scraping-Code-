import csv

with open('test1.csv', 'r') as file:
    reader = csv.reader(file)
    column_index = 2  
    column = []
    for row in reader:
        column.append(row[column_index])
    print(column)
for i in column:
    print(i)



