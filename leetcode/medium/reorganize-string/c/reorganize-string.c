// Solution for reorganize-string (C)
// Problem: https://leetcode.com/problems/reorganize-string/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char character;
    int count;
} CharCount;

int compare(const void *a, const void *b) {
    return ((CharCount*)b)->count - ((CharCount*)a)->count;
}

char* reorganizeString(char* s) {
    int count[26] = {0};
    int len = strlen(s);
    
    // Count character frequencies
    for (int i = 0; i < len; i++) {
        count[s[i] - 'a']++;
    }
    
    // Check if rearrangement is possible
    int max_count = 0;
    char max_char;
    for (int i = 0; i < 26; i++) {
        if (count[i] > max_count) {
            max_count = count[i];
            max_char = 'a' + i;
        }
    }
    if (max_count > (len + 1) / 2) {
        char* result = malloc(1);
        result[0] = '\0';
        return result;
    }
    
    // Create an array of CharCount and sort it
    CharCount char_counts[26];
    int num_chars = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] > 0) {
            char_counts[num_chars].character = 'a' + i;
            char_counts[num_chars].count = count[i];
            num_chars++;
        }
    }
    qsort(char_counts, num_chars, sizeof(CharCount), compare);
    
    // Build the result string
    char* result = malloc(len + 1);
    int pos = 0;
    
    while (char_counts[0].count > 0) {
        // Place the most frequent character
        result[pos++] = char_counts[0].character;
        char_counts[0].count--;
        
        // If there's a second most frequent character, place it
        if (char_counts[1].count > 0) {
            result[pos++] = char_counts[1].character;
            char_counts[1].count--;
        }
        
        // Re-sort to maintain order
        qsort(char_counts, num_chars, sizeof(CharCount), compare);
    }
    
    result[pos] = '\0';
    return result;
}

int main() {
    char* test_cases[] = {"aab", "aaab", "a", "aa", "abc", "aabbcc", "aaaaa", "aabb", "aabbb", "aabbbc"};
    int num_tests = sizeof(test_cases) / sizeof(test_cases[0]);
    
    for (int i = 0; i < num_tests; i++) {
        char* result = reorganizeString(test_cases[i]);
        printf("Input: %s\nOutput: %s\n\n", test_cases[i], result);
        free(result);
    }
    
    return 0;
}