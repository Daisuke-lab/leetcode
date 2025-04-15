class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = sorted(candidates)
        self.recursion(target, [], 0)
        return self.answer

    def recursion(self, target, curr, i):
        if target ==  0:
            self.answer.append(curr.copy())
            return
        elif target < 0:
            return
        elif i >= len(self.candidates):
            return
        
        curr.append(self.candidates[i])
        self.recursion(target - self.candidates[i], curr, i+1)
        curr.pop()

        while i + 1 < len(self.candidates) and self.candidates[i] == self.candidates[i+1]:
            i += 1
        i += 1
        self.recursion(target, curr, i)
              
        
            
        