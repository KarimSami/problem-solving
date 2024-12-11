class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break

        return jumps


def test_jump():
    solution = Solution()

    # Test case 1
    nums = [2, 3, 1, 1, 4]
    expected = 2
    actual = solution.jump(nums)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2
    nums = [1, 2, 1, 1, 1]
    expected = 3
    actual = solution.jump(nums)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3
    nums = [0]
    expected = 0
    actual = solution.jump(nums)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4
    nums = [1, 2, 3]
    expected = 2
    actual = solution.jump(nums)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    # Test case 5
    nums = [1, 1, 1, 1]
    expected = 3
    actual = solution.jump(nums)
    assert actual == expected, f"Test case 5 failed: expected {expected}, got {actual}"
    print("Test case 5 succeeded")

    # Edge case 1: Empty array
    nums = []
    expected = 0
    actual = solution.jump(nums)
    assert actual == expected, f"Edge case 1 failed: expected {expected}, got {actual}"
    print("Edge case 1 succeeded")

    # Edge case 2: Single element array
    nums = [0]
    expected = 0
    actual = solution.jump(nums)
    assert actual == expected, f"Edge case 2 failed: expected {expected}, got {actual}"
    print("Edge case 2 succeeded")

    # Edge case 4: Array with large numbers
    nums = [100, 1, 1, 1, 1]
    expected = 1
    actual = solution.jump(nums)
    assert actual == expected, f"Edge case 4 failed: expected {expected}, got {actual}"
    print("Edge case 4 succeeded")

    # Edge case 5: Array with increasing sequence
    nums = [1, 2, 3, 4, 5]
    expected = 3
    actual = solution.jump(nums)
    assert actual == expected, f"Edge case 5 failed: expected {expected}, got {actual}"
    print("Edge case 5 succeeded")

    print("All tests passed.")


test_jump()
