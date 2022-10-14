# Task
# You are given a string S. Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format
# A single line containing a string S.

# Constraints 0 < len(S) < 1000

# Output Format
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in range(len(s)):
        if s[i].isalnum() and not alnum:
            alnum = True
        if s[i].isalpha() and not alpha:
            alpha = True
        if s[i].isdigit() and not digit:
            digit = True
        if s[i].islower() and not lower:
            lower = True
        if s[i].isupper() and not upper:
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)