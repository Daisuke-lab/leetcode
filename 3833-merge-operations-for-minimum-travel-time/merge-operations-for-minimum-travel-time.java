class Solution {
     static public int minTravelTime(int l, int n, int k, int[] positions, int[] times) {
        int[] prefix = new int[n];
        prefix[0] = times[0];
        for (int idx = 1; idx < n - 1; idx++)
            prefix[idx] = prefix[idx - 1] + times[idx];
        Integer[][][] dp = new Integer[k + 1][n][n + 1];
        return (int) solve(k, 0, 0, n, positions, prefix, dp);
    }

    static private int solve(int k, int i, int last, int n, int[] positions, int[] prefix, Integer[][][] dp) {
        if (i == n - 1) {
            if (k == 0) return 0;
            return 10000000;
        }

        if (dp[k][i][last] != null) return dp[k][i][last];

        int rate = prefix[i] - (last > 0 ? prefix[last - 1] : 0), ans = 10000000;
        System.out.println(rate);
        int till = Math.min(n - 1, i + k + 1);
        for (int j = i + 1; j <= till; j++) {
            int dist = positions[j] - positions[i];
            int temp = dist * rate + solve(k - (j - i - 1), j, i + 1, n, positions, prefix, dp);
            ans = Math.min(ans, temp);
        }
        return dp[k][i][last] = ans;
    }
}