"""
Core module - Núcleo comum de interfaces e abstrações
"""

from .algorithm_base import AlgorithmBase
from .experiment_runner import ExperimentRunner
from .metrics import Metrics
from .visualizer import Visualizer

__all__ = ['AlgorithmBase', 'ExperimentRunner', 'Metrics', 'Visualizer']
