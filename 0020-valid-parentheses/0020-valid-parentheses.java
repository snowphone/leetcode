class Solution {
    public boolean isValid(String s) {
        var stk = new Stack<Character>();
        
        for(var ch : s.toCharArray()) {
            if (List.of('(', '[', '{').contains(ch)) {
                stk.add(ch);
                continue;
            }
            if (stk.isEmpty()) {
                return false;
            }
            if (stk.peek() == '(' && ch == ')') {
                stk.pop();
                continue;
            }
            if (stk.peek() == '[' && ch == ']') {
                stk.pop();
                continue;
            }
            if (stk.peek() == '{' && ch == '}') {
                stk.pop();
                continue;
            }
            return false;
        }
        return stk.empty();
    }
}
