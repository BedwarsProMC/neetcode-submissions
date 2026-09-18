class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        // build an array initalised with new arrayliss
        for(int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        // count frequency of each item
        for(int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // put list of items with the frequency at that index
        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            // number : count
            // each index is the freuqncy with the value being an array of values/
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] toReturn = new int[k];
        int index = 0;
        for(int i = freq.length - 1; i > 0 && index < k; i--) {

            for(int n : freq[i]) {
                toReturn[index] = n;
                index++;
                if(index == k) {
                    return toReturn;
                }
            }
        }
        return new int[0];
    }

}
