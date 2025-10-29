"""
Experimento: Longest Increasing Subsequence (LIS)
Comparação entre Divisão e Conquista (DC) e Programação Dinâmica (PD)
"""

import os
import sys

# Adicionar diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from paradigms.divide_and_conquer.lis_dc import LIS_DC
from paradigms.dynamic_programming.lis_dp import LIS_DP
from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator
from utils.logger import get_logger


log = get_logger(__name__)


def dataset(n: int):
    """
    Função de dataset para o runner.
    Retorna uma tupla com o array que será passado para o algoritmo.
    """
    DataGenerator.set_seed(42)  # reprodutibilidade
    arr = DataGenerator.generate_lis_instance(n)
    log.info(f"Instância gerada para n={n}: {arr}")
    return (arr,)


def main():
    """
    Executa o experimento de comparação entre as versões DC e PD do LIS.
    """
    # Diretório de saída
    outdir = os.path.join("results", "lis")
    os.makedirs(outdir, exist_ok=True)

    # Inicializa o executor
    runner = ExperimentRunner(name="LIS", output_dir=outdir)

    # Algoritmos
    algos = [
        LIS_DC(),
        LIS_DP()
    ]

    # Tamanhos de entrada
    n_values = [5, 7, 9, 11, 13, 15]

    # Execução
    log.info("Iniciando experimento LIS...")
    runner.run_series(
        algorithms=algos,
        dataset_fn=dataset,
        param_values=n_values,
        label="LIS",
        xlabel="Tamanho do vetor (n)"
    )

    log.info("Experimento finalizado com sucesso!")


if __name__ == "__main__":
    main()
