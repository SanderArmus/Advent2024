import itertools

def evaluate_expression(numbers, operations):
    # Calculate the result from left to right
    result = numbers[0]
    for i in range(len(operations)):
        if operations[i] == '+':
            result += numbers[i + 1]
        elif operations[i] == '*':
            result *= numbers[i + 1]
    return result

def generate_parentheses(numbers):
    if len(numbers) == 1:
        return [str(numbers[0])]
    
    expressions = []
    for i in range(len(numbers)):
        for left in generate_parentheses(numbers[:i]):
            for right in generate_parentheses(numbers[i+1:]):
                # Add operators between left and right
                expressions.append(f"({left} {numbers[i]} {right})")
                # Add the case where we don't have a right part
                if right:
                    expressions.append(f"({left} {numbers[i]} {right})")
    return expressions

filename = 'advent/advent7.txt'
total_sum = 0  # Initialize a variable to hold the sum of all found combination answers
found_combinations = set()  # Use a set to track unique combinations

with open(filename, 'r') as file:
    for line in file:
        line = line.split(':')
        target_number = int(line[0])  # Convert line[0] to an integer
        numbers = list(map(int, line[1].split()))  # Convert elements in line[1] to integers
        
        # Generate all combinations of operations
        operations = ['+', '*']  # Define the list of operations
        found = False
        
        # Generate all possible expressions with parentheses
        for ops in itertools.product(operations, repeat=len(numbers)-1):
            expression = evaluate_expression(numbers, ops)
            if expression == target_number:
                combination_key = (tuple(numbers), ops)  # Create a unique key for the combination
                if combination_key not in found_combinations:
                    print(f"Combination found: {' '.join(map(str, numbers))} with operations {ops} = {target_number}")
                    total_sum += expression  # Add the found expression to the total sum
                    found_combinations.add(combination_key)  # Add the combination to the set
                    found = True
                    break  # Stop searching after finding the first valid combination
        
        # Check all combinations with parentheses only if no combination was found yet
        if not found:
            for parenthesis in generate_parentheses(numbers):
                try:
                    # Ensure the expression is valid for eval
                    if eval(parenthesis) == target_number:  # No need to replace spaces
                        if parenthesis not in found_combinations:  # Check if this combination is already counted
                            print(f"Combination found with parentheses: {parenthesis} = {target_number}")
                            total_sum += target_number  # Add the target number to the total sum
                            found_combinations.add(parenthesis)  # Add the combination to the set
                            found = True
                            break  # Stop searching after finding the first valid combination
                except ZeroDivisionError:
                    continue  # Handle any division by zero if applicable
                except SyntaxError:
                    continue  # Handle any syntax errors if applicable
        
        if not found:
            print(f"No combination found for {target_number} with numbers {numbers}.")

# Print the total sum of all found combination answers
print(f"Total sum of all found combination answers: {total_sum}")
