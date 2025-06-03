class Solution:
    # you don't know how to sort it
    # you don't know how not to violate the proportional distribution of money
    
    # => You want to fix the rate by sorting (there is one person who will get the minimum wage)
    # => you want to collect min_heap such that all other workers can get more than min wage
    # ==> you have lower efficiency but you want to maximizize the efficiency in this requirements
    
    # you can not sort by rate for sure
    # 
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        min_money = float("inf")
        max_heap = []
        total_quality = 0
        workers = sorted(list(zip(quality, wage)), key=lambda worker: worker[1] / worker[0])
        for curr_quality, curr_wage in workers:
            curr_rate = curr_wage / curr_quality
            total_quality += curr_quality
            heapq.heappush(max_heap, (-curr_quality))
            if len(max_heap) == k:
                min_money = min(min_money, total_quality * curr_rate)
                total_quality += heapq.heappop(max_heap)
        return min_money
                    