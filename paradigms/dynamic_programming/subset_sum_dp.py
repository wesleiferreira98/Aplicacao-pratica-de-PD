from core.algorithm_base import AlgorithmBase

class SubsetSum_DP(AlgorithmBase):
    def __init__(self):
        super().__init__("Subset Sum (PD)")
    
    def solve(self, S, T):
        """Implementação usando solve() - chamado por run() da classe base"""
        return self._subset_sum_algorithm(S, T)
    
    def _subset_sum_algorithm(self, S, T):
        """Implementação do algoritmo Subset Sum usando DP"""
        n = len(S)
        dp = [[False] * (T + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
            self.count()

        for i in range(1, n + 1):
            self.count()
            for t in range(1, T + 1):
                self.count()
                dp[i][t] = dp[i - 1][t] or (t >= S[i - 1] and dp[i - 1][t - S[i - 1]])
                self.count()

        return dp[n][T]

    def run(self, S, T):
        """Sobrescreve run para medir tempo corretamente"""
        import time
        start = time.perf_counter()
        result = self._subset_sum_algorithm(S, T)
        end = time.perf_counter()
        
        return {
            'result': result,
            'metrics': {
                'execution_time': end - start,
                'operations_count': self.metrics['operations_count'],
                'memory_usage': 0
            }
        }
