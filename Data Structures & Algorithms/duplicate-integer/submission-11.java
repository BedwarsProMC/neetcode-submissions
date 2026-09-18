class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for(int number : nums) {
            if(seen.contains(number)) {
                return true;
            }
            seen.add(number);
        }
        return false;

    }
}