"""
Experimento: Subset Sum
Comparação entre Backtracking (DC) e Programação Dinâmica (PD)
"""

import os
import sys

# Adicionar diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from paradigms.divide_and_conquer.subset_sum_dc import SubsetSum_DC
from paradigms.dynamic_programming.subset_sum_dp import SubsetSum_DP
from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator
from utils.logger import get_logger

log = get_logger(__name__)

def dataset(n: int):
    DataGenerator.set_seed(42)
    S, T = DataGenerator.generate_subset_sum_instance(n, max_val=50)
    log.info(f"Instância para n={n}: {S} | Target={T}")
    return (S, T)

def main():
    outdir = os.path.join("results", "subset_sum")
    os.makedirs(outdir, exist_ok=True)
    runner = ExperimentRunner(name="SubsetSum", output_dir=outdir)
    algos = [SubsetSum_DC(), SubsetSum_DP()]
    n_values = [8, 10, 12, 14, 16]  # Cuidado com n>18, o backtracking explode
    log.info("Iniciando experimento Subset Sum...")
    runner.run_series(algos, dataset, n_values, label="SubsetSum", xlabel="Tamanho do conjunto (n)")
    log.info("Experimento finalizado com sucesso!")

if __name__ == "__main__":
    main()
