class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = [nums1, nums2] if len(nums1) <= len(nums2) else [nums2, nums1]
        total = len(nums1) + len(nums2)
        half = total // 2
        is_even = total % 2 == 0


        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            nums1_paritition_length = i + 1
            j = (half - nums1_paritition_length) - 1

            nums1left = nums1[i] if i >= 0 else float("-infinity")
            nums1right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            nums2left = nums2[j] if j >= 0 else float("-infinity")
            nums2right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if nums1left <= nums2right and nums2left <= nums1right:
                if is_even:
                    return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
                else:
                    return min(nums1right, nums2right)
                
            elif nums1left > nums2right:
                r = i - 1
            else:
                l = i + 1
        