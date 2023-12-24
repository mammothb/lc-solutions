def activity_selection(intervals):
    def is_overlap(interval1, interval2):
        return interval1[1] > interval2[0]

    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            if is_overlap(result[-1], interval):
                if result[-1][1] > interval[1]:
                    result.pop()
                    result.append(interval)
            else:
                result.append(interval)
    return result


def activity_selection_2(intervals):
    def is_overlap(interval1, interval2):
        return interval1[1] > interval2[0]

    intervals = sorted(intervals, key=lambda x: x[1])
    idx = 0
    result = [intervals[idx]]
    n = len(intervals)
    for i in range(1, n):
        if not is_overlap(intervals[idx], intervals[i]):
            result.append(intervals[i])
            idx = i
    return result


print(
    activity_selection_2(
        [
            (1, 4),
            (3, 5),
            (0, 6),
            (5, 7),
            (3, 8),
            (5, 9),
            (6, 10),
            (8, 11),
            (8, 12),
            (2, 13),
            (12, 14),
        ]
    )
)
