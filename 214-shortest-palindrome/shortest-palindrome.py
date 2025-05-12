class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t, pali_radiuses = self.mana(s)
        #print(pali_radiuses)
        max_index = 2
        for i, radius in enumerate(pali_radiuses):
            left = i - radius
            # if left reaches 1 (# at "^#")
            if left == 1 and radius > pali_radiuses[max_index]:
                max_index = i
        max_radius = pali_radiuses[max_index]
        #print(max_radius)
        right = t[max_index + max_radius:].replace("#", "").replace("$", "")
        #print("RIGHT:", t[max_index + max_radius:])
        return right[::-1] + s 
    def mana(self, s):
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        # max radius of palindrome starting from i
        pali_radiuses = [0] * n
        center = right = 0

        # Skip the first "^#" and the last "#$", so 2 to n-2
        for i in range(2, n - 2):
            # 
            radius = 0

            # If i is a part of the previous biggest palindrome
            if i < right:
                distance = i - center
                mirror = center - distance # = center*2 - i
                radius = min(right - i, pali_radiuses[mirror])


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
                right = i + pali_radiuses[i] # or r - 1

        return t, pali_radiuses