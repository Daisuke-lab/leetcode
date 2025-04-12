class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        fleet = 0
        curr_slowest_time = -float("inf")
        cars = sorted(list(zip(positions, speeds)), key= lambda car: car[0], reverse=True)
        for position, speed in cars:
            time = (target - position) / speed
            if time <= curr_slowest_time:
                continue
            else:
                curr_slowest_time = time
                fleet += 1
        return fleet
        