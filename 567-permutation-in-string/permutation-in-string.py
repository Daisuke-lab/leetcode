class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # you can make a permutation of either of them
        # Time complexity is O(2n^2). one for creation and one for scan
        # every time you can create it, you can test it so it can be O(n^2)
        # *n = the length of shorter string


        # It has to be O(n).
        # you can point the initial character to start with (initiated by shorter)
        # you can check left or right (initiated by longer)
        # How should I handle duplicated values?? => you should try everthing O(n)
        # keep going to left until it meets the requirement
        # if you stuck, you can start going to right
        # the worse case is O(n^2) but slight optimization
        # I want to know the list of start line
        # I want to have hashmap of shorter string
        if len(s1) > len(s2):
            return False
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1
        queue = []
        s2_map = defaultdict(int)
        # Save length here. Otherwise when you call s1_map[new_char], it automatically insert 0 and elongate map
        s1_map_length = len(s1_map) 
        match_length = 0
        for i in range(len(s1)):
            c = s2[i]
            queue.append(c)
            s2_map[c] += 1
            if s1_map[c] == s2_map[c]:
                match_length += 1
            if match_length == s1_map_length:
                return True
        for i in range(len(s1), len(s2)):
            c = s2[i]
            removing_c = queue.pop(0)
            if s1_map[removing_c] == s2_map[removing_c]:
                match_length -=1
            s2_map[removing_c]  -= 1
            s2_map[c] += 1
            queue.append(c)
            if s1_map[c] == s2_map[c]:
                match_length += 1
            if match_length == s1_map_length:
                return True
        return False


        
            