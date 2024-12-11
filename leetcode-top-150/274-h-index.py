class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n = len(citations)
        h_index = 0

        for i in range(n):
            if citations[i] >= n - i:
                h_index = n - i
                break

        return h_index


def test_h_index():
    solution = Solution()

    # Test case 1
    citations = [3, 0, 6, 1, 5]
    expected = 3
    actual = solution.hIndex(citations)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2
    citations = [1, 3, 1]
    expected = 1
    actual = solution.hIndex(citations)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3
    citations = [0, 0, 0]
    expected = 0
    actual = solution.hIndex(citations)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4
    citations = [10, 8, 5, 4, 3]
    expected = 4
    actual = solution.hIndex(citations)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    # Test case 5
    citations = [25, 8, 5, 3, 3]
    expected = 3
    actual = solution.hIndex(citations)
    assert actual == expected, f"Test case 5 failed: expected {expected}, got {actual}"
    print("Test case 5 succeeded")

    print("All tests passed.")


test_h_index()
