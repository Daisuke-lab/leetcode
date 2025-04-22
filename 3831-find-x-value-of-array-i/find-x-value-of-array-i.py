class Solution:
    # you might want total product
    # two pointers?
    # define what you make it remained
    # n^2
    # Math?
    # Once you find k*n, it's endless
    # (nk- m) * (pk - q) = m*q
    # k + x or x without include k
    # 
    # prefix/suffix product
    # only return count 
    # n*k
    # prefix * answer * suffix = total_product
    # if x = 0, answer must have k
    # if x = 1, 1 = total/prefix*suffix
    # you have no idea which pointer you will shift
    # 
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * k
        counts = [0] * k
            
        for num in nums:
            new_counts = [0] * k
            for i, count in enumerate(counts):
                new_counts[i * num % k] += count
                answer[i * num % k] += count
            counts = new_counts
            counts[num % k] += 1
            answer[num % k] += 1
        return answer