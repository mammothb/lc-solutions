class Solution:
    r"""
    N(0) = 1, N(1) = 1, N(2) = 2, N(3) = 5
        1         2         3
      /   \     /   \     /   \
    N(0) N(2) N(1) N(1) N(2) N(0)
          i
       /     \
    N(i-1) N(n-i)
    """

    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for tree_size in range(2, n + 1):
            for i in range(1, tree_size + 1):
                dp[tree_size] += dp[i - 1] * dp[tree_size - i]
        return dp[-1]
