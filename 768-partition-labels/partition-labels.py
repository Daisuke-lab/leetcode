class Solution:
    # you can not have duplicates in other parts
    # as soon as you see different characters, you want to split the part
    # if you find the existing character, you combine.
    # => feels like stack
    # => what do you need in stack?? count and collected (set)
    # when you find a new character. => add(1, set(["a"]))
    # when you find an existing character => keep popping until curr in stack[-1][1] and increment the count.   
    # don't forget + 1
    # => we need visited (set)
    # what if "abca"

    # Union Find?? 
    def partitionLabels(self, s: str) -> List[int]:
        count_stack = []
        set_stack = []
        visited = set()
        for i in range(len(s)):
            c = s[i]
            if c in visited:
                count = 1
                joint_set = set()
                #print(set_stack)
                while c not in set_stack[-1]:
                    joint_set = joint_set | set_stack.pop()
                    count += count_stack.pop()
                count_stack[-1] += count
                set_stack[-1] = set_stack[-1] | joint_set
            else:
                visited.add(c)
                count_stack.append(1)
                set_stack.append(set([c]))
        return count_stack