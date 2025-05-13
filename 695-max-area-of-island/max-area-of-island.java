class Solution {
    private int[][] grid;
    private int ROW;
    private int COL;
    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        int maxArea = 0;
        ROW = this.grid.length;
        COL = this.grid[0].length;
        for (int i = 0; i < ROW; i++) {
            for (int j =0; j < COL; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(i, j);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        return maxArea;
    }

    public int dfs(int i, int j) {
        if (i < 0 || i == ROW || j < 0 || j == COL) {
            return 0;
        }
        if (grid[i][j] == 0) {
            return 0;
        }
        grid[i][j] = 0;
        int area = 1;
        area += dfs(i -1, j);
        area += dfs(i +1, j);
        area += dfs(i, j - 1);
        area += dfs(i, j + 1);
        return area;
    }
}