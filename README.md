# Aplicação Prática de Programação Dinâmica

Projeto de estudo e comparação de algoritmos usando diferentes paradigmas de programação.

## Visão Geral

Este projeto implementa e compara algoritmos clássicos usando diferentes paradigmas:

- **Programação Dinâmica (DP)**
- **Divisão e Conquista (D&C)**
- **Backtracking**

## Estrutura do Projeto

```
├── core/                       # Núcleo comum de interfaces e abstrações
│   ├── algorithm_base.py       # Classe base para todos os algoritmos
│   ├── experiment_runner.py    # Executor de experimentos padronizados
│   ├── metrics.py              # Contadores, tempo, memória, etc.
│   └── visualizer.py           # Módulo central de visualização interativa
│
├── paradigms/                  # Algoritmos organizados por paradigma
│   ├── divide_and_conquer/
│   │   ├── lis_dc.py
│   │   └── subset_sum_dc.py
│   ├── dynamic_programming/
│   │   ├── lis_dp.py
│   │   ├── subset_sum_dp.py
│   │   └── edit_distance_dp.py
│   └── backtracking/
│       └── n_queens_bt.py
│
├── datasets/
│   ├── generators.py           # Geração de instâncias aleatórias
│   └── samples/                # Dados salvos em JSON/CSV
│
├── experiments/
│   ├── experiment_lis.py       # Benchmark específico (LIS)
│   ├── experiment_edit_distance.py
│   └── experiment_subset_sum.py
│
├── results/
│   ├── figures/                # Gráficos gerados
│   └── logs/                   # Saídas de experimentos
│
├── tests/
│   └── test_algorithms.py
│
├── docs/
│   ├── README.md
│   ├── design_overview.md      # Explicação da arquitetura
│   └── algorithm_theory.md     # Explicações matemáticas
│
├── utils/
│   ├── plotting.py
│   ├── logger.py
│   └── config.yaml
│
├── main.py
├── requirements.txt
└── LICENSE
```

## Como Usar

### Instalação

```bash
# Clone o repositório
git clone https://github.com/wesleiferreira98/Aplicacao-pratica-de-PD.git
cd Aplicacao-pratica-de-PD

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Executar

```bash
# Modo interativo
python main.py

# Executar experimento específico
python experiments/experiment_lis.py
python experiments/experiment_edit_distance.py
python experiments/experiment_subset_sum.py
```

## Algoritmos

### Programação Dinâmica

- [ ] **LIS** - Longest Increasing Subsequence
- [ ] **Edit Distance** (Levenshtein)
- [ ] **Subset Sum**

### Divisão e Conquista

- [ ] **LIS** - Longest Increasing Subsequence
- [ ] **Subset Sum**

### Backtracking

- [ ] **N-Queens**

## Métricas Coletadas

- Tempo de execução
- Número de operações
- Uso de memória
- Complexidade observada

## Dependências

- Python 3.8+
- NumPy
- Matplotlib
- Seaborn
- Pandas
- psutil
- PyYAML

## Documentação

Veja a documentação completa em [`docs/`](docs/):

- [README](docs/README.md) - Visão geral do projeto
- [Design Overview](docs/design_overview.md) - Arquitetura e padrões
- [Algorithm Theory](docs/algorithm_theory.md) - Fundamentos teóricos

## Testes

```bash
# Executar testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=. --cov-report=html
```

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

**Weslei Ferreira**

- GitHub: [@wesleiferreira98](https://github.com/wesleiferreira98)

## Agradecimentos

Projeto desenvolvido para estudo de algoritmos e paradigmas de programação.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
