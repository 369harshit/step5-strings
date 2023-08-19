def largest_odd_substring(num):
    largest_odd = ""
    
    for i in range(len(num)):
        for j in range(i + 1, len(num) + 1):
            substring = num[i:j]
            if substring.isdigit() and int(substring) % 2 != 0:
                if largest_odd == "" or int(substring) > int(largest_odd):
                    largest_odd = substring
    
    return largest_odd

num = "52"
result = largest_odd_substring(num)
print(result)
