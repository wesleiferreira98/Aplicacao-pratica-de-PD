"""
Experimento: Edit Distance (Levenshtein)
Comparação entre Divisão e Conquista (DC) e Programação Dinâmica (PD)
"""

import os
import sys

# Adicionar diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from paradigms.divide_and_conquer.edit_distance_dc import EditDistance_DC
from paradigms.dynamic_programming.edit_distance_dp import EditDistance_DP
from core.experiment_runner import ExperimentRunner
from datasets.generators import DataGenerator
from utils.logger import get_logger

log = get_logger(__name__)

def dataset(n: int):
    DataGenerator.set_seed(42)
    s1, s2 = DataGenerator.generate_similar_strings(n, similarity=0.8)
    log.info(f"Instâncias para n={n}: {s1} | {s2}")
    return (s1, s2)

def main():
    outdir = os.path.join("results", "edit_distance")
    os.makedirs(outdir, exist_ok=True)
    runner = ExperimentRunner(name="EditDistance", output_dir=outdir)
    algos = [EditDistance_DC(), EditDistance_DP()]
    n_values = [2, 4, 6, 8, 10]  # cuidado, DC explode depois de ~10
    log.info("Iniciando experimento Edit Distance...")
    runner.run_series(algos, dataset, n_values, label="EditDistance", xlabel="n (comprimento das strings)")
    log.info("Experimento finalizado com sucesso!")

if __name__ == "__main__":
    main()
