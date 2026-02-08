# LeetCode 1 - Two Sum
# Difficulty: Easy
# Topic: Array
# Approach: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def twoSum(lst,target):
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[i] + lst[j] == target:
        return [i,j]
