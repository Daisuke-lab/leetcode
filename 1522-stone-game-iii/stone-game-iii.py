class Solution:
    # it is not a good idea to just return string in dp
    # you can store both scores
    # you need current index
    # you also who is playing now
    #
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.stones = stoneValue
        self.memo = [[
            -1 for i in range(2)]
                for j in range(len(self.stones))]
        alice_score, bob_score = self.dp(0, True)
        if alice_score > bob_score:
            return "Alice"
        elif alice_score < bob_score:
            return "Bob"
        else:
            return "Tie"


    def dp(self, i, is_alice):
        if i >= len(self.stones):
            return 0, 0
        if self.memo[i][is_alice] != -1:
            return self.memo[i][is_alice]
        max_score = -float("inf")
        min_score = float("inf")
        new_points = 0
        for j in range(3):
            if i + j == len(self.stones):
                break
            new_points += self.stones[i+j]
            alice_score, bob_score = self.dp(i + j + 1, not is_alice)
            curr_score = alice_score if is_alice else bob_score
            other_score = alice_score if not is_alice else bob_score
            if curr_score + new_points > max_score:
                max_score =  curr_score + new_points
                min_score = other_score
        if is_alice:
            self.memo[i][is_alice] = (max_score, min_score)
        else:
            self.memo[i][is_alice] = min_score, max_score
        return self.memo[i][is_alice]
        