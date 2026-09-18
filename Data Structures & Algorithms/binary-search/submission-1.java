class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while(l <= r) {
            int middleIndex = l + ((r - l) / 2);

            if (nums[middleIndex] == target)
                return middleIndex;
            
            if(nums[middleIndex] > target)
                r = middleIndex - 1;
            else 
                l = middleIndex + 1;
        }

        return -1;
    }
}
