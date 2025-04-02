class Solution:
    # you have to pick up gas[i] >= cost[i]
    # otherwise you can not travel
    
    # Brute Force
    # you try every possible start position and check it
    # Time Complexity is O(n^2)

    # you want starting_points = [i]
    # if you reach the positive value in the middle, you can skip to investigate the i => visited(set)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        i = 0
        starting_point = None
        tank = 0
        started = set()
        negative = set()
        while True:
            gap = gas[i] - cost[i]
            if gap < 0:
                negative.add(i)
            if len(negative) == len(cost):
                return -1

            if tank >= 0 and starting_point == i:
                return starting_point

            if starting_point is None and gap >= 0:
                if i in started:
                    return -1

                starting_point = i
                tank = 0

            if starting_point is not None:
                tank += gap

            if tank >= 0 and starting_point is not None:
                started.add(i)
            if tank < 0:
                starting_point = None
            i = i + 1 if i != len(cost) -1 else 0

                