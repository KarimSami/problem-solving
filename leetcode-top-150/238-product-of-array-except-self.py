class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length

        # Calculate left products
        left_product = 1
        for i in range(length):
            answer[i] = left_product
            left_product *= nums[i]

        # Calculate right products and final result
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


def test_product_except_self():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    actual = solution.productExceptSelf(nums)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2
    nums = [2, 3, 4, 5]
    expected = [60, 40, 30, 24]
    actual = solution.productExceptSelf(nums)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3
    nums = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    actual = solution.productExceptSelf(nums)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4
    nums = [0, 1, 2, 3]
    expected = [6, 0, 0, 0]
    actual = solution.productExceptSelf(nums)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    # Test case 5
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    actual = solution.productExceptSelf(nums)
    assert actual == expected, f"Test case 5 failed: expected {expected}, got {actual}"
    print("Test case 5 succeeded")

    print("All tests passed.")


test_product_except_self()
