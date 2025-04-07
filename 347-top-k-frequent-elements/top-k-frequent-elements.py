class Solution:
    # Hashmap: n + nlogn
    # min Heap with size k 3n
    # 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        count_map = dict(sorted(count_map.items(), key = lambda item: item[1], reverse=True))
        answer = []
        for num, count in count_map.items():
            k -= 1
            if k >= 0:
                answer.append(num)
            if k ==0:
                return answer
            



        