// Solution for maximumUnitsOnATruck (C)
// Problem: https://leetcode.com/problems/maximumUnitsOnATruck/
#include <stdio.h>
#include <stdlib.h>


// Comparator function for sorting box types in descending order of units per box
int compare(const void *a, const void *b){
    const int *boxA = *(const int **)a;
    const int *boxB = *(const int **)b;
    return boxB[1] - boxA[1];
}

int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize){
     // Early return if no boxes are provided
    if (boxTypes == NULL || boxTypesSize == 0) {
        return 0;
    }
    
    // sort the boxTypes array based on units per box in descending order
    qsort(boxTypes, boxTypesSize, sizeof(int*), compare);

    int totalUnits = 0;
    int remainingSize = truckSize;

    for (int i = 0; i < boxTypesSize; i++){
        if (remainingSize <= 0){
            break;
        }
        int boxes = boxTypes[i][0];
        int units = boxTypes[i][1];
        int take = boxes < remainingSize ? boxes : remainingSize;
        totalUnits += take * units;
        remainingSize -= take;
    }
    return totalUnits;
}

// Function to test the maximumUnits function
void test_maximumUnits() {
    // Test Case 1: Example from the problem statement
    int *boxTypes1[] = {
        (int[]){1, 3},
        (int[]){2, 2},
        (int[]){3, 1}
    };
    int boxTypesColSize1[] = {2, 2, 2};
    int truckSize1 = 4;
    int expected1 = 8;
    int result1 = maximumUnits(boxTypes1, 3, boxTypesColSize1, truckSize1);
    printf("Test Case 1: Expected %d, got %d\n", expected1, result1);
    
    // Test Case 2: Another example from the problem statement
    int *boxTypes2[] = {
        (int[]){5, 10},
        (int[]){2, 5},
        (int[]){4, 7},
        (int[]){3, 9}
    };
    int boxTypesColSize2[] = {2, 2, 2, 2};
    int truckSize2 = 10;
    int expected2 = 91;
    int result2 = maximumUnits(boxTypes2, 4, boxTypesColSize2, truckSize2);
    printf("Test Case 2: Expected %d, got %d\n", expected2, result2);
    
    // Test Case 3: Truck size is exactly enough for all boxes
    int *boxTypes3[] = {
        (int[]){2, 5},
        (int[]){3, 10}
    };
    int boxTypesColSize3[] = {2, 2};
    int truckSize3 = 5;
    int expected3 = 40;
    int result3 = maximumUnits(boxTypes3, 2, boxTypesColSize3, truckSize3);
    printf("Test Case 3: Expected %d, got %d\n", expected3, result3);
    
    // Test Case 4: Truck size is larger than total boxes
    int *boxTypes4[] = {
        (int[]){1, 2},
        (int[]){1, 3}
    };
    int boxTypesColSize4[] = {2, 2};
    int truckSize4 = 5;
    int expected4 = 5;
    int result4 = maximumUnits(boxTypes4, 2, boxTypesColSize4, truckSize4);
    printf("Test Case 4: Expected %d, got %d\n", expected4, result4);
    
    // Test Case 5: Only one type of box
    int *boxTypes5[] = {
        (int[]){10, 5}
    };
    int boxTypesColSize5[] = {2};
    int truckSize5 = 3;
    int expected5 = 15;
    int result5 = maximumUnits(boxTypes5, 1, boxTypesColSize5, truckSize5);
    printf("Test Case 5: Expected %d, got %d\n", expected5, result5);
    
    // Test Case 6: Edge case with truckSize 0
    int *boxTypes6[] = {
        (int[]){1, 2},
        (int[]){2, 3}
    };
    int boxTypesColSize6[] = {2, 2};
    int truckSize6 = 0;
    int expected6 = 0;
    int result6 = maximumUnits(boxTypes6, 2, boxTypesColSize6, truckSize6);
    printf("Test Case 6: Expected %d, got %d\n", expected6, result6);
    
    // Test Case 7: Edge case with empty boxTypes
    int **boxTypes7 = NULL;
    int boxTypesColSize7[] = {};
    int truckSize7 = 10;
    int expected7 = 0;
    int result7 = maximumUnits(boxTypes7, 0, boxTypesColSize7, truckSize7);
    printf("Test Case 7: Expected %d, got %d\n", expected7, result7);
}

int main() {
    test_maximumUnits();
    return 0;
}