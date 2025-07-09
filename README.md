# practice-problems

## Adding New Problems
#### From repo root, run:
python generate_problem.py "problem_name" --source "leetcode" --difficulty "easy"

##  Testing Automation

This repo uses GitHub Actions to automatically test solutions in Python, Java, and C. Here's how it works:

###  How to Run Tests
1. **Manually trigger tests**:
   - Via GitHub UI: 
     1. Go to **Actions** tab
     2. Select **"Test Solutions"** workflow
     3. Click **"Run workflow"**
   - Via CLI (requires [GitHub CLI](https://cli.github.com)):
     ```bash
     gh workflow run "Test Solutions"
     ```

2. **What gets tested**:
   - All solution files matching these patterns:
     - Python: `**/*.py` (except in `test/` directories)
     - Java: `**/*.java`
     - C: `**/*.c`

###  How to Write Testable Solutions
For tests to work, each solution file must include executable code:

#### Python Example
```python
# practice-problems/leetcode/two_sum.py
def two_sum(nums, target):
    # Your solution
    return [0, 1]  # Example

if __name__ == "__main__":
    assert two_sum([2,7,11,15], 9) == [0, 1]  # Test case
    print("✓ Test passed")

#### Java Example 
// practice-problems/leetcode/TwoSum.java
public class TwoSum {
    public static void main(String[] args) {
        int[] result = twoSum(new int[]{2,7,11,15}, 9);
        assert result[0] == 0 && result[1] == 1;
        System.out.println("✓ Test passed");
    }
    
    public static int[] twoSum(int[] nums, int target) {
        return new int[]{0, 1};  // Example
    }
}

#### C Example
// practice-problems/leetcode/two_sum.c
#include <stdio.h>
#include <assert.h>

int* twoSum(int* nums, int numsSize, int target) {
    static int result[2] = {0, 1};  // Example
    return result;
}

int main() {
    int nums[] = {2,7,11,15};
    int* result = twoSum(nums, 4, 9);
    assert(result[0] == 0 && result[1] == 1);
    printf("✓ Test passed\n");
    return 0;
}


