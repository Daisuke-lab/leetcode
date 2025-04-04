class Solution:
    # you can not choose any tripet bigger than target
    # DP? => 2^n
    # you also have to find the target number for any tricket
    # it's harmless to choose tricket that is all smaller than target
    # 
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr_triplet = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                curr_triplet = [max(curr_triplet[0], triplet[0]), max(curr_triplet[1], triplet[1]), max(curr_triplet[2], triplet[2])]
            if curr_triplet[0] == target[0] and curr_triplet[1] == target[1] and curr_triplet[2] == target[2]:
                return True
        return False