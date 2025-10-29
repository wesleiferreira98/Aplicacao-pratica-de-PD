"""
Executor de experimentos padronizados
Permite executar múltiplos algoritmos com diferentes entradas e comparar resultados
"""

from typing import List, Dict, Any, Callable
import json
from datetime import datetime
from pathlib import Path

from .algorithm_base import AlgorithmBase


class ExperimentRunner:
    """
    Gerencia a execução de experimentos comparativos entre algoritmos.
    """
    
    def __init__(self, name: str, output_dir: str = "results/logs"):
        """
        Args:
            name: Nome do experimento
            output_dir: Diretório para salvar resultados
        """
        self.name = name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = []
    
    def run_experiment(
        self,
        algorithms: List[AlgorithmBase],
        test_cases: List[Dict[str, Any]],
        repetitions: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Executa experimentos com múltiplos algoritmos e casos de teste.
        
        Args:
            algorithms: Lista de algoritmos a testar
            test_cases: Lista de casos de teste (dicts com args/kwargs)
            repetitions: Número de repetições para cada caso
            
        Returns:
            Lista com resultados de todos os experimentos
        """
        self.results = []
        
        for test_case in test_cases:
            case_name = test_case.get('name', 'unnamed')
            args = test_case.get('args', [])
            kwargs = test_case.get('kwargs', {})
            
            for algorithm in algorithms:
                for rep in range(repetitions):
                    algorithm.reset_metrics()
                    
                    result_data = algorithm.run(*args, **kwargs)
                    
                    self.results.append({
                        'experiment': self.name,
                        'test_case': case_name,
                        'algorithm': algorithm.name,
                        'repetition': rep + 1,
                        'result': result_data['result'],
                        'metrics': result_data['metrics'],
                        'timestamp': datetime.now().isoformat()
                    })
        
        return self.results
    
    def save_results(self, filename: str = None):
        """
        Salva resultados em arquivo JSON.
        
        Args:
            filename: Nome do arquivo (padrão: experiment_name_timestamp.json)
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.name}_{timestamp}.json"
        
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"Resultados salvos em: {filepath}")
        return filepath
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Retorna um resumo dos resultados do experimento.
        
        Returns:
            Dict com estatísticas agregadas
        """
        if not self.results:
            return {}
        
        summary = {
            'total_runs': len(self.results),
            'algorithms': list(set(r['algorithm'] for r in self.results)),
            'test_cases': list(set(r['test_case'] for r in self.results))
        }
        
        # Métricas médias por algoritmo
        algo_stats = {}
        for algo in summary['algorithms']:
            algo_results = [r for r in self.results if r['algorithm'] == algo]
            avg_time = sum(r['metrics']['execution_time'] for r in algo_results) / len(algo_results)
            
            algo_stats[algo] = {
                'avg_execution_time': avg_time,
                'total_runs': len(algo_results)
            }
        
        summary['algorithm_stats'] = algo_stats
        
        return summary
