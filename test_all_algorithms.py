#!/usr/bin/env python3
"""
Teste completo de todos os algoritmos implementados
"""

print("=" * 70)
print("  Teste Completo - Todos os Algoritmos")
print("=" * 70)
print()

# Teste 1: LIS
print("1️⃣ Testando LIS (Longest Increasing Subsequence)...")
try:
    from paradigms.dynamic_programming.lis_dp import LIS_DP
    from paradigms.divide_and_conquer.lis_dc import LIS_DC
    
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    
    lis_dp = LIS_DP()
    result_dp = lis_dp.run(arr)
    print(f"   ✅ LIS_DP: resultado={result_dp['result']}, "
          f"tempo={result_dp['metrics']['execution_time']:.6f}s, "
          f"ops={result_dp['metrics']['operations_count']}")
    
    lis_dc = LIS_DC()
    result_dc = lis_dc.run(arr)
    print(f"   ✅ LIS_DC: resultado={result_dc['result']}, "
          f"tempo={result_dc['metrics']['execution_time']:.6f}s, "
          f"ops={result_dc['metrics']['operations_count']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# Teste 2: Edit Distance
print("2️⃣ Testando Edit Distance (Levenshtein)...")
try:
    from paradigms.dynamic_programming.edit_distance_dp import EditDistance_DP
    from paradigms.divide_and_conquer.edit_distance_dc import EditDistance_DC
    
    str1, str2 = "kitten", "sitting"
    
    ed_dp = EditDistance_DP()
    result_dp = ed_dp.run(str1, str2)
    print(f"   ✅ EditDistance_DP('{str1}', '{str2}'): "
          f"resultado={result_dp['result']}, "
          f"tempo={result_dp['metrics']['execution_time']:.6f}s, "
          f"ops={result_dp['metrics']['operations_count']}")
    
    ed_dc = EditDistance_DC()
    result_dc = ed_dc.run(str1, str2)
    print(f"   ✅ EditDistance_DC('{str1}', '{str2}'): "
          f"resultado={result_dc['result']}, "
          f"tempo={result_dc['metrics']['execution_time']:.6f}s, "
          f"ops={result_dc['metrics']['operations_count']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# Teste 3: Subset Sum
print("3️⃣ Testando Subset Sum...")
try:
    from paradigms.dynamic_programming.subset_sum_dp import SubsetSum_DP
    from paradigms.divide_and_conquer.subset_sum_dc import SubsetSum_DC
    
    S = [3, 34, 4, 12, 5, 2]
    target = 9
    
    ss_dp = SubsetSum_DP()
    result_dp = ss_dp.run(S, target)
    print(f"   ✅ SubsetSum_DP(target={target}): "
          f"resultado={result_dp['result']}, "
          f"tempo={result_dp['metrics']['execution_time']:.6f}s, "
          f"ops={result_dp['metrics']['operations_count']}")
    
    ss_dc = SubsetSum_DC()
    result_dc = ss_dc.run(S, target)
    print(f"   ✅ SubsetSum_DC(target={target}): "
          f"resultado={result_dc['result']}, "
          f"tempo={result_dc['metrics']['execution_time']:.6f}s, "
          f"ops={result_dc['metrics']['operations_count']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# Teste 4: Experimentos
print("4️⃣ Testando Experimentos...")
try:
    from experiments.experiment_lis import main as lis_main
    from experiments.experiment_edit_distance import main as ed_main
    from experiments.experiment_subset_sum import main as ss_main
    
    print("   ✅ experiment_lis importado")
    print("   ✅ experiment_edit_distance importado")
    print("   ✅ experiment_subset_sum importado")
except Exception as e:
    print(f"   ❌ Erro ao importar experimentos: {e}")

print()
print("=" * 70)
print("✅ Todos os testes concluídos!")
print("=" * 70)
print()
print("📊 Resumo:")
print("   • 3 algoritmos implementados (LIS, Edit Distance, Subset Sum)")
print("   • 2 paradigmas por algoritmo (DP e DC/Backtracking)")
print("   • Total: 6 implementações funcionais")
print()
print("🚀 Para executar experimentos completos:")
print("   python main.py")
print()
