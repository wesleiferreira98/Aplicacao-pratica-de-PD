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
    
    def run_series(
        self,
        algorithms: List[AlgorithmBase],
        dataset_fn: Callable,
        param_values: List[Any],
        label: str = "experiment",
        xlabel: str = "Input Size",
        repetitions: int = 3,
        show_plot: bool = False
    ):
        """
        Executa uma série de experimentos variando um parâmetro.
        
        Args:
            algorithms: Lista de algoritmos a testar
            dataset_fn: Função que gera dataset dado um parâmetro
            param_values: Lista de valores de parâmetro para testar
            label: Rótulo do experimento
            xlabel: Rótulo do eixo X (parâmetro variado)
            repetitions: Número de repetições por configuração
            show_plot: Se True, exibe o gráfico interativo (padrão: False)
        """
        import matplotlib.pyplot as plt
        
        self.results = []
        
        # Estrutura para armazenar tempos por algoritmo
        algo_times = {algo.name: [] for algo in algorithms}
        
        for param in param_values:
            # Gerar dataset para este parâmetro
            dataset = dataset_fn(param)
            
            for algo in algorithms:
                times = []
                
                for rep in range(repetitions):
                    algo.reset_metrics()
                    
                    # Executar algoritmo
                    result_data = algo.run(*dataset)
                    
                    times.append(result_data['metrics']['execution_time'])
                    
                    self.results.append({
                        'experiment': label,
                        'parameter': param,
                        'algorithm': algo.name,
                        'repetition': rep + 1,
                        'result': result_data['result'],
                        'metrics': result_data['metrics'],
                        'timestamp': datetime.now().isoformat()
                    })
                
                # Média dos tempos
                avg_time = sum(times) / len(times)
                algo_times[algo.name].append(avg_time)
        
        # Salvar resultados
        self.save_results()
        
        # Plotar gráfico
        import matplotlib
        if not show_plot:
            matplotlib.use('Agg')  # Backend não-interativo
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        
        for algo_name, times in algo_times.items():
            plt.plot(param_values, times, marker='o', label=algo_name)
        
        plt.xlabel(xlabel)
        plt.ylabel('Tempo de Execução (s)')
        plt.title(f'{label} - Comparação de Desempenho')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Salvar figura
        fig_path = self.output_dir / f"{label}_comparison.png"
        plt.savefig(fig_path, dpi=300, bbox_inches='tight')
        print(f"Gráfico salvo em: {fig_path}")
        
        if show_plot:
            plt.show()
        else:
            plt.close()
        
        return self.results
