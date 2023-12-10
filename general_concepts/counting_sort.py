from typing import List


def counting_sort(array: List[int]) -> List[int]:
    max_val = max(array)
    n = len(array)
    counts = [0] * (max_val + 1)
    result = [0] * n
    # Store the counts of each unique value
    for val in array:
        counts[val] += 1
    # Compute the prefix sum
    for i in range(1, max_val + 1):
        counts[i] += counts[i - 1]
    # Iterate from the end to preserve order of equal element, stable sort
    for i in range(n - 1, -1, -1):
        counts[array[i]] -= 1
        result[counts[array[i]]] = array[i]

    return result


if __name__ == "__main__":
    print(counting_sort([2, 5, 3, 0, 2, 3, 0, 3]))
