class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> sMap = new HashMap<>();
        for(char c : s.toCharArray()) {
            if(sMap.containsKey(c)) {
                sMap.put(c, sMap.get(c) + 1);
            } else {
                sMap.put (c, 1);
            }
        }

        HashMap<Character, Integer> tMap = new HashMap<>();
        for(char c : t.toCharArray()) {
            if(tMap.containsKey(c)) {
                tMap.put(c, tMap.get(c) + 1);
            } else {
                tMap.put (c, 1);
            }
        }

        if(sMap.equals(tMap)) {
            return true;
        }
        return false;

    }
}
