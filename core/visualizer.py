"""
Módulo central de visualização interativa
Gera gráficos e visualizações dos resultados dos experimentos
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
from pathlib import Path


class Visualizer:
    """
    Classe para criar visualizações dos resultados de experimentos.
    """
    
    def __init__(self, output_dir: str = "results/figures"):
        """
        Args:
            output_dir: Diretório para salvar as figuras
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurações de estilo
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10
    
    def plot_execution_time_comparison(
        self,
        results: List[Dict[str, Any]],
        title: str = "Comparação de Tempo de Execução",
        save_as: Optional[str] = None
    ):
        """
        Plota comparação de tempo de execução entre algoritmos.
        
        Args:
            results: Lista de resultados dos experimentos
            title: Título do gráfico
            save_as: Nome do arquivo para salvar (opcional)
        """
        # Converter para DataFrame
        df = pd.DataFrame(results)
        df['execution_time'] = df['metrics'].apply(lambda x: x['execution_time'])
        
        # Criar gráfico
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x='test_case', y='execution_time', hue='algorithm')
        
        plt.title(title)
        plt.xlabel('Caso de Teste')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Algoritmo')
        plt.tight_layout()
        
        if save_as:
            filepath = self.output_dir / save_as
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Gráfico salvo em: {filepath}")
        
        plt.show()
    
    def plot_complexity_analysis(
        self,
        results: List[Dict[str, Any]],
        x_metric: str = 'input_size',
        y_metric: str = 'execution_time',
        title: str = "Análise de Complexidade",
        save_as: Optional[str] = None
    ):
        """
        Plota análise de complexidade (tempo vs tamanho da entrada).
        
        Args:
            results: Lista de resultados dos experimentos
            x_metric: Métrica para o eixo X
            y_metric: Métrica para o eixo Y
            title: Título do gráfico
            save_as: Nome do arquivo para salvar (opcional)
        """
        df = pd.DataFrame(results)
        
        plt.figure(figsize=(12, 6))
        
        for algorithm in df['algorithm'].unique():
            algo_data = df[df['algorithm'] == algorithm]
            
            x_values = algo_data['metrics'].apply(lambda m: m.get(x_metric, 0))
            y_values = algo_data['metrics'].apply(lambda m: m.get(y_metric, 0))
            
            plt.plot(x_values, y_values, marker='o', label=algorithm)
        
        plt.title(title)
        plt.xlabel(x_metric.replace('_', ' ').title())
        plt.ylabel(y_metric.replace('_', ' ').title())
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_as:
            filepath = self.output_dir / save_as
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Gráfico salvo em: {filepath}")
        
        plt.show()
    
    def plot_operations_heatmap(
        self,
        results: List[Dict[str, Any]],
        title: str = "Heatmap de Operações",
        save_as: Optional[str] = None
    ):
        """
        Plota heatmap de contagem de operações.
        
        Args:
            results: Lista de resultados dos experimentos
            title: Título do gráfico
            save_as: Nome do arquivo para salvar (opcional)
        """
        df = pd.DataFrame(results)
        df['operations'] = df['metrics'].apply(lambda x: x.get('operations_count', 0))
        
        # Criar matriz pivot
        pivot_data = df.pivot_table(
            values='operations',
            index='algorithm',
            columns='test_case',
            aggfunc='mean'
        )
        
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd')
        
        plt.title(title)
        plt.xlabel('Caso de Teste')
        plt.ylabel('Algoritmo')
        plt.tight_layout()
        
        if save_as:
            filepath = self.output_dir / save_as
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Gráfico salvo em: {filepath}")
        
        plt.show()
    
    def plot_memory_usage(
        self,
        results: List[Dict[str, Any]],
        title: str = "Uso de Memória",
        save_as: Optional[str] = None
    ):
        """
        Plota comparação de uso de memória.
        
        Args:
            results: Lista de resultados dos experimentos
            title: Título do gráfico
            save_as: Nome do arquivo para salvar (opcional)
        """
        df = pd.DataFrame(results)
        df['memory_usage'] = df['metrics'].apply(lambda x: x.get('memory_usage', 0))
        
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='algorithm', y='memory_usage')
        
        plt.title(title)
        plt.xlabel('Algoritmo')
        plt.ylabel('Uso de Memória (MB)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if save_as:
            filepath = self.output_dir / save_as
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Gráfico salvo em: {filepath}")
        
        plt.show()
