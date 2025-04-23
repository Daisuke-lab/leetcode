class Solution:
    #heap
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        print(people)
        res = []
        for person in people:
            k = person[1]
            res.insert(k, person)
        return res