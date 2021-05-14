import csv

with open('students.csv', encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    from collections import defaultdict

    group_ids = defaultdict(list)
    for row in csv_reader:
        if line_count == 1:
            print(f'Column names are {", ".join(row[0].split(";"))}')
            line_count += 1
        else:
            row = row[0].split(';')
            if row[9] == ' ':
                group_ids['open university'].append((row[4] + " " + row[5]))
                print('open University')
            else:
                group_ids[row[9].rstrip().lower()].append((row[4] + " " + row[5]))
                print(row[9].rstrip())

            line_count += 1

    while True:
        val = input("Enter your value: ")
        if val == 'q':
            break
        print(group_ids[val.lower()])
