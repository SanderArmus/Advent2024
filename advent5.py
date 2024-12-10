def is_correctly_ordered(update, rules):
    page_indices = {page: idx for idx, page in enumerate(update)}
    
    for rule in rules:
        a, b = map(int, rule.split('|'))
        if a in page_indices and b in page_indices:
            if page_indices[a] > page_indices[b]:
                return False
    return True

def correct_order(update, rules):
    page_indices = {page: idx for idx, page in enumerate(update)}
    ordered_update = []
    visited = set()

    def visit(page):
        if page in visited:
            return
        visited.add(page)
        for rule in rules:
            a, b = map(int, rule.split('|'))
            if a == page and b in page_indices:
                visit(b)
        ordered_update.append(page)

    for page in update:
        visit(page)

    ordered_update.reverse()
    return ordered_update

def solve(pages_rules, updates):
    rules = pages_rules.splitlines()
    updates = [list(map(int, update.split(','))) for update in updates.splitlines()]
    
    middle_elements = []
    
    for update in updates:
        if not is_correctly_ordered(update, rules):
            corrected_update = correct_order(update, rules)
            middle_index = len(corrected_update) // 2
            middle_elements.append(corrected_update[middle_index])
    
    print(f"Middle Elements from Corrected Updates: {middle_elements}")
    
    total_sum = sum(middle_elements)
    print(f"Total Sum of Middle Elements from Corrected Updates: {total_sum}")
    return total_sum

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        
    separator_index = lines.index('')
    pages_rules = '\n'.join(lines[:separator_index])
    updates = '\n'.join(lines[separator_index + 1:])
    
    return pages_rules, updates

filename = '/Users/sanderarmus/Kool/Advent/advent5.txt'
pages_rules, updates = read_input_from_file(filename)
result = solve(pages_rules, updates)
print(result) 
