class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subarrays = []
        # split by 0
        cur = []
        max_product = float('-inf')

        for num in nums:
            max_product = max(max_product, num)
            if num == 0:
                if cur:
                    subarrays.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur: subarrays.append(cur)

        for sub in subarrays:
            negs_count = sum(1 for i in sub if i < 0)
            prod = 1
            needed_negs_count = negs_count if negs_count % 2 == 0 else negs_count - 1
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > needed_negs_count:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    max_product = max(max_product, prod)
        return max_product