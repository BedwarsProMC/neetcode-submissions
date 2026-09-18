class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) { 
            int curVal = nums[i];
            int needVal = target - curVal;

            if(map.containsKey(needVal)) {
                int j = map.get(needVal);
                return new int[]{j, i};
            } else {
                map.put(curVal, i);
            }
        }
        return new int[]{0,0};
    }
}
