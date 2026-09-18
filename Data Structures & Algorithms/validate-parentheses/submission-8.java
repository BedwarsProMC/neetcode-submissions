class Solution {
    public boolean isValid(String s) {
        
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('}', '{');
        brackets.put(']', '[');
        brackets.put(')', '(');

        Stack<Character> stack = new Stack<>();

        for(char current : s.toCharArray()) {
            if(brackets.containsKey(current)) {
                
                if(stack.isEmpty())
                    return false;

                char expectedBracket = brackets.get(current);
                char actualBracket = stack.pop();

                if(actualBracket != expectedBracket) {
                    return false;
                }

            } else {
                stack.push(current);
            }

        }

        return stack.isEmpty();
    }
}
