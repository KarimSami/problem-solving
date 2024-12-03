class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


def test_removeDuplicates():
    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = solution.removeDuplicates(nums)
    assert k == 5, f"Test case 1 failed: {k}"
    assert nums[:k] == [1, 1, 2, 2, 3], f"Test case 1 failed: {nums[:k]}"
    print("Test case 1 passed")

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = solution.removeDuplicates(nums)
    assert k == 7, f"Test case 2 failed: {k}"
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3], f"Test case 2 failed: {nums[:k]}"
    print("Test case 2 passed")

    nums = []
    k = solution.removeDuplicates(nums)
    assert k == 0, f"Test case 3 failed: {k}"
    assert nums[:k] == [], f"Test case 3 failed: {nums[:k]}"
    print("Test case 3 passed")

    nums = [1, 1, 1, 1]
    k = solution.removeDuplicates(nums)
    assert k == 2, f"Test case 4 failed: {k}"
    assert nums[:k] == [1, 1], f"Test case 4 failed: {nums[:k]}"
    print("Test case 4 passed")


test_removeDuplicates()

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
