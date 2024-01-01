class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num1 = list(map(int, list(num1)))
        num2 = list(map(int, list(num2)))

        n1 = len(num1)
        n2 = len(num2)

        dp = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                prod = num1[i] * num2[j]
                pos_1 = i + j
                pos_2 = i + j + 1
                prod += dp[pos_2]

                dp[pos_1] += prod // 10
                dp[pos_2] = prod % 10

        result = []
        for d in dp:
            if result or d != 0:
                result.append(str(d))
        return "".join(result) if result else "0"
