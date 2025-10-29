"""
LIS (Longest Increasing Subsequence) - Divide and Conquer
TODO: Implementar versão Divide and Conquer do LIS
"""

from core.algorithm_base import AlgorithmBase

class LIS_DC(AlgorithmBase):
    def __init__(self):
        super().__init__("LIS (Divisão e Conquista)")

    def lis_end(self, arr, i):
        self.count()
        if i == 0:
            return 1
        best = 1
        for j in range(i):
            self.count()
            if arr[j] < arr[i]:
                cand = self.lis_end(arr, j) + 1
                self.count()
                if cand > best:
                    best = cand; self.count()
        return best

    def run(self, arr):
        if not arr:
            return 0
        return max(self.lis_end(arr, i) for i in range(len(arr)))
