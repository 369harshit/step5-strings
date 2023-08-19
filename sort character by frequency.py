def sort_characters_by_frequency(input_str):
    # Create a dictionary to store character frequencies
    char_freq = {}
    
    # Count the occurrences of each character
    for char in input_str:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Sort characters based on frequencies
    sorted_chars = sorted(char_freq.keys(), key=lambda char: char_freq[char], reverse=True)
    
    # Construct the sorted string
    sorted_str = ''
    for char in sorted_chars:
        sorted_str += char * char_freq[char]

    
    return sorted_str

# Example usage
input_str = "tree"
sorted_str = sort_characters_by_frequency(input_str)
print(sorted_str)  
