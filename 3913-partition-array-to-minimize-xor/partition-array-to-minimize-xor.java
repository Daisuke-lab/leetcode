class Solution {
    public int minXor(int[] nums, int k) {
        dp = new Integer[nums.length+1][k+1];
        return solve(0,k,nums.length,nums);
    }
    static Integer dp[][];
    static int solve(int i, int k, int n, int a[]){
        if(k<0) return Integer.MAX_VALUE;
        if(k==0 && i<n) return Integer.MAX_VALUE;
        if(i>=n){
            if(k==0) return 0;
            return Integer.MAX_VALUE;
        }
        if(dp[i][k]!=null) return dp[i][k];
        int xor = 0;

        int ans = Integer.MAX_VALUE;
            
        for(int j=i;j<n;j++){
            xor = (xor^a[j]);

            ans = Math.min(ans, Math.max(xor,solve(j+1,k-1,n,a)));
        }

        return dp[i][k] = ans;
    }
}