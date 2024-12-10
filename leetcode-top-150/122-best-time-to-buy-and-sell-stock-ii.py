class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


def test_max_profit():
    solution = Solution()

    # Test case 1
    prices = [7, 1, 5, 3, 6, 4]
    expected = 7
    actual = solution.maxProfit(prices)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2
    prices = [7, 6, 4, 3, 1]
    expected = 0
    actual = solution.maxProfit(prices)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3
    prices = [1, 2, 3, 4, 5]
    expected = 4
    actual = solution.maxProfit(prices)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4
    prices = [2, 4, 1]
    expected = 2
    actual = solution.maxProfit(prices)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    # Test case 5
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    expected = 8
    actual = solution.maxProfit(prices)
    assert actual == expected, f"Test case 5 failed: expected {expected}, got {actual}"
    print("Test case 5 succeeded")

    print("All tests passed.")


test_max_profit()
