class Solution {
public:
    int dp[32][2][3];
    int n = 32;
    string num;
    int solve(int pos,int tight,int prev){
        if (pos == 32) {
        return 1; 
    }


    if (dp[pos][tight][prev] != -1) {
        return dp[pos][tight][prev];
    }

    int res = 0; 
    int limit = tight ? (num[pos] - '0') : 1;


    for (int digit = 0; digit <= limit; digit++) {

        if (prev == 1 && digit == 1) {
            continue;
        }


        bool next_tight = tight && (digit == limit);


        int next_prev = digit;


        res += solve(pos + 1, next_tight, next_prev);
    }


    return dp[pos][tight][prev] = res;

    }
    int findIntegers(int n) {
        memset(dp,-1,sizeof(dp));
        num = bitset<32>(n).to_string();
        return solve(0,true,2);
    }
};