from core.algorithm_base import AlgorithmBase

class SubsetSum_DC(AlgorithmBase):
    def __init__(self):
        super().__init__("Subset Sum (Backtracking)")
    
    def solve(self, S, target):
        """Implementação usando solve() - chamado por run() da classe base"""
        return self._subset_sum_algorithm(S, target)
    
    def _subset_sum_algorithm(self, S, target):
        """Implementação do algoritmo Subset Sum usando Backtracking/D&C"""
        return self._bt(S, 0, target)

    def _bt(self, S, i, target):
        self.count()
        if target == 0:
            return True
        if i == len(S) or target < 0:
            return False
        # Escolhe ou não escolhe o elemento atual
        return self._bt(S, i + 1, target) or self._bt(S, i + 1, target - S[i])

    def run(self, S, target):
        """Sobrescreve run para medir tempo corretamente"""
        import time
        start = time.perf_counter()
        result = self._subset_sum_algorithm(S, target)
        end = time.perf_counter()
        
        return {
            'result': result,
            'metrics': {
                'execution_time': end - start,
                'operations_count': self.metrics['operations_count'],
                'memory_usage': 0
            }
        }
