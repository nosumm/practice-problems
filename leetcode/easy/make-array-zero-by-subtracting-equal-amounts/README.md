# Make-Array-Zero-By-Subtracting-Equal-Amounts

## Problem
Source: [leetcode](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/)
*included in top amazon questions problem list. 
## Notes

You are given a non-negative integer array nums. 
In one operation: 
- choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- subtract x from every positive element in nums.

Return the minimum number of operatiosn to make every element in nums equal to 0. 

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.

 
Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100


## Approach

1. Extract all non-zero elements from the array.
2. Find the number of unique elements in the list. 
3. Number of unique elements = number of operations needed. return that count. 

### Pseudo Code

function minimumOperations(nums):
    unique_non_zeros = empty set
    for each num in nums:
        if num != 0:
            add num to unique_non_zeros
    return size of unique_non_zeros

## Solutions
| Language | File |
|----------|------|
| Python | [make-array-zero-by-subtracting-equal-amounts.py](python/make-array-zero-by-subtracting-equal-amounts.py) |
| Java | [Make-Array-Zero-By-Subtracting-Equal-Amounts.java](java/Make-Array-Zero-By-Subtracting-Equal-Amounts.java) |
| C | [make-array-zero-by-subtracting-equal-amounts.c](c/make-array-zero-by-subtracting-equal-amounts.c) |