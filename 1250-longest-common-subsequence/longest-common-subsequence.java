class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] grid = new int[text1.length() + 1][text2.length() + 1];
        for (int i =0; i < grid.length; i++) {
            for (int j=0; j < grid[0].length; j++) {
                if (i ==0 || j == 0) {
                    grid[i][j] = 0;
                    continue;
                }
                if (text1.charAt(i-1) == text2.charAt(j-1)) {
                    grid[i][j] = grid[i-1][j-1] + 1;
                } else {
                    grid[i][j] = Math.max(grid[i][j-1], grid[i-1][j]);
                }
            }
        }
        return grid[text1.length()][text2.length()];

    }
}