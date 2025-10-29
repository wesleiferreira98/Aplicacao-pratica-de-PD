"""
Utilidades de plotagem e visualização
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import List, Dict, Any


def set_plot_style(style: str = "whitegrid"):
    """
    Configura estilo padrão dos gráficos.
    
    Args:
        style: Estilo do seaborn ('whitegrid', 'darkgrid', 'white', 'dark', 'ticks')
    """
    sns.set_theme(style=style)
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_comparison_bar(
    data: Dict[str, List[float]],
    title: str,
    xlabel: str,
    ylabel: str,
    save_path: str = None
):
    """
    Plota gráfico de barras comparativo.
    
    Args:
        data: Dicionário {categoria: [valores]}
        title: Título do gráfico
        xlabel: Rótulo do eixo X
        ylabel: Rótulo do eixo Y
        save_path: Caminho para salvar a figura (opcional)
    """
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(12, 6))
    df.plot(kind='bar', rot=45)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_line_comparison(
    data: Dict[str, List[float]],
    x_values: List[Any],
    title: str,
    xlabel: str,
    ylabel: str,
    save_path: str = None
):
    """
    Plota gráfico de linhas comparativo.
    
    Args:
        data: Dicionário {série: [valores]}
        x_values: Valores do eixo X
        title: Título do gráfico
        xlabel: Rótulo do eixo X
        ylabel: Rótulo do eixo Y
        save_path: Caminho para salvar a figura (opcional)
    """
    plt.figure(figsize=(12, 6))
    
    for label, values in data.items():
        plt.plot(x_values, values, marker='o', label=label)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
