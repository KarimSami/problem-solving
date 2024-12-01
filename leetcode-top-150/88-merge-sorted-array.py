class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        ptr1 = m - 1
        ptr2 = n - 1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[last] = nums1[ptr1]
                ptr1 -= 1
            else:

                nums1[last] = nums2[ptr2]
                ptr2 -= 1
            last -= 1

        while ptr2 >= 0:
            nums1[last] = nums2[ptr2]
            ptr2 -= 1
            last -= 1


# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150


def test_merge():
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Test case 1 failed: {nums1}"

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Test case 2 failed: {nums1}"

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Test case 3 failed: {nums1}"


test_merge()
