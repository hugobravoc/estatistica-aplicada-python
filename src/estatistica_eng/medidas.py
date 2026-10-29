"""Medidas descritivas reutilizáveis."""

from collections.abc import Sequence

import numpy as np


def media_amostral(valores: Sequence[float]) -> float:
    """Retorna a média aritmética; requer pelo menos uma observação."""
    if len(valores) == 0:
        raise ValueError("A amostra não pode estar vazia")
    return float(np.mean(valores))
