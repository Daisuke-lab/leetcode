class Solution:
    # common stack question
    # when you have "*", you have 3 choices
    # back tracking => n^3

    #  keep track of * index
    #  keep track of unresolved () as well
    # for "(", you look for greater index of "*"
    # for ")", you look for smaller idnex of "*"

    # what you need
    # star_stack = [] <= indexes of stars
    # par_stack = [] <= indexes of ()

    # 1. just do normal parenthesis problem
    # 2. pop par_stack
    # 2.1 if par is ")", if star index is less than par_i, move on, otherwise, return False
    # 2.2 if par is "(", keep poppping until star idnex is greater than par_i, if found, move on. otherwise return False
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        par_stack = []
        for i in range(len(s)):
            if s[i] == "*":
                star_stack.append(i)
            elif s[i] == "(":
                par_stack.append(i)
            elif s[i] == ")":
                if par_stack and s[par_stack[-1]] == "(":
                    par_stack.pop()
                else:
                    par_stack.append(i)

        while par_stack:
            i = par_stack.pop(0)
            if s[i] == ")":
                if star_stack and star_stack[0] < i:
                    star_stack.pop(0)
                else:
                    return False
            elif s[i] == "(":
                while star_stack and i > star_stack[0]:
                    star_stack.pop(0)
                if len(star_stack) == 0:
                    return False
                star_stack.pop(0)
        return True
        