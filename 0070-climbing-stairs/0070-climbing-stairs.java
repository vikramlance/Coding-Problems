class Solution {
    public int climbStairs(int n) {
        int ways1 = 0;
        int ways2 = 1;

        for (int i =1;i<=n;i++) {      
            int temp = ways2;
            ways2 = ways2 + ways1;
            ways1 = temp; 
        }
        return ways2;
    }
}