// Solution for design-parking-system (Java)
// Problem: https://leetcode.com/problems/design-parking-system/

class parkingSystem{
    private int[] slots;

    public ParkingSystem(int big, int medium, int small){
        slots = new int[]{big, medium, small};
    }

    public boolean addCar(int carType){
        if(slots[carType - 1] > 0){
            slots[carType - 1]--;
            return true;
        }
        return false;
    }
}