def can_shift_to_goal(s, goal):
    if len(s) != len(goal):
        return False
    
    for i in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]  # Shift the leftmost character to the rightmost position
    
    return False

s = "abcde"
goal = "cdeab"
result = can_shift_to_goal(s, goal)
print(result)
