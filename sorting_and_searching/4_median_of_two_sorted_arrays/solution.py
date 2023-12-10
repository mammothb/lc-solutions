from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

    def findMedianSortedArrays_binary_search(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        def get_kth(nums1, len_1, nums2, len_2, k):
            if len_1 == 0:
                return nums2[k - 1]
            if len_2 == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            i = min(len_1, k // 2)
            j = min(len_2, k // 2)
            if nums1[i - 1] < nums2[j - 1]:
                return get_kth(nums1[i:], len_1 - i, nums2, len_2, k - i)
            return get_kth(nums1, len_1, nums2[j:], len_2 - j, k - j)

        len1 = len(nums1)
        len2 = len(nums2)

        l = (len1 + len2 + 1) // 2
        r = (len1 + len2 + 2) // 2
        return (
            get_kth(nums1, len1, nums2, len2, l) + get_kth(nums1, len1, nums2, len2, r)
        ) / 2

    def findMedianSortedArrays_binary_search_median(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        """
        nums1: 1 2 3 4 7
        nums2: 2 3 5 6 8
        partitions:
            1 2 3 | 4 7
              2 3 | 5 6 8
        """
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = len1 + len2
        lo = 0
        hi = len1
        left = (len1 + len2 + 1) // 2
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = left - mid1
            l1 = -sys.maxsize - 1
            l2 = -sys.maxsize - 1
            r1 = sys.maxsize + 1
            r2 = sys.maxsize + 1
            if mid1 < len1:
                r1 = nums1[mid1]
            if mid2 < len2:
                r2 = nums2[mid2]
            if mid1 > 0:
                l1 = nums1[mid1 - 1]
            if mid2 > 0:
                l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1

    def findMedianSortedArrays_binary_search_pointers(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        def get_kth(nums1, start1, stop1, nums2, start2, stop2, k):
            if start1 > stop1:
                return nums2[start2 + k - 1]
            if start2 > stop2:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            mid1 = (start1 + stop1) // 2
            mid2 = (start2 + stop2) // 2
            # Looking at the left (front) partition
            if mid1 - start1 + mid2 - start2 < k - 1:
                # nums1[start1:mid1] contains the smaller numbers, can
                # safely toss them out, and decrease k value
                if nums1[mid1] < nums2[mid2]:
                    return get_kth(
                        nums1,
                        mid1 + 1,
                        stop1,
                        nums2,
                        start2,
                        stop2,
                        k - (mid1 + 1 - start1),
                    )
                return get_kth(
                    nums1,
                    start1,
                    stop1,
                    nums2,
                    mid2 + 1,
                    stop2,
                    k - (mid2 + 1 - start2),
                )
                # Looking at the back partition
            else:
                # nums2[mid2:] is larger and can be safely tossed, k remain the
                # same since it counts from the front and we threw out the back.
                if nums1[mid1] < nums2[mid2]:
                    return get_kth(nums1, start1, stop1, nums2, start2, mid2 - 1, k)
                return get_kth(nums1, start1, mid1 - 1, nums2, start2, stop2, k)

        len1 = len(nums1)
        len2 = len(nums2)
        n = len1 + len2

        l = (n + 1) // 2
        r = (n + 2) // 2
        if n % 2 == 1:
            return get_kth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, l)

        return (
            get_kth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, l)
            + get_kth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, r)
        ) / 2


print(
    Solution().findMedianSortedArrays_binary_search_pointers(
        [1, 2, 3, 4, 7], [2, 3, 5, 6, 8]
    )
)
