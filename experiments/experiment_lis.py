"""
Experimento específico para LIS (Longest Increasing Subsequence)
Compara diferentes implementações do algoritmo LIS
"""

from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator


def run_lis_experiment():
    """
    Executa experimento comparativo para LIS
    """
    print("=== Experimento: Longest Increasing Subsequence ===\n")
    
    # Criar runner
    runner = ExperimentRunner("LIS_Comparison")
    
    # TODO: Importar algoritmos quando implementados
    # from paradigms.dynamic_programming.lis_dp import LISDynamicProgramming
    # from paradigms.divide_and_conquer.lis_dc import LISDivideConquer
    
    # algorithms = [
    #     LISDynamicProgramming(),
    #     LISDivideConquer()
    # ]
    
    # Gerar casos de teste
    test_cases = []
    sizes = [10, 50, 100, 500, 1000]
    
    for size in sizes:
        arr = DataGenerator.generate_random_array(size, 1, 100)
        test_cases.append({
            'name': f'random_n{size}',
            'args': [arr],
            'kwargs': {}
        })
    
    print(f"Gerados {len(test_cases)} casos de teste")
    print(f"Tamanhos: {sizes}\n")
    
    # TODO: Executar experimentos quando algoritmos estiverem implementados
    # results = runner.run_experiment(algorithms, test_cases, repetitions=3)
    # runner.save_results()
    # summary = runner.get_summary()
    # print(summary)
    
    print("Experimento preparado. Implemente os algoritmos para executar.")


if __name__ == "__main__":
    run_lis_experiment()
