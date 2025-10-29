"""
Sistema de logging para experimentos
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logger(name: str, log_file: str = None, level=logging.INFO):
    """
    Configura logger para experimentos.
    
    Args:
        name: Nome do logger
        log_file: Caminho para arquivo de log (opcional)
        level: Nível de logging
        
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Formato do log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler para arquivo (se especificado)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_default_logger(experiment_name: str = None):
    """
    Retorna logger padrão para experimentos.
    
    Args:
        experiment_name: Nome do experimento (opcional)
        
    Returns:
        Logger configurado
    """
    if experiment_name:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"results/logs/{experiment_name}_{timestamp}.log"
        return setup_logger(experiment_name, log_file)
    else:
        return setup_logger("experiment")


# Alias para conveniência
def get_logger(name: str = None):
    """
    Alias para get_default_logger.
    Retorna logger configurado para o módulo especificado.
    
    Args:
        name: Nome do módulo/experimento
        
    Returns:
        Logger configurado
    """
    return get_default_logger(name)
