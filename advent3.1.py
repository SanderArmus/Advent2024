import re

def extract_and_multiply(filename):
    pattern = r'(do\(\)|mul\((\d+),\s*(\d+)\)|don\'t|add\((\d+),\s*(\d+)\))'
    results = []
    with open(filename, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        for match in matches:
            results.append(match[0]) 

    return results

filename = '/Users/sanderarmus/Kool/Advent/advent3.txt'
results = extract_and_multiply(filename)

do_active = True 
total_sum = 0  
for command in results:
    print(f"Processing command: {command}")
    
    
    if command.startswith("don't"):
        do_active = False
        print("do_active set to False")
    
    elif command.startswith('do'):
        do_active = True 
        print("do_active set to True")

    elif command.startswith('mul') and do_active:
        num1, num2 = map(int, re.findall(r'\d+', command))
        product = num1 * num2
        total_sum += product
        print(f"Added {product} to total_sum")
print(f"Total sum: {total_sum}")
