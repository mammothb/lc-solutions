def merge_sort(arr, start, stop):
    # Merge sort with inversion counting
    if stop - start <= 1:
        return 0
    mid = (start + stop) // 2
    count = merge_sort(arr, start, mid) + merge_sort(arr, mid, stop)

    # Merge
    l = start
    r = mid
    cache = []
    while l < mid and r < stop:
        if arr[l] <= arr[r]:
            cache.append(arr[l])
            l += 1
        else:
            cache.append(arr[r])
            count += mid - l
            r += 1
    while l < mid:
        cache.append(arr[l])
        l += 1
    while r < stop:
        cache.append(arr[r])
        r += 1
    for i, n in enumerate(cache):
        arr[start + i] = n
    return count
