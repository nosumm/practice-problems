# Solution for two_sum (Python)
# Problem: https://leetcode.com/problems/two-sum/
def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

def test_twoSum(twoSum_function):
    # Test cases now include all possible valid answers
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "possible_answers": [[0, 1]]},
        {"nums": [3, 3], "target": 6, "possible_answers": [[0, 1]]},
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "possible_answers": [[2, 4]]},
        {"nums": [1, 2], "target": 3, "possible_answers": [[0, 1]]},
        {"nums": [1, 2, 3, 4, 5, 6], "target": 7, "possible_answers": [[0, 5], [1, 4], [2, 3]]},
    ]

    for case in test_cases:
        result = twoSum_function(case["nums"], case["target"])
        # Check if result is one of the possible answers
        assert sorted(result) in [sorted(pair) for pair in case["possible_answers"]], (
            f"Test failed for nums={case['nums']}, target={case['target']}. "
            f"Expected one of {case['possible_answers']}, got {result}"
        )
    print(f"All test cases passed for {twoSum_function.__name__}!")

if __name__ == '__main__':
    print("Testing optimized twoSum:")
    test_twoSum(twoSum)

    print("\nTesting brute-force twoSumBruteForce:")
    test_twoSum(twoSumBruteForce)

