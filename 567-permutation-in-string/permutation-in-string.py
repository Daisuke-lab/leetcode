class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_map = {}
        for c in s1:
            count_map[c] = count_map.get(c, 0) + 1
        i = j = 0
        while j < len(s2):
            c = s2[j]
            if c in count_map and count_map[c] > 0:
                count_map[c] -= 1
                if j - i + 1 == len(s1):
                    return True
                j += 1
            elif c in count_map:
                removing_c = s2[i]
                count_map[removing_c] += 1
                i += 1
            else:
                while i < j:
                    removing_c = s2[i]
                    count_map[removing_c] += 1
                    i += 1
                j += 1
                i = j
            
        return False
                
                

        
            