class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while(l < r) {
            // shift pointers to ignore any non alpjhanumeric characers
            while(l < r && !isAlphanumeric(s.charAt(l))) {
                l++;
            }
            while(l < r && !isAlphanumeric(s.charAt(r))) {
                r--;
            }

            if(Character.toLowerCase(s.charAt(l)) != 
                Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private boolean isAlphanumeric(char c) {
        return c >= 'a' && c <= 'z' ||
               c >= 'A' && c <= 'Z' ||
               c >= '0' && c <= '9';
    }
}
