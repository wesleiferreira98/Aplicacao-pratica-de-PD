from core.algorithm_base import AlgorithmBase

class EditDistance_DC(AlgorithmBase):
    def __init__(self):
        super().__init__("Edit Distance (Divisão e Conquista)")
    
    def solve(self, a: str, b: str):
        """Implementação usando solve() - chamado por run() da classe base"""
        return self._edit_distance_algorithm(a, b)
    
    def _edit_distance_algorithm(self, a: str, b: str) -> int:
        """Implementação do algoritmo Edit Distance usando D&C"""
        return self._dist(a, b)

    def _dist(self, a: str, b: str) -> int:
        self.count()
        if not a:
            return len(b)
        if not b:
            return len(a)

        cost = 0 if a[-1] == b[-1] else 1
        return min(
            self._dist(a[:-1], b) + 1,      # deleção
            self._dist(a, b[:-1]) + 1,      # inserção
            self._dist(a[:-1], b[:-1]) + cost  # substituição ou match
        )

    def run(self, a: str, b: str):
        """Sobrescreve run para medir tempo corretamente"""
        import time
        start = time.perf_counter()
        result = self._edit_distance_algorithm(a, b)
        end = time.perf_counter()
        
        return {
            'result': result,
            'metrics': {
                'execution_time': end - start,
                'operations_count': self.metrics['operations_count'],
                'memory_usage': 0
            }
        }
