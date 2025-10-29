"""
LIS (Longest Increasing Subsequence) - Dynamic Programming
TODO: Implementar versão Dynamic Programming do LIS
"""

from core.algorithm_base import AlgorithmBase

class LIS_DP(AlgorithmBase):
    def __init__(self):
        super().__init__("LIS (PD)")
    
    def solve(self, arr):
        """Implementação usando solve() - chamado por run() da classe base"""
        return self._lis_algorithm(arr)
    
    def _lis_algorithm(self, arr):
        """Implementação do algoritmo LIS usando DP"""
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

    def run(self, arr):
        """Sobrescreve run para medir tempo corretamente"""
        import time
        start = time.perf_counter()
        result = self._lis_algorithm(arr)
        end = time.perf_counter()
        
        return {
            'result': result,
            'metrics': {
                'execution_time': end - start,
                'operations_count': self.metrics['operations_count'],
                'memory_usage': 0
            }
        }
