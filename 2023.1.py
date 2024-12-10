with open('advent/2023.1.txt', 'r') as file:
    res=0
    for line in file:
        digits=""
        for char in line:
            if char.isdigit():
                digits+=char
        res+=int(digits[0]+digits[-1])
    print(res)