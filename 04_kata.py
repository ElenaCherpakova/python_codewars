# Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).
# Example
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    return [i for i in range(nums[0], nums[-1]+1)]
        
print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
print(pipe_fix([1, 2, 3, 12]))
print(pipe_fix([6, 9]))