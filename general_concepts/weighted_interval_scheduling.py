def weighted_interval_scheduling(jobs):
    def find_non_overlapping_interval(jobs, idx):
        for i in range(idx - 1, -1, -1):
            if jobs[i][1] < jobs[idx][0]:
                return i
        return -1

    def solve(jobs, idx):
        if idx < 0:
            return 0
        if idx == 0:
            return jobs[idx][2]

        next_idx = find_non_overlapping_interval(jobs, idx)
        include = jobs[idx][2] + solve(jobs, next_idx)
        exclude = solve(jobs, idx - 1)

        return max(exclude, include)

    jobs = sorted(jobs, key=lambda x: x[1])
    return solve(jobs, len(jobs) - 1)


def weighted_interval_scheduling_dp(jobs):
    def find_non_overlapping_interval(jobs, idx):
        for i in range(idx - 1, -1, -1):
            if jobs[i][1] < jobs[idx][0]:
                return i
        return -1

    def solve(jobs, idx):
        if idx < 0:
            return 0
        if idx == 0:
            return jobs[idx][2]

        next_idx = find_non_overlapping_interval(jobs, idx)
        include = jobs[idx][2] + solve(jobs, next_idx)
        exclude = solve(jobs, idx - 1)

        return max(exclude, include)

    jobs = sorted(jobs, key=lambda x: x[1])
    n = len(jobs)
    dp = [-1] * n
    dp[0] = jobs[0][2]
    for i in range(1, n):
        index = find_non_overlapping_interval(jobs, i)
        include = jobs[i][2]
        if index != -1:
            include += dp[index]
        dp[i] = max(include, dp[i - 1])
    return dp[-1]
