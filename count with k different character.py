def count_substrings_with_k_chars(input_str, k):
    n = len(input_str)
    total_substrings = 0
    
    for i in range(n):
        char_set = set()
        for j in range(i, n):
            char_set.add(input_str[j])
            if len(char_set) == k:
                total_substrings += 1
            elif len(char_set) > k:
                break
    
    return total_substrings

# Example usage
input_str = "abcad"
k = 2
result = count_substrings_with_k_chars(input_str, k)
print(result)  
