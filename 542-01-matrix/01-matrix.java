class Solution {
    private int[][] mat;
    private int ROW;
    private int COL;
    public int[][] updateMatrix(int[][] mat) {
        this.mat = mat;
        ROW = mat.length;
        COL = mat[0].length;
        int time = 0;
        int[][] output = new int[ROW][COL];
        Queue<Integer[]> zeros = getZeros(output);
        while (!zeros.isEmpty()) {
            int size = zeros.size();
            for (int k = 0; k < size; k++) {
                Integer[] location = zeros.poll();
                int i = location[0];
                int j = location[1];
                if (output[i][j] >= 0) {
                    continue;
                }
                output[i][j] = time;
                mat[i][j] = 0;
                int[][] directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
                for (int[] direction: directions) {
                    int newI = i + direction[0];
                    int newJ = j + direction[1];
                    if (newI < 0 || newI == ROW || newJ < 0 || newJ == COL) {
                        continue;
                    }
                    if (mat[newI][newJ] == 1) {
                        Integer[] newZero = {newI, newJ};
                        zeros.add(newZero);
                    }
                }
            }
            time++;
        }
        return output;
        
    }

    public Queue<Integer[]> getZeros(int[][] output) {
        Queue<Integer[]> zeros = new LinkedList<>();
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                output[i][j] = -1;
                if (mat[i][j] == 0) {
                    Integer[] zero = {i, j};
                    zeros.add(zero);
                }
            }
        }
        return zeros;
    }
}