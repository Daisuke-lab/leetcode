class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = [nums1, nums2] if len(nums1) <= len(nums2) else [nums2, nums1]
        l = 0
        r = len(nums1) - 1
        total_length = len(nums1) + len(nums2)
        # If it's odd, you take bigger partition on left side.
        half_length = total_length // 2
        is_even = total_length % 2 == 0
                
        

        while True:
            print("-----------------------")
            m = (l + r) // 2
            print("m:", m)
            nums1_length = m + 1
            nums2_length = half_length - nums1_length
            left_partition_nums1_right_most = nums1[nums1_length-1] if nums1_length != 0 else -float("inf")
            left_partition_nums2_right_most = nums2[nums2_length-1] if nums2_length != 0 else -float("inf")
            right_partition_nums1_left_most = nums1[nums1_length] if nums1_length != len(nums1) else float("inf")
            right_partition_nums2_left_most = nums2[nums2_length] if nums2_length != len(nums2) else float("inf")
            print("left partition nums1 right_most:", left_partition_nums1_right_most)
            print("left partition nums2 right most:", left_partition_nums2_right_most)
            print("right partition nums1 left most:", right_partition_nums1_left_most)
            print("right partition nums2 left most:", right_partition_nums2_left_most)

            # nums1 partition is too big
            if left_partition_nums1_right_most > right_partition_nums2_left_most:
                r = m - 1
                continue
            # nums2 partition is too big
            elif left_partition_nums2_right_most > right_partition_nums1_left_most:
                l = m + 1
                continue
            if is_even:
                small_num = max(left_partition_nums1_right_most, left_partition_nums2_right_most)
                big_num = min(right_partition_nums1_left_most, right_partition_nums2_left_most)
                return (small_num + big_num) / 2
            else:
                return min(right_partition_nums1_left_most, right_partition_nums2_left_most)