class Solution:
    # 1. To meet the first requirement, you sort it by rate so that previous worker get more money than their expectation
    # 2. To minimize the total wage, you want to keep low quality people because you do rate * quality
    #   => To do so, you use max heap
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
                    