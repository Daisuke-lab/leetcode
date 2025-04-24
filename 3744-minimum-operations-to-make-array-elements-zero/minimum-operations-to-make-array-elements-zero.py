class Solution:
    # Heap: you want to big number first
    # is cache useful?
    # you want to know if you pop only one


    def minOperations(self, queries: List[List[int]]) -> int:
        
        total_count = 0
        for query in queries:
            start, end = query
            count = 0
            prev = 1

            for d in range(1, 20):
                cur = prev * 4
                # Find the intersection between [start, end] and [prev, cur - 1]
                l = max(start, prev)
                r = min(end, cur - 1)
                if r >= l:
                    count += (r - l + 1) * d
                prev = cur
            # Since each operation can reduce two division steps, we need ceil(ops / 2) operations.
            total_count += ceil(count/2)
        return total_count
            