# Design e Arquitetura do Projeto

## 🎯 Objetivo

Este projeto foi projetado para facilitar a implementação, teste e comparação de algoritmos usando diferentes paradigmas de programação.

## 🏛️ Arquitetura

### Princípios de Design

1. **Separação de Responsabilidades**: Cada módulo tem uma responsabilidade clara
2. **Extensibilidade**: Fácil adicionar novos algoritmos e experimentos
3. **Reusabilidade**: Componentes compartilhados entre diferentes algoritmos
4. **Testabilidade**: Estrutura facilita criação de testes

### Componentes Principais

#### Core (`core/`)

O módulo core fornece a infraestrutura comum para todos os algoritmos:

- **AlgorithmBase**: Classe abstrata que define a interface para algoritmos
  - Método `solve()`: Implementação específica do algoritmo
  - Método `run()`: Executa e coleta métricas automaticamente
  - Gerenciamento de métricas integrado

- **ExperimentRunner**: Gerencia execução de experimentos
  - Executa múltiplos algoritmos
  - Múltiplos casos de teste
  - Repetições para confiabilidade estatística
  - Salva resultados em JSON

- **Metrics**: Sistema de coleta de métricas
  - Tempo de execução (alta precisão)
  - Contadores de operações
  - Uso de memória
  - Métricas customizadas

- **Visualizer**: Geração de gráficos
  - Comparação de tempo de execução
  - Análise de complexidade
  - Heatmaps de operações
  - Uso de memória

#### Paradigms (`paradigms/`)

Algoritmos organizados por paradigma de programação:

```
paradigms/
├── dynamic_programming/    # Algoritmos de PD
├── divide_and_conquer/     # Algoritmos D&C
└── backtracking/           # Algoritmos de Backtracking
```

Cada algoritmo:
- Herda de `AlgorithmBase`
- Implementa método `solve()`
- Automaticamente tem suporte a métricas

#### Datasets (`datasets/`)

Geração de dados de teste:

- **DataGenerator**: Classe com métodos estáticos
  - Arrays aleatórios
  - Strings com similaridade controlada
  - Instâncias específicas para cada problema
  - Casos de teste realistas

#### Experiments (`experiments/`)

Scripts de experimentos específicos:

- Um arquivo por tipo de experimento
- Configuração de casos de teste
- Execução comparativa
- Geração de relatórios

## 🔄 Fluxo de Execução

```
1. Criar algoritmo (herda de AlgorithmBase)
   ↓
2. Criar ExperimentRunner
   ↓
3. Gerar casos de teste (DataGenerator)
   ↓
4. Executar experimentos (run_experiment)
   ↓
5. Coletar métricas (automático)
   ↓
6. Salvar resultados (JSON)
   ↓
7. Visualizar resultados (Visualizer)
```

## 📝 Como Adicionar um Novo Algoritmo

### 1. Criar classe do algoritmo

```python
from core.algorithm_base import AlgorithmBase

class MeuAlgoritmo(AlgorithmBase):
    def __init__(self):
        super().__init__("Meu Algoritmo - DP")
    
    def solve(self, *args, **kwargs):
        # Implementação
        return resultado
```

### 2. Criar experimento

```python
from core.experiment_runner import ExperimentRunner
from paradigms.meu_modulo import MeuAlgoritmo

runner = ExperimentRunner("Experimento")
algorithms = [MeuAlgoritmo()]
test_cases = [...]

results = runner.run_experiment(algorithms, test_cases)
runner.save_results()
```

### 3. Visualizar resultados

```python
from core.visualizer import Visualizer

viz = Visualizer()
viz.plot_execution_time_comparison(results)
```

## 🎨 Padrões de Código

### Nomenclatura

- Classes: PascalCase (`AlgorithmBase`)
- Funções/Métodos: snake_case (`run_experiment`)
- Constantes: UPPER_CASE (`MAX_SIZE`)
- Arquivos: snake_case (`algorithm_base.py`)

### Documentação

- Todas as classes têm docstrings
- Todos os métodos públicos têm docstrings
- Formato: Google Style Python Docstrings

### Type Hints

Usar type hints sempre que possível:

```python
def solve(self, arr: List[int]) -> int:
    ...
```

## 🧪 Testes

Estrutura de testes em `tests/`:

- Um arquivo de teste por módulo
- Usar pytest
- Testes de unidade e integração

## 📊 Formato de Resultados

Resultados salvos em JSON:

```json
{
  "experiment": "nome",
  "test_case": "caso",
  "algorithm": "algoritmo",
  "result": ...,
  "metrics": {
    "execution_time": 0.001,
    "operations_count": 100,
    ...
  }
}
```

## 🔮 Extensões Futuras

- Suporte a paralelização
- Interface web para visualização
- Comparação com complexidade teórica
- Geração automática de relatórios PDF
- Integração com Jupyter Notebooks
