def read_columns_from_file(filename):
    col1, col2 = [], []
    with open(filename, 'r') as file:
        for line in file:

            num1, num2 = map(int, line.split())
            col1.append(num1)
            col2.append(num2)
    return col1, col2

file_path = 'advent/advent1.txt'
list1, list2 = read_columns_from_file(file_path)

slist1 = sorted(list1)
slist2 = sorted(list2)
total_sum = 0
for i in range(len(slist1)):
    difference = abs(slist1[i] - slist2[i])
    total_sum += difference
    print(difference)
print(total_sum)
