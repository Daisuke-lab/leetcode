class Solution:
    # 0: return 0
    # 1: return dp(i+1) + dp(i+2)
    # 2:
    # if next is 0 - 6: dp(i+1) + dp(i+2)
    # if next is 7 - 9: dp(i+1)
    # 3 - 9: return dp(i+1) 

    # what is the base case
    # if it's the last character, count =1
    # if it'S the last 2 characters and it's valid count = 1 
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.memo = [-1 for i in range(len(s))]
        result =  self.dp(0)
        #print(self.memo)
        return result

    def dp(self, i):
        if i >= len(self.s):
            return 0
        if self.s[i] == "0":
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        
        result = 0
        if self.s[i] == "1":
            result += self.dp(i+1) + self.dp(i+2)
        elif self.s[i] == "2":
            if self.is_valid_as_two(i):
                result += self.dp(i+1) + self.dp(i+2)
            else:
                result += self.dp(i+1)
        else:
            result += self.dp(i+1)
        
        if self.is_valid_last_one(i):
            result += 1
        elif self.is_valid_last_two(i):
            result += 1
        self.memo[i] = result
        return result

    def is_valid_as_two(self, i):
        if i + 1 >= len(self.s):
            return False
        num = int(self.s[i] + self.s[i+1])
        if self.s[i] == "1":
            return True
        if 20 <= num and num <= 26:
            return True
        return False
    def is_valid_last_one(self, i):
        return i == len(self.s) - 1 and self.s[i] != "0"
    
    def is_valid_last_two(self, i):
        return self.is_valid_as_two(i) and i + 1 == len(self.s) -1 
        