filename = '/Users/sanderarmus/Kool/Advent/advent1.txt'
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

total_sum = 0 
for i in range(len(list1)):
    total_sum += list1[i]*list2.count(list1[i])
print(total_sum)