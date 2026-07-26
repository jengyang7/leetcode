class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int med = (left + right) / 2;

            if (nums[med] == target){
                return med;
            } else if (nums[med] < target){
                left = med + 1;
            } else{
                right = med - 1;
            }
            
        }
        return -1;
    }
}