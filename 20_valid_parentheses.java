class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> bracketMap = new HashMap<>();bracketMap.put(')', '(');
        bracketMap.put('}', '{');
        bracketMap.put(']', '[');

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);

            // if the char is closing bracket
            if (bracketMap.containsKey(c)){
                // get top element
                char topElement = stack.empty() ? '#' : stack.pop();

                // invalid if mapped open bracket doesnt match with top of the stack
                if (topElement != bracketMap.get(c)){
                    return false;
                }
            } else {
            // push to stack if it is opening bracket
            stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}