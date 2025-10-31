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
    # worst_case=True força o pior caso do DC (target impossível)
    # Isso faz o backtracking explorar toda a árvore (2^n nós)
    S, T = DataGenerator.generate_subset_sum_instance(n, max_val=50, worst_case=True)
    log.info(f"Instância para n={n}: {S} | Target={T} (impossível - pior caso)")
    return (S, T)

def main():
    outdir = os.path.join("results", "subset_sum")
    os.makedirs(outdir, exist_ok=True)
    runner = ExperimentRunner(name="SubsetSum", output_dir=outdir)
    algos = [SubsetSum_DC(), SubsetSum_DP()]
    # Aumentei até n=18 para mostrar crescimento exponencial do DC
    n_values = [8, 10, 12, 14, 16, 18]
    log.info("Iniciando experimento Subset Sum (PIOR CASO - target impossível)...")
    runner.run_series(algos, dataset, n_values, label="SubsetSum", xlabel="Tamanho do conjunto (n)")
    log.info("Experimento finalizado com sucesso!")

if __name__ == "__main__":
    main()
