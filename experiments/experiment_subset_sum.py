"""
Experimento específico para Subset Sum
Compara diferentes abordagens do problema
"""

from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator


def run_subset_sum_experiment():
    """
    Executa experimento para Subset Sum
    """
    print("=== Experimento: Subset Sum ===\n")
    
    # Criar runner
    runner = ExperimentRunner("SubsetSum_Comparison")
    
    # TODO: Importar algoritmos quando implementados
    # from paradigms.dynamic_programming.subset_sum_dp import SubsetSumDynamicProgramming
    # from paradigms.divide_and_conquer.subset_sum_dc import SubsetSumDivideConquer
    
    # algorithms = [
    #     SubsetSumDynamicProgramming(),
    #     SubsetSumDivideConquer()
    # ]
    
    # Gerar casos de teste
    test_cases = []
    sizes = [10, 20, 30, 50, 100]
    
    for size in sizes:
        arr, target = DataGenerator.generate_subset_sum_instance(size, max_val=50)
        test_cases.append({
            'name': f'size{size}',
            'args': [arr, target],
            'kwargs': {}
        })
    
    print(f"Gerados {len(test_cases)} casos de teste")
    print(f"Tamanhos: {sizes}\n")
    
    # TODO: Executar experimentos quando algoritmos estiverem implementados
    print("Experimento preparado. Implemente os algoritmos para executar.")


if __name__ == "__main__":
    run_subset_sum_experiment()
