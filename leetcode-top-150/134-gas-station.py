class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # Initialize starting station and current gas
        start = 0
        current_gas = 0

        # Iterate through all stations
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]

            # If current_gas becomes negative, reset starting point and gas
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        return start


def test_can_complete_circuit():
    solution = Solution()

    # Test case 1: Valid circuit starting from index 3
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expected = 3
    actual = solution.canCompleteCircuit(gas, cost)
    assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    print("Test case 1 succeeded")

    # Test case 2: No valid circuit possible
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    expected = -1
    actual = solution.canCompleteCircuit(gas, cost)
    assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    print("Test case 2 succeeded")

    # Test case 3: Single station
    gas = [1]
    cost = [1]
    expected = 0
    actual = solution.canCompleteCircuit(gas, cost)
    assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    print("Test case 3 succeeded")

    # Test case 4: LeetCode example
    gas = [3, 1, 1]
    cost = [1, 2, 2]
    expected = 0
    actual = solution.canCompleteCircuit(gas, cost)
    assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    print("Test case 4 succeeded")

    print("All tests passed.")


test_can_complete_circuit()
