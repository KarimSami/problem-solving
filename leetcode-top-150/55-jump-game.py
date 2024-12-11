class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
            if max_reachable >= len(nums) - 1:
                return True
        return False


def test_can_jump():
    solution = Solution()

    # Test case 1
    nums = [2, 3, 1, 1, 4]
    expected = True
    actual = solution.canJump(nums)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2
    nums = [3, 2, 1, 0, 4]
    expected = False
    actual = solution.canJump(nums)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3
    nums = [0]
    expected = True
    actual = solution.canJump(nums)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4
    nums = [2, 0, 0]
    expected = True
    actual = solution.canJump(nums)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    # Test case 5
    nums = [1, 2, 3]
    expected = True
    actual = solution.canJump(nums)
    assert actual == expected, f"Test case 5 failed: expected {expected}, got {actual}"
    print("Test case 5 succeeded")

    print("All tests passed.")


test_can_jump()
