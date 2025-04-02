class Solution:
    # you have to pick up gas[i] >= cost[i]
    # otherwise you can not travel
    
    # Brute Force
    # you try every possible start position and check it
    # Time Complexity is O(n^2)

    # you want starting_points = [i]
    # if you reach the positive value in the middle, you can skip to investigate the i => visited(set)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gaps = []
        starting_points = []
        visited = set()
        for i in range(len(gas)):
            gap = gas[i] - cost[i]
            gaps.append(gap)
            if gap >= 0:
                starting_points.append(i)

        for starting_point in starting_points:
            if starting_point in visited:
                continue
            tank = gaps[starting_point]
            i = starting_point
            while True:
                i = i + 1 if i != len(gaps) -1 else 0
                tank += gaps[i]
                if gaps[i] >= 0:
                    visited.add(i)
                if tank < 0:
                    break
                if i == starting_point:
                    return starting_point
        return -1
                