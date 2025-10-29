"""
Módulo para coletar métricas de desempenho
Inclui contadores de operações, tempo de execução e uso de memória
"""

import time
import psutil
import os
from typing import Optional, Dict, Any
from functools import wraps


class Metrics:
    """
    Classe para coletar e armazenar métricas de desempenho de algoritmos.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reseta todas as métricas"""
        self.start_time = None
        self.end_time = None
        self.operations_count = 0
        self.comparisons_count = 0
        self.memory_start = None
        self.memory_peak = None
        self.custom_metrics = {}
    
    def start_timing(self):
        """Inicia contagem de tempo"""
        self.start_time = time.perf_counter()
        self.memory_start = self._get_memory_usage()
    
    def stop_timing(self):
        """Para contagem de tempo"""
        self.end_time = time.perf_counter()
        self.memory_peak = self._get_memory_usage()
    
    def get_execution_time(self) -> float:
        """Retorna tempo de execução em segundos"""
        if self.start_time is None or self.end_time is None:
            return 0.0
        return self.end_time - self.start_time
    
    def get_memory_usage(self) -> Dict[str, float]:
        """Retorna uso de memória em MB"""
        return {
            'start_mb': self.memory_start if self.memory_start else 0.0,
            'peak_mb': self.memory_peak if self.memory_peak else 0.0,
            'delta_mb': (self.memory_peak - self.memory_start) if (self.memory_peak and self.memory_start) else 0.0
        }
    
    def increment_operations(self, count: int = 1):
        """Incrementa contador de operações"""
        self.operations_count += count
    
    def increment_comparisons(self, count: int = 1):
        """Incrementa contador de comparações"""
        self.comparisons_count += count
    
    def add_custom_metric(self, name: str, value: Any):
        """Adiciona métrica customizada"""
        self.custom_metrics[name] = value
    
    def get_all_metrics(self) -> Dict[str, Any]:
        """Retorna todas as métricas coletadas"""
        return {
            'execution_time_seconds': self.get_execution_time(),
            'operations_count': self.operations_count,
            'comparisons_count': self.comparisons_count,
            'memory_usage': self.get_memory_usage(),
            'custom_metrics': self.custom_metrics.copy()
        }
    
    @staticmethod
    def _get_memory_usage() -> float:
        """Retorna uso de memória do processo atual em MB"""
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # Converte para MB
    
    def __str__(self):
        metrics = self.get_all_metrics()
        return (
            f"Execution Time: {metrics['execution_time_seconds']:.6f}s\n"
            f"Operations: {metrics['operations_count']}\n"
            f"Comparisons: {metrics['comparisons_count']}\n"
            f"Memory Delta: {metrics['memory_usage']['delta_mb']:.2f} MB"
        )


def measure_performance(func):
    """
    Decorator para medir automaticamente o desempenho de uma função.
    
    Usage:
        @measure_performance
        def my_algorithm(data):
            # implementação
            pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        metrics = Metrics()
        metrics.start_timing()
        
        result = func(*args, **kwargs)
        
        metrics.stop_timing()
        
        print(f"\nPerformance metrics for {func.__name__}:")
        print(metrics)
        
        return result
    
    return wrapper
