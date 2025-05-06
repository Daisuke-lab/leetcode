class Solution {
    private char[][] phoneMap;
    private List<String>  answer;
    public List<String> letterCombinations(String digits) {
        phoneMap = initPhoneMap();
        answer = new ArrayList<>();
        backtrack(digits, new StringBuilder());
        return answer;
    }

    public char[][] initPhoneMap() {
        char[][] map = {
            {'0', '0', '0'},
            {'0', '0', '0'},
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'},
            {'j', 'k', 'l'},
            {'m', 'n', 'o'},
            {'p', 'q', 'r', 's'},
            {'t', 'u', 'v'},
            {'w', 'x', 'y', 'z'}
        };
        return map;
    }
    public void backtrack(String digits, StringBuilder letters) {
        if (digits.length() == 0) {
            if (letters.length() > 0) {
                answer.add(letters.toString());
            }
            return;
        }
        int num = digits.charAt(0) - '0';
        char[] chars = phoneMap[num];
        for (char c : chars) {
            letters.append(c);
            String nextDigits = digits.substring(1);
            backtrack(nextDigits, letters);
            letters.deleteCharAt(letters.length() - 1);
        }
        
    }
    
}