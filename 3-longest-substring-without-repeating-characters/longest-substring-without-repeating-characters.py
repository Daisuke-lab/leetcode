class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        deque = collections.deque()
        max_length = 0
        for c in s:
            while c in visited:
                max_length = max(max_length, len(deque))
                removing_c = deque.popleft()
                visited.remove(removing_c)
            deque.append(c)
            visited.add(c)
        max_length = max(max_length, len(deque))
        return max_length