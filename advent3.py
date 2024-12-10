import re

def extract_and_multiply(filename):
    pattern = r'mul\((\d+),\s*(\d+)\)'

    results = []
    with open(filename, 'r') as file:
        content = file.read()

        matches = re.findall(pattern, content)

        for match in matches:
            num1, num2 = map(int, match) 
            product = num1 * num2
            results.append((num1, num2, product))

    return results

filename = '/Users/sanderarmus/Kool/Advent/advent3.txt'
results = extract_and_multiply(filename)

for num1, num2, product in results:
    print(f'mul({num1}, {num2}) = {product}')
sum=0
for result in results:
    sum+=result[2]  
print(sum)