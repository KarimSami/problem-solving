class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        # first pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1] and not candy[i] > candy[i - 1]:
                candy[i] = candy[i - 1] + 1

        # second pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and not candy[i] > candy[i + 1]:
                candy[i] = candy[i + 1] + 1
        return sum(candy)


def test_candy_distribution():
    solution = Solution()

    ratings = [1, 0, 2]
    expected = 5  # 1 + 2 + 3 + 4 + 5
    actual = solution.candy(ratings)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    ratings = [1, 2, 2]
    expected = 4  # 5 + 4 + 3 + 2 + 1
    actual = solution.candy(ratings)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    ratings = [1, 1, 1, 1]
    expected = 4  # 1 + 1 + 1 + 1
    actual = solution.candy(ratings)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    ratings = [1, 3, 5, 3, 1]
    expected = 9  # 1 + 2 + 3 + 2 + 1
    actual = solution.candy(ratings)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    print("All tests passed.")


test_candy_distribution()
