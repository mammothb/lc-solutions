class Solution:
    def max_subarray(self, nums):
        n = len(nums)
        dp = [[float("-inf")] * (n + 1) for _ in range(2)]
        for i in range(n):
            dp[0][i + 1] = max(dp[0][i] + nums[i], nums[i])
            dp[1][i + 1] = max(dp[1][i], dp[0][i + 1])

        return dp[-1][-1]

    def turbulent_subarray(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        result = 0
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                dp[0][i] = dp[1][i - 1] + 1
                result = max(result, dp[0][i])
            elif nums[i - 1] > nums[i]:
                dp[1][i] = dp[0][i - 1] + 1
                result = max(result, dp[1][i])
        return result + 1

    def maxlen_positive_product(self, nums):
        n = len(nums)
        # dp[i][0] for ending with positive product
        # dp[i][1] for ending with negative product
        dp = [[0] * n for _ in range(2)]

        if nums[0] > 0:
            dp[0][0] = 1
        if nums[0] < 0:
            dp[1][0] = 1

        result = dp[0][0]
        for i in range(1, n):
            if nums[i] > 0:
                dp[0][i] = dp[0][i - 1] + 1
                if dp[1][i - 1] > 0:
                    dp[1][i] = dp[1][i - 1] + 1
            if nums[i] < 0:
                dp[1][i] = dp[0][i - 1] + 1
                if dp[1][i - 1] > 0:
                    dp[0][i] = dp[1][i - 1] + 1
            result = max(result, dp[0][i])
        return result

    def numOfSubarrays(self, arr) -> int:
        n = len(arr)
        # dp[0][i] for even
        # dp[1][i] for odd
        dp = [[0] * n for _ in range(2)]

        if arr[0] % 2 == 0:
            dp[0][0] = 1
        else:
            dp[1][0] = 1
        mod = 10**9 + 7
        for i in range(1, n):
            if arr[i] % 2 == 0:
                dp[0][i] = (dp[0][i - 1] + 1) % mod
                dp[1][i] = dp[1][i - 1]
            else:
                dp[1][i] = (dp[0][i - 1] + 1) % mod
                dp[0][i] = dp[1][i - 1]
        return sum(dp[1]) % mod


# print(Solution().max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(Solution().maxlen_positive_product([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(Solution().numOfSubarrays([1, 3, 5]))
print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
