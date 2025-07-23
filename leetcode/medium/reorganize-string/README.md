# Reorganize-String

## Problem
Source: [leetcode](https://leetcode.com/problems/reorganize-string/)

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""


Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.


### Approach

1) Count Character Frequencies:
    Count how many times each character appears in the string. 
    Determine if a valid rearrangement is possible. 
    if any char's count exceeds half the length of the string (rounded up) --> impossible to rearrange. 
    For example, in a string of length 4, no character should appear more than 2 times.

2) Use a Max-Heap
    Use a max-heap (or a priority queue) to always pick the character with the highest remaining count. Place the most frequent characters first.

3) Build the Result String: 
    Repeatedly take the two most frequent characters (if available) from the heap
    Append them to the result
    Decrementing their counts. 
    If only one character remains with a count greater than zero, append it once. 
    This process continues until all characters are placed in the string or it's determined that no valid arrangement is possible.


## Solutions
| Language | File |
|----------|------|
| Python | [reorganize-string.py](python/reorganize-string.py) |
| Java | [Reorganize-String.java](java/Reorganize-String.java) |
| C | [reorganize-string.c](c/reorganize-string.c) |