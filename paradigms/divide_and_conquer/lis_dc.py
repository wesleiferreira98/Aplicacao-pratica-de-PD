"""
LIS (Longest Increasing Subsequence) - Divide and Conquer
TODO: Implementar versão Divide and Conquer do LIS
"""

from core.algorithm_base import AlgorithmBase

class LIS_DC(AlgorithmBase):
    def __init__(self):
        super().__init__("LIS (Divisão e Conquista)")
    
    def solve(self, arr):
        """Implementação usando solve() - chamado por run() da classe base"""
        return self._lis_algorithm(arr)

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

    def _lis_algorithm(self, arr):
        """Implementação do algoritmo LIS usando Divisão e Conquista"""
        if not arr:
            return 0
        return max(self.lis_end(arr, i) for i in range(len(arr)))

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
