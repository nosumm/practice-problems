# Solution for design-parking-system (Python)
# Problem: https://leetcode.com/problems/design-parking-system/

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spaces = {
            1: big, 
            2: medium, 
            3: small
        }
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1
            return True
        return False
        