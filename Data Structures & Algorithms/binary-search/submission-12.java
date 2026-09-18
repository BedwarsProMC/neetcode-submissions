class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        while(l <= r) {
            int middleIndex = l + ((r - l) / 2);

            int middleValue = nums[middleIndex];

            if(target == middleValue) {
                return middleIndex;
            } else if(target > middleValue) {
                l = middleIndex + 1;
            } else {
                r = middleIndex - 1;
            }
        }

        return -1;
    }

}
