// Solution for make-array-zero-by-subtracting-equal-amounts (C)
// Problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
#include <stdio.h>
#include <stdlib.h>

// Comparision function for qsort
int compare(const void* a, const void* b){
    return (*(int*)a - *(int*)b);
}

int minimumOperations(int* nums, int numsSize){
    // sort the array first
    qsort(nums, numsSize, sizeof(int), compare);
    int count = 0;
    int prev = 0;

    for (int i = 0; i < numsSize; i++){
        if(nums[i] != 0 && nums[i] != prev){
            count++;
            prev = nums[i];
        }
    }
    return count;
}
int main() {
    printf("Solution for make-array-zero-by-subtracting-equal-amounts\n");
        // Test Case 1
    int nums1[] = {1, 5, 0, 3, 5};
    int size1 = sizeof(nums1)/sizeof(nums1[0]);
    int result1 = minimumOperations(nums1, size1);
    printf("Test Case 1: Expected 3, Got %d - %s\n", 
           result1, result1 == 3 ? "PASSED" : "FAILED");
    
    // Test Case 2
    int nums2[] = {0};
    int size2 = sizeof(nums2)/sizeof(nums2[0]);
    int result2 = minimumOperations(nums2, size2);
    printf("Test Case 2: Expected 0, Got %d - %s\n", 
           result2, result2 == 0 ? "PASSED" : "FAILED");
    
    // Edge Case - All zeros
    int nums3[] = {0, 0, 0};
    int size3 = sizeof(nums3)/sizeof(nums3[0]);
    int result3 = minimumOperations(nums3, size3);
    printf("Test Case 3: Expected 0, Got %d - %s\n", 
           result3, result3 == 0 ? "PASSED" : "FAILED");
    
    // Edge Case - Large numbers
    int nums4[] = {1000000, 999999, 1000000};
    int size4 = sizeof(nums4)/sizeof(nums4[0]);
    int result4 = minimumOperations(nums4, size4);
    printf("Test Case 4: Expected 2, Got %d - %s\n", 
           result4, result4 == 2 ? "PASSED" : "FAILED");
    
    return 0;
}



