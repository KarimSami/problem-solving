class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_threshold = len(nums) // 2
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > majority_threshold:
                return num


def test_majorityElement():
    solution = Solution()

    # Test cases
    assert solution.majorityElement([3, 2, 3]) == 3, "Test case 1 failed"
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2, "Test case 2 failed"
    assert solution.majorityElement([1]) == 1, "Test case 3 failed"
    assert solution.majorityElement([1, 1, 2, 2, 2]) == 2, "Test case 4 failed"
    assert (
        solution.majorityElement(
            [1000000000, 1000000000, -1000000000, -1000000000, -1000000000]
        )
        == -1000000000
    ), "Test case 5 failed"

    print("All tests passed.")


test_majorityElement()
