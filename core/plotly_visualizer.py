"""
Visualizador alternativo usando Plotly para gráficos interativos
"""

import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import List, Dict, Any


class PlotlyVisualizer:
    """
    Visualizador de resultados usando Plotly para gráficos interativos
    """
    
    def __init__(self, output_dir: str = "results/figures"):
        """
        Args:
            output_dir: Diretório para salvar as figuras
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Paleta de cores moderna
        self.colors = [
            '#FF6B6B',  # Vermelho coral
            '#4ECDC4',  # Turquesa
            '#45B7D1',  # Azul claro
            '#FFA07A',  # Salmão
            '#98D8C8',  # Verde água
            '#F7DC6F',  # Amarelo ouro
            '#BB8FCE',  # Roxo
            '#85C1E2'   # Azul céu
        ]
    
    def plot_comparison_interactive(
        self,
        algo_times: Dict[str, List[float]],
        param_values: List[Any],
        label: str,
        xlabel: str,
        save_html: bool = True
    ):
        """
        Cria gráfico interativo de comparação de algoritmos
        
        Args:
            algo_times: Dicionário {algoritmo: [tempos]}
            param_values: Valores dos parâmetros
            label: Título do experimento
            xlabel: Rótulo do eixo X
            save_html: Se deve salvar em HTML (padrão: True)
        """
        fig = go.Figure()
        
        for idx, (algo_name, times) in enumerate(algo_times.items()):
            color = self.colors[idx % len(self.colors)]
            
            fig.add_trace(go.Scatter(
                x=param_values,
                y=times,
                mode='lines+markers',
                name=algo_name,
                line=dict(color=color, width=3),
                marker=dict(
                    size=10,
                    color=color,
                    line=dict(color='white', width=2)
                ),
                hovertemplate='<b>%{fullData.name}</b><br>' +
                             f'{xlabel}: %{{x}}<br>' +
                             'Tempo: %{y:.6f}s<br>' +
                             '<extra></extra>'
            ))
        
        # Layout moderno
        fig.update_layout(
            title={
                'text': f'<b>{label} - Comparação de Desempenho</b>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2c3e50'}
            },
            xaxis=dict(
                title=dict(text=f'<b>{xlabel}</b>', font=dict(size=14)),
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(128, 128, 128, 0.2)',
                showline=True,
                linewidth=2,
                linecolor='#95a5a6'
            ),
            yaxis=dict(
                title=dict(text='<b>Tempo de Execução (s)</b>', font=dict(size=14)),
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(128, 128, 128, 0.2)',
                showline=True,
                linewidth=2,
                linecolor='#95a5a6',
                type='log' if max(max(times) for times in algo_times.values()) > 1 else 'linear'
            ),
            hovermode='x unified',
            plot_bgcolor='#ffffff',
            paper_bgcolor='#f8f9fa',
            font=dict(family='Arial, sans-serif', color='#2c3e50'),
            legend=dict(
                bgcolor='rgba(248, 249, 250, 0.9)',
                bordercolor='#95a5a6',
                borderwidth=1,
                font=dict(size=12)
            ),
            width=1200,
            height=700,
            margin=dict(l=80, r=80, t=100, b=80)
        )
        
        if save_html:
            html_path = self.output_dir / f"{label}_interactive.html"
            fig.write_html(str(html_path))
            print(f"📊 Gráfico interativo salvo em: {html_path}")
        
        return fig
    
    def plot_operations_comparison(
        self,
        results: List[Dict[str, Any]],
        label: str,
        save_html: bool = True
    ):
        """
        Cria gráfico comparando número de operações
        
        Args:
            results: Lista de resultados dos experimentos
            label: Título do experimento
            save_html: Se deve salvar em HTML
        """
        import pandas as pd
        
        # Converter para DataFrame
        data = []
        for result in results:
            data.append({
                'Tamanho': result['parameter'],
                'Algoritmo': result['algorithm'],
                'Operações': result['metrics']['operations_count']
            })
        
        df = pd.DataFrame(data)
        df_grouped = df.groupby(['Tamanho', 'Algoritmo'])['Operações'].mean().reset_index()
        
        fig = go.Figure()
        
        for idx, algo in enumerate(df_grouped['Algoritmo'].unique()):
            df_algo = df_grouped[df_grouped['Algoritmo'] == algo]
            color = self.colors[idx % len(self.colors)]
            
            fig.add_trace(go.Bar(
                x=df_algo['Tamanho'],
                y=df_algo['Operações'],
                name=algo,
                marker=dict(
                    color=color,
                    line=dict(color='white', width=2)
                ),
                hovertemplate='<b>%{fullData.name}</b><br>' +
                             'Tamanho: %{x}<br>' +
                             'Operações: %{y:,.0f}<br>' +
                             '<extra></extra>'
            ))
        
        fig.update_layout(
            title={
                'text': f'<b>{label} - Comparação de Operações</b>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2c3e50'}
            },
            xaxis=dict(
                title=dict(text='<b>Tamanho da Entrada</b>', font=dict(size=14)),
                showgrid=True,
                gridcolor='rgba(128, 128, 128, 0.2)'
            ),
            yaxis=dict(
                title=dict(text='<b>Número de Operações</b>', font=dict(size=14)),
                showgrid=True,
                gridcolor='rgba(128, 128, 128, 0.2)',
                type='log'
            ),
            barmode='group',
            hovermode='x unified',
            plot_bgcolor='#ffffff',
            paper_bgcolor='#f8f9fa',
            font=dict(family='Arial, sans-serif', color='#2c3e50'),
            legend=dict(
                bgcolor='rgba(248, 249, 250, 0.9)',
                bordercolor='#95a5a6',
                borderwidth=1
            ),
            width=1200,
            height=700
        )
        
        if save_html:
            html_path = self.output_dir / f"{label}_operations.html"
            fig.write_html(str(html_path))
            print(f"📊 Gráfico de operações salvo em: {html_path}")
        
        return fig
