import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element = self.list[-1]
        idx_to_remove = self.dict[val]
        self.list[idx_to_remove] = last_element
        self.dict[last_element] = idx_to_remove
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


def test_randomized_set():
    randomized_set = RandomizedSet()

    # Test case 1: Insert elements
    assert (
        randomized_set.insert(1) == True
    ), "Test case 1 failed: expected True, got False"
    assert (
        randomized_set.insert(2) == True
    ), "Test case 1 failed: expected True, got False"
    assert (
        randomized_set.insert(1) == False
    ), "Test case 1 failed: expected False, got True"
    print("Test case 1 succeeded")

    # Test case 2: Remove elements
    assert (
        randomized_set.remove(1) == True
    ), "Test case 2 failed: expected True, got False"
    assert (
        randomized_set.remove(1) == False
    ), "Test case 2 failed: expected False, got True"
    assert (
        randomized_set.remove(3) == False
    ), "Test case 2 failed: expected False, got True"
    print("Test case 2 succeeded")

    # Test case 3: Get random element
    assert (
        randomized_set.insert(3) == True
    ), "Test case 3 failed: expected True, got False"
    assert (
        randomized_set.insert(4) == True
    ), "Test case 3 failed: expected True, got False"
    random_element = randomized_set.getRandom()
    assert random_element in [
        2,
        3,
        4,
    ], f"Test case 3 failed: expected one of [2, 3, 4], got {random_element}"
    print("Test case 3 succeeded")

    # Test case 4: Edge cases
    empty_set = RandomizedSet()
    try:
        empty_set.getRandom()
        print("Test case 4 failed: expected an exception, got no exception")
    except IndexError:
        print("Test case 4 succeeded")

    print("All tests passed.")


test_randomized_set()
