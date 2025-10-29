"""
LIS (Longest Increasing Subsequence) - Dynamic Programming
TODO: Implementar versão Dynamic Programming do LIS
"""

from core.algorithm_base import AlgorithmBase

class LIS_DP(AlgorithmBase):
    def __init__(self):
        super().__init__("LIS (PD)")

    def run(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            self.count()
            for j in range(i):
                self.count()
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    self.count()
        return max(dp)
