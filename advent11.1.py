with open('advent2024/advent11.txt', 'r') as file:
    data = file.read()
    list_data = data.split()
m = len(list_data)
n = 0 
answerlist = []
while n < 75:
    current_list = []
    for item in list_data:
        if int(item) == 0:
            current_list.append(1)
        else:
            if len(str(item)) % 2 == 0:
                half_length = len(str(item)) // 2
                current_list.append(int(str(item)[:half_length]))
                current_list.append(int(str(item)[half_length:]))
            else:
                current_list.append(int(item) * 2024)
    list_data = current_list
    n += 1
    print(n)
print("Final answer", len(current_list))
