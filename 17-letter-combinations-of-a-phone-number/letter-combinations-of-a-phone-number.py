class Solution:
    # First you need map
    # the outpur is list and you can not simply append to the list, you need to modify the child result
    # So let's use top down
    #  => define another function
    #  => define answer list
    #  => pass current string as arg
    # If digits == "", it's the time to add curr to answer
    def letterCombinations(self, digits: str) -> List[str]:
        self.answer = []
        self.phone_map = [None, None, ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
        ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        self.recursion(digits, "")
        return self.answer

    def recursion(self, digits, curr):
        if digits == "" and curr != "":
            self.answer.append(curr)
            return
        if digits == "":
            return 
        digit = int(digits[0])
        chars = self.phone_map[digit]
        for c in chars:
            self.recursion(digits[1:], curr + c)      