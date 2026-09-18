class Solution {
    
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) 
            return false;

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        
        char[] tChar = t.toCharArray();

        for(int i = 0; i < s.length(); i ++) {
            sMap.put(s.charAt(i), 
                sMap.getOrDefault(s.charAt(i), 0) + 1
            );
            tMap.put(tChar[i], 
                tMap.getOrDefault(tChar[i], 0) + 1
            );
        }

        return sMap.equals(tMap);
    }

}
