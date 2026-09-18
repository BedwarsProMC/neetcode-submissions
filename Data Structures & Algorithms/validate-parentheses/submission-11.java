class Solution {
    public boolean isValid(String s) {
        
        Map<Character, Character> brackets = new HashMap<>();
        brackets.put('}', '{');
        brackets.put(']', '[');
        brackets.put(')', '(');

        Stack<Character> stack = new Stack<>();

        for(char current : s.toCharArray()) {
            if(brackets.containsKey(current)) {
                
                if(!stack.isEmpty() && stack.peek() == brackets.get(current))
                    stack.pop();
                else
                    return false;

            } else {
                stack.push(current);
            }

        }

        return stack.isEmpty();
    }
}
