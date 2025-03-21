class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Not Deque
        # stack / queue 
        # you keep adding index to queu
        # if you find bigger one, retrieve top element from stack and assign output
        # keep doing so while element in stack is smaller than current
        # append current value
        stack = []
        answer = []
        for i in range(len(temperatures)):
            answer.append(0)
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j =  stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer