class Solution {
    
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        if(s.length() != t.length()) 
            return false;
        
        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();

        for(int i = 0; i < sChar.length; i ++) {
            sMap.put(sChar[i], 
                sMap.getOrDefault(sChar[i], 0) + 1
            );
            tMap.put(tChar[i], 
                tMap.getOrDefault(tChar[i], 0) + 1
            );
        }

        return sMap.equals(tMap);
    }

}
