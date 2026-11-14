import pytest
from apartalo.reglas import calcular_reembolso


@pytest.mark.regresion
def test_regresion_limite_exacto_6_horas():
    """Atrapa defecto si se cambia >= 6.0 por > 6.0 en el reembolso del 100%."""
    assert calcular_reembolso(140.00, 6.0) == 140.00
