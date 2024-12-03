class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


def test_removeDuplicates():
    solution = Solution()

    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    assert k == 2, f"Test case 1 failed: {k}"
    assert nums[:k] == [1, 2], f"Test case 1 failed: {nums[:k]}"
    print("Test case 1 passed")

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == 5, f"Test case 2 failed: {k}"
    assert nums[:k] == [0, 1, 2, 3, 4], f"Test case 2 failed: {nums[:k]}"
    print("Test case 2 passed")

    nums = []
    k = solution.removeDuplicates(nums)
    assert k == 0, f"Test case 3 failed: {k}"
    assert nums[:k] == [], f"Test case 3 failed: {nums[:k]}"
    print("Test case 3 passed")

    nums = [1]
    k = solution.removeDuplicates(nums)
    assert k == 1, f"Test case 4 failed: {k}"
    assert nums[:k] == [1], f"Test case 4 failed: {nums[:k]}"
    print("Test case 4 passed")


test_removeDuplicates()
