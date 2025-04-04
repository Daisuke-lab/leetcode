class Solution:
    def checkValidString(self, s: str) -> bool:
        # 
        left_min = 0 # the number of "(" that can not eliminated when interpreting * as ")"
        left_max = 0 # the number of "(" that can not eliminated when interpreting * as "("

        # If left_max < 0, it means there are too many ")". you can not eliminate even with all "*"
        # If left_min > 0, it means there are too many "(". you can not eliminate event with all "*"

        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


        