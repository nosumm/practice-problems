# Solution for reorganize-string (Python)
# Problem: https://leetcode.com/problems/reorganize-string/
import heapq
from collections import defaultdict


def reorganizeString(s):
    # count the frequencies of each char
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    # create a max heap
    # python heapq is a min-heap, so use negative values
    max_heap = []
    for char, count in freq.items():
        heapq.heappush(max_heap, (-count, char))
    
    res = []
    while len(max_heap) >= 2:
        # pop the two most frequent chars
        count1, char1 = heapq.heappop(max_heap)
        count2, char2 = heapq.heappop(max_heap)
        res.extend([char1, char2])

        # decrement the counts 
        # and push back to heap if remaining count > 0
        if count1 + 1 < 0:
            heapq.heappush(max_heap, (count1 + 1, char1))
        if count2 + 1 < 0:
            heapq.heappush(max_heap, (count2 + 1, char2))
        
    # handle any remaining char
    if max_heap:
        remaining_count, remaining_char = heapq.heappop(max_heap)
        if -remaining_count > 1:
            return ""
        res.append(remaining_char)
    return ''.join(res)

        

if __name__ == '__main__':
    # Test cases
    test_cases = [
        ("aab", ["aba"]),
        ("aaab", [""]),
        ("a", ["a"]),
        ("aa", [""]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("aabbcc", ["abacbc", "abcabc", "acbacb", "bacbac", "bcabca", "cabcab", "cbacba"]),
        ("aaaaa", [""]),
        ("aabb", ["abab", "baba"]),
        ("aabbb", ["ababb", "babab"]),
        ("aabbbc", ["ababcb", "abcbab", "bababc", "babacb", "bacbab", "bcabab", "bcbaba", "cbabab"]),
    ]
    for input_str, expected_outputs in test_cases:
        result = reorganizeString(input_str)
        if result == "":
            if "" in expected_outputs:
                print(f"Test passed: Input '{input_str}' => Output '{result}' (Expected one of: {expected_outputs})")
            else:
                print(f"Test failed: Input '{input_str}' => Output '{result}' (Expected one of: {expected_outputs})")
        else:
            # Check if the result is a valid permutation with no adjacent duplicates
            is_valid = True
            for i in range(len(result) - 1):
                if result[i] == result[i + 1]:
                    is_valid = False
                    break
            if is_valid and sorted(result) == sorted(input_str) and result in expected_outputs:
                print(f"Test passed: Input '{input_str}' => Output '{result}' (Expected one of: {expected_outputs})")
            else:
                print(f"Test failed: Input '{input_str}' => Output '{result}' (Expected one of: {expected_outputs})")