# Fundamentos Teóricos dos Algoritmos

## 📚 Programação Dinâmica

### Conceitos Fundamentais

A Programação Dinâmica (DP) é uma técnica de otimização que resolve problemas dividindo-os em subproblemas sobrepostos e armazenando suas soluções para evitar recálculos.

**Princípios:**
1. **Subestrutura ótima**: Solução ótima contém soluções ótimas dos subproblemas
2. **Subproblemas sobrepostos**: Mesmos subproblemas são resolvidos múltiplas vezes

**Abordagens:**
- **Top-down (Memoization)**: Recursão + cache
- **Bottom-up (Tabulation)**: Iterativo, preenche tabela

---

## 🔢 Longest Increasing Subsequence (LIS)

### Definição

Encontrar o tamanho da maior subsequência estritamente crescente em um array.

### Exemplo

```
Input:  [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explicação: [2, 3, 7, 101] é uma LIS
```

### Programação Dinâmica - O(n²)

**Recorrência:**
```
dp[i] = max(dp[j] + 1) para todo j < i onde arr[j] < arr[i]
dp[i] = 1 se nenhum j satisfaz a condição
```

**Pseudocódigo:**
```
LIS_DP(arr):
    n = length(arr)
    dp = [1] * n
    
    for i from 1 to n-1:
        for j from 0 to i-1:
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

**Complexidade:**
- Tempo: O(n²)
- Espaço: O(n)

### Programação Dinâmica + Busca Binária - O(n log n)

Usa array auxiliar que mantém o menor elemento final para cada tamanho de LIS.

**Complexidade:**
- Tempo: O(n log n)
- Espaço: O(n)

---

## ✏️ Edit Distance (Levenshtein Distance)

### Definição

Número mínimo de operações (inserção, remoção, substituição) para transformar uma string em outra.

### Exemplo

```
Input:  str1 = "kitten", str2 = "sitting"
Output: 3
Explicações:
1. kitten → sitten (substituir 'k' por 's')
2. sitten → sittin (substituir 'e' por 'i')
3. sittin → sitting (inserir 'g')
```

### Programação Dinâmica

**Recorrência:**

```
Se i = 0: dp[0][j] = j
Se j = 0: dp[i][0] = i

Caso contrário:
Se str1[i-1] == str2[j-1]:
    dp[i][j] = dp[i-1][j-1]
Senão:
    dp[i][j] = 1 + min(
        dp[i-1][j],      # remoção
        dp[i][j-1],      # inserção
        dp[i-1][j-1]     # substituição
    )
```

**Tabela DP:**

```
    ""  s  i  t  t  i  n  g
""   0  1  2  3  4  5  6  7
k    1  1  2  3  4  5  6  7
i    2  2  1  2  3  4  5  6
t    3  3  2  1  2  3  4  5
t    4  4  3  2  1  2  3  4
e    5  5  4  3  2  2  3  4
n    6  6  5  4  3  3  2  3
```

**Complexidade:**
- Tempo: O(m × n) onde m, n são tamanhos das strings
- Espaço: O(m × n), otimizável para O(min(m,n))

---

## 🎯 Subset Sum

### Definição

Dado um conjunto de inteiros e um valor alvo, determinar se existe um subconjunto cuja soma é igual ao alvo.

### Exemplo

```
Input:  arr = [3, 34, 4, 12, 5, 2], target = 9
Output: True
Explicação: {4, 5} soma 9
```

### Programação Dinâmica

**Recorrência:**

```
dp[i][j] = True se existe subconjunto dos primeiros i elementos 
           que soma j

Caso base:
dp[0][0] = True (conjunto vazio soma 0)
dp[0][j] = False para j > 0

Transição:
dp[i][j] = dp[i-1][j]                    # não inclui arr[i-1]
        OR dp[i-1][j-arr[i-1]]           # inclui arr[i-1]
```

**Pseudocódigo:**
```
SUBSET_SUM_DP(arr, target):
    n = length(arr)
    dp = matriz (n+1) x (target+1)
    
    dp[0][0] = True
    for j from 1 to target:
        dp[0][j] = False
    
    for i from 1 to n:
        for j from 0 to target:
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i][j] OR dp[i-1][j-arr[i-1]]
    
    return dp[n][target]
```

**Complexidade:**
- Tempo: O(n × sum)
- Espaço: O(n × sum), otimizável para O(sum)

**Observação:** É pseudo-polinomial, pois depende do valor da soma.

---

## ♟️ N-Queens (Backtracking)

### Definição

Colocar N rainhas em um tabuleiro N×N tal que nenhuma ataque outra.

### Backtracking

**Ideia:**
1. Colocar rainha linha por linha
2. Para cada linha, tentar cada coluna
3. Verificar se posição é segura
4. Se não conseguir completar, voltar (backtrack)

**Pseudocódigo:**
```
N_QUEENS(n):
    board = matriz n x n
    solutions = []
    
    SOLVE(board, row, solutions):
        if row == n:
            solutions.add(copy(board))
            return
        
        for col from 0 to n-1:
            if IS_SAFE(board, row, col):
                board[row][col] = QUEEN
                SOLVE(board, row + 1, solutions)
                board[row][col] = EMPTY  # backtrack
    
    SOLVE(board, 0, solutions)
    return solutions
```

**Complexidade:**
- Tempo: O(N!) no pior caso
- Espaço: O(N²)

---

## 📊 Comparação de Paradigmas

| Paradigma | Características | Quando usar |
|-----------|----------------|-------------|
| **DP** | Subproblemas sobrepostos, subestrutura ótima | Otimização, contagem, decisão |
| **D&C** | Divide problema, resolve independentemente, combina | Problemas divisíveis independentes |
| **Backtracking** | Busca exaustiva com poda | Encontrar todas as soluções, permutações |

---

## 🎓 Referências

1. Cormen, T. H., et al. "Introduction to Algorithms" (CLRS)
2. Kleinberg, J., & Tardos, É. "Algorithm Design"
3. Skiena, S. S. "The Algorithm Design Manual"
