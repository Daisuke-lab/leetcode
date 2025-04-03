class Solution:
    # if you can not divide hand by groupSize => false
    # maybe need to be sorted ?? => [1,2,2,3,4,6] you want 2 in the second half
    # vi
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count_map = defaultdict(int)
        for num in hand:
            count_map[num] += 1
        #keys = sorted(list(count_map.keys()))
        count_map = dict(sorted(count_map.items()))
        for i in range(len(hand)//groupSize):
            keys = list(count_map.keys())
            prev = None
            for j in range(groupSize):
                if j >= len(keys):
                    return False
                key = keys[j]
                #print(key)
                if prev != None and prev + 1 != key:
                    return False
                prev = key
                count_map[key] -= 1
                if count_map[key] == 0:
                    del count_map[key]
        return True