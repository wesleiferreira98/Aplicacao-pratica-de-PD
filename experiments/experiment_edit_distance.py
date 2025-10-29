"""
Experimento específico para Edit Distance
Compara desempenho com strings de diferentes tamanhos
"""

from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator


def run_edit_distance_experiment():
    """
    Executa experimento para Edit Distance
    """
    print("=== Experimento: Edit Distance ===\n")
    
    # Criar runner
    runner = ExperimentRunner("EditDistance_Analysis")
    
    # TODO: Importar algoritmo quando implementado
    # from paradigms.dynamic_programming.edit_distance_dp import EditDistanceDynamicProgramming
    # algorithms = [EditDistanceDynamicProgramming()]
    
    # Gerar casos de teste
    test_cases = []
    string_lengths = [10, 50, 100, 200, 500]
    similarities = [0.9, 0.7, 0.5, 0.3]
    
    for length in string_lengths:
        for sim in similarities:
            str1, str2 = DataGenerator.generate_similar_strings(length, sim)
            test_cases.append({
                'name': f'len{length}_sim{int(sim*100)}',
                'args': [str1, str2],
                'kwargs': {}
            })
    
    print(f"Gerados {len(test_cases)} casos de teste")
    print(f"Comprimentos: {string_lengths}")
    print(f"Similaridades: {similarities}\n")
    
    # TODO: Executar experimentos quando algoritmo estiver implementado
    print("Experimento preparado. Implemente o algoritmo para executar.")


if __name__ == "__main__":
    run_edit_distance_experiment()
