class Solution:
    # Brute Force
    # try every pattern
    # nCk *n

    # DP
    # when k > 0, you have 2 choices
    # case1: change the direction
    # case2: leave it as it is
    
    # args: i , k
    # output: the max distance from 0
    # you also need state, (i, j)
    # O(n^4)
    
    # how about return (i, j)?
    # => you don't even know where you are unless you pass

    # when you want to use k?
    # => when it get closer to zero. By changing it, you could have two more distances
    # You decide which way to grow (NE, NW, SE, SW)
    # if you get S or W when you are targeting NE, you flip
    # O(n)

    def maxDistance(self, s: str, k: int) -> int:
        max_distance = 0
        max_distance = max(max_distance, self.travel(s, ["N", "E"], k))
        max_distance = max(max_distance, self.travel(s, ["N", "W"], k))
        max_distance = max(max_distance, self.travel(s, ["S", "E"], k))
        max_distance = max(max_distance, self.travel(s, ["S", "W"], k))
        return max_distance

    def travel(self, s, directions, k):
        distance = 0
        max_distance = 0
        for i in range(len(s)):
            if s[i] in directions:
                distance += 1
            else:
                if k > 0:
                    k -= 1
                    distance += 1
                else:
                    distance -= 1
            max_distance = max(max_distance, distance)
        return max_distance