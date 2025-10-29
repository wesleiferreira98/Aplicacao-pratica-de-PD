#!/usr/bin/env python3
"""
Aplicação Prática de Programação Dinâmica
Implementação e comparação de algoritmos usando diferentes paradigmas
"""

import sys
from pathlib import Path


def print_banner():
    """Exibe banner do projeto"""
    print("=" * 70)
    print("  Aplicação Prática de Programação Dinâmica")
    print("  Comparação de Paradigmas: DP, Divide & Conquer, Backtracking")
    print("=" * 70)
    print()


def show_menu():
    """Exibe menu principal"""
    print("\n📋 Menu Principal:")
    print("1. Experimento: LIS (Longest Increasing Subsequence)")
    print("2. Experimento: Edit Distance")
    print("3. Experimento: Subset Sum")
    print("4. Executar todos os experimentos")
    print("5. Visualizar resultados salvos")
    print("6. Sobre o projeto")
    print("0. Sair")
    print()


def run_lis_experiment():
    """Executa experimento LIS"""
    from experiments.experiment_lis import run_lis_experiment
    run_lis_experiment()


def run_edit_distance_experiment():
    """Executa experimento Edit Distance"""
    from experiments.experiment_edit_distance import run_edit_distance_experiment
    run_edit_distance_experiment()


def run_subset_sum_experiment():
    """Executa experimento Subset Sum"""
    from experiments.experiment_subset_sum import run_subset_sum_experiment
    run_subset_sum_experiment()


def run_all_experiments():
    """Executa todos os experimentos"""
    print("\n🚀 Executando todos os experimentos...\n")
    run_lis_experiment()
    print("\n" + "-" * 70 + "\n")
    run_edit_distance_experiment()
    print("\n" + "-" * 70 + "\n")
    run_subset_sum_experiment()


def show_results():
    """Mostra resultados salvos"""
    results_dir = Path("results/logs")
    
    if not results_dir.exists():
        print("\n⚠️  Nenhum resultado encontrado.")
        return
    
    results = list(results_dir.glob("*.json"))
    
    if not results:
        print("\n⚠️  Nenhum resultado salvo ainda.")
        return
    
    print("\n📊 Resultados disponíveis:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result.name}")


def show_about():
    """Exibe informações sobre o projeto"""
    print("\n" + "=" * 70)
    print("📖 Sobre o Projeto")
    print("=" * 70)
    print("""
Este projeto implementa e compara algoritmos clássicos usando diferentes
paradigmas de programação:

🔹 Programação Dinâmica (DP)
  - Otimização através de subproblemas sobrepostos
  - Técnicas: memoization e tabulation

🔹 Divisão e Conquista (D&C)
  - Divide problema, resolve e combina soluções
  - Útil para problemas divisíveis independentes

🔹 Backtracking
  - Busca exaustiva com poda inteligente
  - Encontra todas as soluções possíveis

📊 Algoritmos Implementados:
  - LIS (Longest Increasing Subsequence)
  - Edit Distance (Levenshtein)
  - Subset Sum
  - N-Queens

🎯 Recursos:
  - Coleta automática de métricas (tempo, operações, memória)
  - Geração de visualizações comparativas
  - Experimentos reproduzíveis
  - Documentação detalhada

📁 Estrutura modular e extensível para fácil adição de novos algoritmos.

Para mais informações, veja a documentação em docs/
    """)
    print("=" * 70)


def main():
    """Função principal"""
    print_banner()
    
    while True:
        show_menu()
        
        try:
            choice = input("Escolha uma opção: ").strip()
            
            if choice == "0":
                print("\n👋 Até logo!")
                sys.exit(0)
            
            elif choice == "1":
                run_lis_experiment()
            
            elif choice == "2":
                run_edit_distance_experiment()
            
            elif choice == "3":
                run_subset_sum_experiment()
            
            elif choice == "4":
                run_all_experiments()
            
            elif choice == "5":
                show_results()
            
            elif choice == "6":
                show_about()
            
            else:
                print("\n❌ Opção inválida! Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            sys.exit(0)
        
        except Exception as e:
            print(f"\n❌ Erro: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
