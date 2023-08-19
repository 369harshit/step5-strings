def beauty_value(substring):
    # Calculate the beauty value for a single substring
    char_freq = {}
    for char in substring:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    max_freq = max(char_freq.values())
    min_freq = min(char_freq.values())
    return max_freq - min_freq

def sum_beauty_of_all_substrings(input_str):
    total_beauty = 0
    n = len(input_str)
    
    # Iterate through all substrings
    for i in range(n):
        for j in range(i, n):
            substring = input_str[i:j+1]
            total_beauty += beauty_value(substring)
    
    return total_beauty

# Example usage
input_str = "aabcb"
total_beauty = sum_beauty_of_all_substrings(input_str)
print(total_beauty)  # Output: 5
