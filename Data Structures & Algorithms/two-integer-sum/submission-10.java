class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if(seen.containsKey(diff)) {
                int index = seen.get(diff);
                return new int[]{index, i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};



        // for(int i = 0; i < nums.length; i++) {
        //     for (int j = i + 1; j < nums.length; j++) {
        //         if(nums[i] + nums[j] == target) {
        //             return new int[]{i,j};
        //         }
        //     }
        // }
        // return new int[]{0,0};

    }
}
