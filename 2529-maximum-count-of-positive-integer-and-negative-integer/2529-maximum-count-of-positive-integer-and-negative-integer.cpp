class Solution {
    int binarySearch(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        int idx = -1;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] <= target) {
                left = mid + 1;
                idx = mid;
            } else {
                right = mid - 1;
            }
        }
        return idx;
    }
public:
    int maximumCount(vector<int>& nums) {
        int posNegOne = binarySearch(nums, -1);
        int posZero = binarySearch(nums, 0);
        return max(posNegOne + 1, (int) nums.size() - posZero - 1);
    }
};