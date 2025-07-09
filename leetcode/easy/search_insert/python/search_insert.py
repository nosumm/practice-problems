# Solution for search_insert (Python)
# Problem: https://leetcode.com/problems/search-insert/

def searchInsertBruteForce(nums, target):
   # brute force solution o(n) time complexity iterates through array linearly
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)

def searchInsert(nums, target):
    # optimized solution with binary search to achieve O(logn) time complexity
     
    # init left and right pointers at the start and end of the array
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def test_searchInsert():
    # Test cases
    test_cases = [
        # Target found in the array
        {"nums": [1, 3, 5, 6], "target": 5, "expected": 2},
        # Target not found, insert at the beginning
        {"nums": [1, 3, 5, 6], "target": 0, "expected": 0},
        # Target not found, insert in the middle
        {"nums": [1, 3, 5, 6], "target": 2, "expected": 1},
        # Target not found, insert at the end
        {"nums": [1, 3, 5, 6], "target": 7, "expected": 4},
        # Single-element array, target found
        {"nums": [1], "target": 1, "expected": 0},
        # Single-element array, target not found (insert at beginning)
        {"nums": [1], "target": 0, "expected": 0},
        # Single-element array, target not found (insert at end)
        {"nums": [1], "target": 2, "expected": 1},
        # Empty array
        {"nums": [], "target": 1, "expected": 0},
    ]

    # Run each test case
    for case in test_cases:
        result = searchInsert(case["nums"], case["target"])
        assert result == case["expected"], (
            f"Test failed for nums={case['nums']}, target={case['target']}. "
            f"Expected {case['expected']}, got {result}"
        )
    print("All test cases passed!")


if __name__ == '__main__':
    test_searchInsert()