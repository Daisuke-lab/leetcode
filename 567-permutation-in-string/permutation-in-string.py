class Solution:
    # create all permutation: n!
    # check all of them: n!

    # create count map of s1 O(n)
    # check s2 can fulfill of all the map O(m)
    # O(n*m)
    # 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_map = defaultdict(int)
        for c in s1:
            count_map[c] = count_map.get(c, 0) + 1
        queue = collections.deque()
        i = 0
        j = 0
        while j < len(s2):
            if s2[j] not in count_map:
                i += 1
                j += 1
                continue
            count_map[s2[j]] -= 1
            j += 1
            if len(s1) == 1:
                return True
            while j < len(s2) and s2[j] in count_map and count_map[s2[j]] > 0:
                count_map[s2[j]] -= 1
                if j - i + 1 == len(s1):
                    return True
                j += 1
            if j == len(s2):
                return False
            if s2[j] in count_map:
                while s2[i] != s2[j]:
                    count_map[s2[i]] += 1
                    i += 1
                count_map[s2[i]] += 1
                i += 1
            else:
                while i != j:
                    count_map[s2[i]] += 1
                    i += 1
        return False

                

        
            