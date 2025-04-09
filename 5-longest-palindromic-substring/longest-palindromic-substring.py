class Solution:
    # If you fixing the middle, it can be easy
    # n^2
    def longestPalindrome(self, s: str) -> str:
        # Make "s" to odd radius "t"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        # max radius of palindrome starting from i
        pali_radiuses = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i
            radius = 0
            #print(pali_radiuses)

            # If i is a part of the previous biggest palindrome
            # you can estimate "palindrome radius" has at least mirrored center of palindrome
            if i < right:
                radius = min(right - i, pali_radiuses[mirror])
            print(radius)
            # You don't have to divide the radius by "2"! because t has many "#" so index is double size.
            l = i - (radius + 1)
            r = i + (radius + 1)
            while t[l] == t[r]:
                radius += 1
                l -= 1
                r += 1

            pali_radiuses[i] = radius

            # Update center and right
            if i + pali_radiuses[i] > right:
                center = i
                right = i + pali_radiuses[i]

        # Find the maximum element in pali_radiuses
        max_len = max(pali_radiuses)
        center_index = pali_radiuses.index(max_len)

        # Convert back to original string indices
        start = (center_index - max_len) // 2
        return s[start: start + max_len]

                        
