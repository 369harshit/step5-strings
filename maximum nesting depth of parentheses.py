def max_nesting_depth(s):
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    
    return max_depth

# Example usage
s = "(1)+((2))+(((3)))"
result = max_nesting_depth(s)
print(result)  # Output: 3
