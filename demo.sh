#!/bin/bash
# Script de demonstração do projeto

echo "======================================================================"
echo "  Demonstração - Aplicação Prática de Programação Dinâmica"
echo "======================================================================"
echo ""

# 1. Testar imports
echo "1️⃣ Testando imports e componentes..."
python test_quick.py
echo ""

# 2. Executar experimento LIS
echo "2️⃣ Executando experimento LIS..."
python experiments/experiment_lis.py
echo ""

# 3. Mostrar resultados
echo "3️⃣ Resultados gerados:"
echo ""
echo "📊 Arquivos JSON de resultados:"
ls -lh results/lis/*.json 2>/dev/null || echo "Nenhum arquivo JSON encontrado"
echo ""
echo "📈 Gráficos gerados:"
ls -lh results/lis/*.png 2>/dev/null || echo "Nenhum gráfico encontrado"
echo ""

# 4. Resumo
echo "======================================================================"
echo "✅ Demonstração concluída!"
echo ""
echo "Para executar o menu interativo:"
echo "  python main.py"
echo ""
echo "Para visualizar o gráfico:"
echo "  xdg-open results/lis/LIS_comparison.png"
echo "======================================================================"
