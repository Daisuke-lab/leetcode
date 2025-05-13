class Solution {
    private char[][] board;
    private int ROW;
    private int COL;
    
    public boolean exist(char[][] board, String word) {
        this.board = board;
        ROW = board.length;
        COL = board[0].length;
        boolean[][] path = new boolean[ROW][COL];
        for (int i=0; i < ROW; i++) {
            for (int j=0; j < COL; j++) {
                if (dfs(i, j, word, path)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(int i, int j, String word, boolean[][] path) {
        if (word.isEmpty()) {
            return true;
        }
        if (i < 0 || i == ROW || j < 0 || j == COL) {
            return false;
        }
        if (path[i][j]) {
            return false;
        }
        char desiredC = word.charAt(0);
        char c = board[i][j];
        if (c == desiredC) {
            String newWord = word.substring(1);
            path[i][j] = true;
            int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
            for (int[] direction: directions) {
                int newI = i + direction[0];
                int newJ = j + direction[1];
                if (dfs(newI, newJ, newWord, path)) {
                    return true;
                }
            }
            path[i][j] = false;            
        }
        return false;
    }
}