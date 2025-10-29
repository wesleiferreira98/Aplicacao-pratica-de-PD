"""
Geração de instâncias aleatórias para testes
"""

import random
import string
from typing import List, Tuple


class DataGenerator:
    """
    Gerador de dados para testes de algoritmos
    """
    
    @staticmethod
    def generate_random_array(size: int, min_val: int = 1, max_val: int = 100) -> List[int]:
        """
        Gera array aleatório de inteiros.
        
        Args:
            size: Tamanho do array
            min_val: Valor mínimo
            max_val: Valor máximo
            
        Returns:
            Lista de inteiros aleatórios
        """
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def generate_increasing_array(size: int, step: int = 1) -> List[int]:
        """
        Gera array crescente.
        
        Args:
            size: Tamanho do array
            step: Passo entre elementos
            
        Returns:
            Lista de inteiros crescentes
        """
        return list(range(0, size * step, step))
    
    @staticmethod
    def generate_decreasing_array(size: int, start: int = 1000) -> List[int]:
        """
        Gera array decrescente.
        
        Args:
            size: Tamanho do array
            start: Valor inicial
            
        Returns:
            Lista de inteiros decrescentes
        """
        return list(range(start, start - size, -1))
    
    @staticmethod
    def generate_random_string(length: int) -> str:
        """
        Gera string aleatória.
        
        Args:
            length: Comprimento da string
            
        Returns:
            String aleatória
        """
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    @staticmethod
    def generate_similar_strings(length: int, similarity: float = 0.8) -> Tuple[str, str]:
        """
        Gera par de strings com similaridade controlada.
        
        Args:
            length: Comprimento das strings
            similarity: Grau de similaridade (0.0 a 1.0)
            
        Returns:
            Tupla com duas strings
        """
        str1 = DataGenerator.generate_random_string(length)
        
        # Número de caracteres a manter iguais
        num_equal = int(length * similarity)
        
        # Criar str2 baseada em str1
        str2_list = list(str1)
        
        # Modificar alguns caracteres aleatoriamente
        indices_to_change = random.sample(range(length), length - num_equal)
        for idx in indices_to_change:
            str2_list[idx] = random.choice(string.ascii_lowercase)
        
        str2 = ''.join(str2_list)
        
        return str1, str2
    
    @staticmethod
    def generate_subset_sum_instance(size: int, max_val: int = 50) -> Tuple[List[int], int]:
        """
        Gera instância do problema Subset Sum.
        
        Args:
            size: Tamanho do array
            max_val: Valor máximo dos elementos
            
        Returns:
            Tupla (array, target_sum)
        """
        arr = DataGenerator.generate_random_array(size, 1, max_val)
        
        # Gerar target que é alcançável (soma de um subconjunto aleatório)
        subset_size = random.randint(1, size)
        subset = random.sample(arr, subset_size)
        target = sum(subset)
        
        return arr, target
    
    @staticmethod
    def generate_lis_instance(size: int, lis_size: int = None) -> List[int]:
        """
        Gera instância do problema LIS com tamanho de LIS conhecido.
        
        Args:
            size: Tamanho do array
            lis_size: Tamanho desejado da LIS (opcional)
            
        Returns:
            Array com LIS do tamanho especificado
        """
        if lis_size is None:
            lis_size = random.randint(size // 4, size // 2)
        
        # Gerar subsequência crescente
        lis = sorted(random.sample(range(1, size * 2), lis_size))
        
        # Adicionar elementos aleatórios
        remaining = size - lis_size
        noise = [random.randint(1, size * 2) for _ in range(remaining)]
        
        # Misturar
        result = lis + noise
        random.shuffle(result)
        
        return result
    
    @staticmethod
    def set_seed(seed: int) -> None:
        """
        Define a semente global para reprodutibilidade dos experimentos.
        """
        random.seed(seed)
