"""
Tests for algorithms
TODO: Implementar testes unitários
"""

import pytest
from core.algorithm_base import AlgorithmBase


class DummyAlgorithm(AlgorithmBase):
    """Algoritmo dummy para testes"""
    
    def __init__(self):
        super().__init__("Dummy")
    
    def solve(self, x):
        return x * 2


def test_algorithm_base():
    """Testa funcionalidade básica de AlgorithmBase"""
    algo = DummyAlgorithm()
    
    result = algo.run(5)
    
    assert result['result'] == 10
    assert 'metrics' in result
    assert 'execution_time' in result['metrics']


def test_metrics_reset():
    """Testa reset de métricas"""
    algo = DummyAlgorithm()
    
    algo.run(5)
    algo.reset_metrics()
    
    assert algo.metrics['execution_time'] == 0.0
    assert algo.metrics['operations_count'] == 0


# TODO: Adicionar mais testes quando algoritmos forem implementados

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
