from typing import List


def insertion_sort(array: List[float]) -> None:
    for i in range(1, len(array)):
        j = i
        tmp = array[i]
        while j > 0 and tmp < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = tmp


def bucket_sort(array: List[float], num_buckets: int) -> List[float]:
    max_val = max(array)
    buckets: List[List[float]] = [[] for _ in range(num_buckets)]
    result: List[float] = [0] * len(array)
    for val in array:
        buckets[int(num_buckets * val / max_val)].append(val)
    for bucket in buckets:
        insertion_sort(bucket)
    i = 0
    for bucket in buckets:
        for val in bucket:
            result[i] = val
            i += 1
    return result


if __name__ == "__main__":
    print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68], 10))
