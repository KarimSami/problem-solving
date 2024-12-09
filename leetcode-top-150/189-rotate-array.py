class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


def test_rotate():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4], "Test case 1 failed"
    print("test 1 succeeded")

    # Test case 2
    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    assert nums == [3, 99, -1, -100], "Test case 2 failed"
    print("test 2 succeeded")

    # Test case 3
    nums = [1]
    solution.rotate(nums, 0)
    assert nums == [1], "Test case 3 failed"
    print("test 3 succeeded")

    # Test case 4
    nums = [1, 2]
    solution.rotate(nums, 3)
    assert nums == [2, 1], "Test case 4 failed"
    print("test 4 succeeded")

    # Test case 5
    nums = [1, 2, 3]
    solution.rotate(nums, 4)
    assert nums == [3, 1, 2], "Test case 5 failed"
    print("test 5 succeeded")

    print("All tests passed.")


test_rotate()
