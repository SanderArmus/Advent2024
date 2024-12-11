from functools import lru_cache
def parse(input_string):
    return list(map(int, input_string.split()))
def blink(n):
    if n == 0:
        return [1]

    digits = str(n)
    length = len(digits)

    if length % 2 == 0:
        half_length = length // 2
        left = int(digits[:half_length])
        right = int(digits[half_length:])
        return [left, right]

    return [2024 * n]
@lru_cache(maxsize=None)
def descendant_count(iters, n):
    if iters == 0:
        return 1
    return sum(descendant_count(iters - 1, next_n) for next_n in blink(n))
def solve(iters, parsed):
    return sum(descendant_count(iters, n) for n in parsed)
def solve2(parsed):
    return solve(75, parsed)

def read_file(filename):
    with open(filename) as f:
        return f.read().strip()

input_string = read_file("advent2024/advent11.txt")
parsed_data = parse(input_string)
print("Solve 75 iterations:", solve2(parsed_data))