# Aplicação Prática de Programação Dinâmica

Projeto de estudo e comparação de algoritmos usando diferentes paradigmas de programação.

## 📋 Visão Geral

Este projeto implementa e compara algoritmos clássicos usando diferentes paradigmas:
- **Programação Dinâmica (DP)**
- **Divisão e Conquista (D&C)**
- **Backtracking**

## 🏗️ Estrutura do Projeto

```
├── core/                       # Núcleo comum de interfaces e abstrações
│   ├── algorithm_base.py       # Classe base para todos os algoritmos
│   ├── experiment_runner.py    # Executor de experimentos padronizados
│   ├── metrics.py              # Contadores, tempo, memória, etc.
│   └── visualizer.py           # Módulo central de visualização interativa
│
├── paradigms/                  # Algoritmos organizados por paradigma
│   ├── divide_and_conquer/
│   ├── dynamic_programming/
│   └── backtracking/
│
├── datasets/                   # Geração de dados de teste
│   ├── generators.py
│   └── samples/
│
├── experiments/                # Experimentos específicos
│   ├── experiment_lis.py
│   ├── experiment_edit_distance.py
│   └── experiment_subset_sum.py
│
├── results/                    # Resultados dos experimentos
│   ├── figures/
│   └── logs/
│
├── utils/                      # Utilitários
│   ├── plotting.py
│   ├── logger.py
│   └── config.yaml
│
└── docs/                       # Documentação
```

## 🚀 Como Usar

### Instalação

```bash
pip install -r requirements.txt
```

### Executar um Experimento

```bash
python experiments/experiment_lis.py
```

### Executar via Main

```bash
python main.py
```

## 📊 Algoritmos Implementados

### Programação Dinâmica
- [ ] LIS - Longest Increasing Subsequence
- [ ] Edit Distance (Levenshtein)
- [ ] Subset Sum

### Divisão e Conquista
- [ ] LIS - Longest Increasing Subsequence
- [ ] Subset Sum

### Backtracking
- [ ] N-Queens

## 📈 Métricas Coletadas

- Tempo de execução
- Número de operações
- Uso de memória
- Complexidade observada

## 🔧 Dependências

- Python 3.8+
- NumPy
- Matplotlib
- Seaborn
- Pandas
- psutil

## 📝 Licença

Veja o arquivo LICENSE para mais detalhes.

## 👥 Autores

Projeto desenvolvido para estudo de algoritmos e paradigmas de programação.
