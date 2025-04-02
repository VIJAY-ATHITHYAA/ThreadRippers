def is_palindrome(s):
    """
    Check if a string is a palindrome using the double pointer technique.
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test the function
test_strings = [
    "A man, a plan, a canal: Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon"
]

for s in test_strings:
    print(f"'{s}': {is_palindrome(s)}")
