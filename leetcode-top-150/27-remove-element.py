class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150


def test_removeElement():
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    assert k == 2, f"Test case 1 failed: {k}"
    assert nums[:k] == [2, 2], f"Test case 1 failed: {nums[:k]}"
    print("Test case 1 passed")

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    assert k == 5, f"Test case 2 failed: {k}"
    assert nums[:k] == [0, 1, 3, 0, 4], f"Test case 2 failed: {nums[:k]}"
    print("Test case 2 passed")

    nums = [1]
    val = 1
    k = solution.removeElement(nums, val)
    assert k == 0, f"Test case 3 failed: {k}"
    assert nums[:k] == [], f"Test case 3 failed: {nums[:k]}"
    print("Test case 3 passed")

    nums = [4, 5]
    val = 5
    k = solution.removeElement(nums, val)
    assert k == 1, f"Test case 4 failed: {k}"
    assert nums[:k] == [4], f"Test case 4 failed: {nums[:k]}"
    print("Test case 4 passed")


test_removeElement()


test_removeElement()
