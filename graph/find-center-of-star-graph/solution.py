class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center_a, center_b = edges[0]

        for edge in edges[1:]:
            if center_a in edge:
                return center_a
            elif center_b in edge:
                return center_b