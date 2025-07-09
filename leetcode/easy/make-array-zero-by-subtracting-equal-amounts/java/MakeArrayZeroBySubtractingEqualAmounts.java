// Solution for make-array-zero-by-subtracting-equal-amounts (Java)
// Problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
import java.util.HashSet;
import java.util.Set;

public class MakeArrayZeroBySubtractingEqualAmounts {
    public int minimumOperations(int[] nums) {
        Set<Integer> uniqueNonZero = new HashSet<>();
        for (int num : nums){
            if (num != 0){
                uniqueNonZero.add(num);
            }
        }
        return uniqueNonZero.size();
    }
    public static void main(String[] args) {
        System.out.println("Testing Java Solution for make-array-zero-by-subtracting-equal-amounts");
        MakeArrayZeroBySubtractingEqualAmounts solution = new MakeArrayZeroBySubtractingEqualAmounts();
        int[] nums1 = {1, 5, 0, 3, 5};
        int[] nums2 = {0};
        if(solution.minimumOperations(nums1) == 3) {
            System.out.println("Test 1 Passed");
        } else{
            System.out.println("Test 1 Failed");
        }
        
        if(solution.minimumOperations(nums2) == 0) {
            System.out.println("Test 2 Passed");
        } else{
            System.out.println("Test 2 Failed");
        }
    }

}