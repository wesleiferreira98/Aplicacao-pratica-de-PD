"""
Classe base abstrata para todos os algoritmos
Define a interface comum que todos os algoritmos devem implementar
"""

from abc import ABC, abstractmethod
from typing import Any, Dict
import time


class AlgorithmBase(ABC):
    """
    Classe base para todos os algoritmos implementados.
    Fornece estrutura comum para execução, métricas e comparação.
    """
    
    def __init__(self, name: str):
        """
        Args:
            name: Nome descritivo do algoritmo
        """
        self.name = name
        self.metrics = {
            'execution_time': 0.0,
            'operations_count': 0,
            'memory_usage': 0
        }
    
    @abstractmethod
    def solve(self, *args, **kwargs) -> Any:
        """
        Método principal que resolve o problema.
        Deve ser implementado por cada algoritmo específico.
        """
        pass
    
    def run(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Executa o algoritmo e coleta métricas.
        
        Returns:
            Dict com resultado e métricas de execução
        """
        start_time = time.perf_counter()
        
        result = self.solve(*args, **kwargs)
        
        end_time = time.perf_counter()
        self.metrics['execution_time'] = end_time - start_time
        
        return {
            'result': result,
            'metrics': self.metrics.copy()
        }
    
    def reset_metrics(self):
        """Reseta as métricas para nova execução"""
        self.metrics = {
            'execution_time': 0.0,
            'operations_count': 0,
            'memory_usage': 0
        }
    
    def __str__(self):
        return f"Algorithm: {self.name}"
