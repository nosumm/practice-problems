# Solution for make-array-zero-by-subtracting-equal-amounts (Python)
# Problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
def minimumOperations(nums):
    unique_non_zero = set()
    for num in nums:
        if num != 0:
            unique_non_zero.add(num)
    return len(unique_non_zero)

if __name__ == '__main__':
    if (minimumOperations([1,5,0,3,5]) == 3):
        print("Test Case 1 Passed")
    else:
        print("Test Case 1 Failed")
    
    if (minimumOperations([0]) == 0):
        print("Test Case 2 Passed")
    else:
        print("Test Case 2 Failed")