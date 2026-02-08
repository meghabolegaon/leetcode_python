# LeetCode 9 - Palindrome Number
# Difficulty: Easy
# Topic: Math
# Approach: Reverse the number
# Time Complexity: O(n)
# Space Complexity: O(1)
def isPalindrome(x):
    if x < 0:
        return False
    
    original = x
    rev = 0

    while x > 0:
        x,r =divmod(x,10)
        rev = rev * 10 + r
      
    return original == rev
