#!/usr/bin/env python3
"""
Script de teste rápido para verificar se tudo está funcionando
"""

print("🧪 Testando componentes do projeto...\n")

# 1. Testar imports
print("1️⃣ Testando imports...")
try:
    from utils.logger import get_logger
    print("   ✅ utils.logger.get_logger")
except ImportError as e:
    print(f"   ❌ utils.logger.get_logger: {e}")

try:
    from core.algorithm_base import AlgorithmBase
    print("   ✅ core.algorithm_base.AlgorithmBase")
except ImportError as e:
    print(f"   ❌ core.algorithm_base.AlgorithmBase: {e}")

try:
    from core.experiment_runner import ExperimentRunner
    print("   ✅ core.experiment_runner.ExperimentRunner")
except ImportError as e:
    print(f"   ❌ core.experiment_runner.ExperimentRunner: {e}")

try:
    from paradigms.dynamic_programming.lis_dp import LIS_DP
    print("   ✅ paradigms.dynamic_programming.lis_dp.LIS_DP")
except ImportError as e:
    print(f"   ❌ paradigms.dynamic_programming.lis_dp.LIS_DP: {e}")

try:
    from paradigms.divide_and_conquer.lis_dc import LIS_DC
    print("   ✅ paradigms.divide_and_conquer.lis_dc.LIS_DC")
except ImportError as e:
    print(f"   ❌ paradigms.divide_and_conquer.lis_dc.LIS_DC: {e}")

try:
    from datasets.generators import DataGenerator
    print("   ✅ datasets.generators.DataGenerator")
except ImportError as e:
    print(f"   ❌ datasets.generators.DataGenerator: {e}")

# 2. Testar algoritmos
print("\n2️⃣ Testando algoritmos...")
try:
    from paradigms.dynamic_programming.lis_dp import LIS_DP
    from paradigms.divide_and_conquer.lis_dc import LIS_DC
    
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    
    # LIS DP
    lis_dp = LIS_DP()
    result_dp = lis_dp.run(arr)
    print(f"   ✅ LIS_DP({arr}): resultado={result_dp['result']}, tempo={result_dp['metrics']['execution_time']:.6f}s")
    
    # LIS DC
    lis_dc = LIS_DC()
    result_dc = lis_dc.run(arr)
    print(f"   ✅ LIS_DC({arr}): resultado={result_dc['result']}, tempo={result_dc['metrics']['execution_time']:.6f}s")
    
except Exception as e:
    print(f"   ❌ Erro ao testar algoritmos: {e}")
    import traceback
    traceback.print_exc()

# 3. Testar DataGenerator
print("\n3️⃣ Testando DataGenerator...")
try:
    from datasets.generators import DataGenerator
    
    DataGenerator.set_seed(42)
    arr = DataGenerator.generate_lis_instance(10)
    print(f"   ✅ generate_lis_instance(10): {arr}")
    
    arr = DataGenerator.generate_random_array(5, 1, 10)
    print(f"   ✅ generate_random_array(5, 1, 10): {arr}")
    
except Exception as e:
    print(f"   ❌ Erro ao testar DataGenerator: {e}")
    import traceback
    traceback.print_exc()

# 4. Testar ExperimentRunner
print("\n4️⃣ Testando ExperimentRunner...")
try:
    from core.experiment_runner import ExperimentRunner
    
    runner = ExperimentRunner("test", output_dir="results/test")
    print(f"   ✅ ExperimentRunner criado: {runner.name}")
    print(f"   ✅ Output dir: {runner.output_dir}")
    
    # Verificar se método run_series existe
    if hasattr(runner, 'run_series'):
        print(f"   ✅ Método run_series disponível")
    else:
        print(f"   ❌ Método run_series NÃO disponível")
    
except Exception as e:
    print(f"   ❌ Erro ao testar ExperimentRunner: {e}")
    import traceback
    traceback.print_exc()

print("\n✅ Testes concluídos!")
