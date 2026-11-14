import time
import pytest
from apartalo.reglas import calcular_total_reserva, calcular_reembolso


@pytest.mark.rnf
def test_rnf_desempeno_hora_pico():
    """Verifica que 10,000 cálculos de tarifa y reembolso tarden menos de 1.0 segundo."""
    inicio = time.perf_counter()
    for _ in range(10_000):
        total = calcular_total_reserva(4, es_estudiante=True)
        calcular_reembolso(total, 3.0)
    duracion = time.perf_counter() - inicio

    assert duracion < 1.0, f"Tardó {duracion:.4f}s (límite: 1.0s)"
