class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = candidates
        self.recursion(target, [], 0)
        return self.answer


    def recursion(self, target, curr, i):
        if target == 0:
            self.answer.append(curr.copy())
        if target < 0:
            return
        for j in range(i, len(self.candidates)):
            candidate = self.candidates[j]
            curr.append(candidate)
            self.recursion(target - candidate, curr, j)
            curr.pop()
        

        