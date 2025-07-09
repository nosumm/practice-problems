# Solution for plus_one (Python)
# Problem: https://leetcode.com/problems/plus-one/

def plusOne(digits):
    # init a pointer at the last digit of the array
    # check if you can add to the last digit. if you can, do so and return resulting array
    # if you cannot, move the pointer to the left by 1 digit 
        n = len(digits)
        for i in range(n - 1, -1, -1): 
            if digits[i] < 9:
                 digits[i] += 1
                 return digits
            digits[i] = 0
        return [1] + digits 





if __name__ == '__main__':
    print(plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(plusOne([9]))  # Output: [1, 0]
    print(plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]