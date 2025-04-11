class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        common_prefix = ""
        while True:
            curr_prefix = None
            for s in strs:
                if len(s) == i:
                    return common_prefix
                if curr_prefix is None:
                    curr_prefix = s[i]
                elif curr_prefix != s[i]:
                    return common_prefix
            common_prefix += curr_prefix
            i += 1
        return common_prefix
        