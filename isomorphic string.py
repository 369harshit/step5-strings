def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping = {}  # To store the mapping from s to t characters
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        if s_char in mapping:
            if mapping[s_char] != t_char:
                return False
        else:
            if t_char in mapping.values():
                return False
            mapping[s_char] = t_char
    
    return True

s = "egg"
t = "add"
result = are_isomorphic(s, t)
print(result)
