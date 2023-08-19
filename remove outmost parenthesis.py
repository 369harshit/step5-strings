def remove_outer_parentheses(s):
    count = 0
    result = ""

    for char in s:
        if char == '(':
            if count > 0:
                result += char
            count += 1
        elif char == ')':
            count -= 1
            if count > 0:
                result += char
    
    return result

# Example usage
input_string =  "(()())(())"
output_string = remove_outer_parentheses(input_string)
print(output_string)  # Output: "()()()"
