# Solution for maximumUnitsOnATruck (Python)
# Problem: https://leetcode.com/problems/maximum-units-on-a-truck/
def maximumUnits(boxTypes, truckSize):
    # sort the boxTypes in descending order of units per box
    boxTypes.sort(key=lambda x: -x[1])

    total_units = 0
    remaining_size = truckSize

    for boxes, units in boxTypes:
        if remaining_size <= 0:
            break
        take = min(boxes, remaining_size)
        total_units += take * units
        remaining_size -= take
    return total_units


def test_maximumUnits():
    # Test Case 1: Example from the problem statement
    boxTypes1 = [[1, 3], [2, 2], [3, 1]]
    truckSize1 = 4
    expected1 = 8
    result1 = maximumUnits(boxTypes1, truckSize1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed")

    # Test Case 2: Another example from the problem statement
    boxTypes2 = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize2 = 10
    expected2 = 91
    result2 = maximumUnits(boxTypes2, truckSize2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed")

    # Test Case 3: Truck size is exactly enough for all boxes
    boxTypes3 = [[2, 5], [3, 10]]
    truckSize3 = 5
    expected3 = 35  # 2*5 + 3*10 = 10 + 30 = 40, but truckSize is 5, so 2*5 + 3*10 = 35? Wait, no. Let's compute:
    # Take all 2 boxes of type 1 (2*5=10) and 3 boxes of type 2 (3*10=30), total boxes 2+3=5, total units 10+30=40
    expected3 = 40
    result3 = maximumUnits(boxTypes3, truckSize3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed")

    # Test Case 4: Truck size is larger than total boxes
    boxTypes4 = [[1, 2], [1, 3]]
    truckSize4 = 5
    expected4 = 5  # 1*2 + 1*3 = 5
    result4 = maximumUnits(boxTypes4, truckSize4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Test Case 4 Passed")

    # Test Case 5: Only one type of box
    boxTypes5 = [[10, 5]]
    truckSize5 = 3
    expected5 = 15  # 3*5 = 15
    result5 = maximumUnits(boxTypes5, truckSize5)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Test Case 5 Passed")

    # Test Case 6: Edge case with truckSize 0
    boxTypes6 = [[1, 2], [2, 3]]
    truckSize6 = 0
    expected6 = 0
    result6 = maximumUnits(boxTypes6, truckSize6)
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Test Case 6 Passed")

    # Test Case 7: Edge case with empty boxTypes
    boxTypes7 = []
    truckSize7 = 10
    expected7 = 0
    result7 = maximumUnits(boxTypes7, truckSize7)
    assert result7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Test Case 7 Passed")

    print("All Test Cases Passed!")


if __name__ == '__main__':
    test_maximumUnits()