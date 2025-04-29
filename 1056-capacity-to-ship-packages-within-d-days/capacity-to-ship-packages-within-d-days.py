class Solution:
    # binary search from where to where
    # max(weight) to sum(weight)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        all_weights = sum(weights)
        #print(all_weights)
        min_capacity = max(weights)
        max_capacity = all_weights
        l = min_capacity
        r = max_capacity
    
        right_capacity = 0
        while l <= r:
            capacity = (l + r) // 2
            spent_days = self.get_spent_days(weights, capacity)
            if spent_days <= days:
                right_capacity = capacity
                r = capacity - 1
            else:
                l = capacity + 1
        return right_capacity

    def get_spent_days(self, weights, capacity):
        spent_days = 1
        loaded = 0
        for weight in weights:
            if loaded + weight > capacity:
                spent_days += 1
                loaded = 0
            loaded += weight
        return spent_days


                
