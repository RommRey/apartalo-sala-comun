import pytest
from apartalo.reglas import calcular_total_reserva


@pytest.mark.unitaria
def test_tarifa_base_sin_descuento():
    assert calcular_total_reserva(1, es_estudiante=False) == 70.00
    assert calcular_total_reserva(3, es_estudiante=False) == 210.00


@pytest.mark.unitaria
def test_hora_gratis_con_4_o_mas_horas():
    assert calcular_total_reserva(4, es_estudiante=False) == 210.00
    assert calcular_total_reserva(5, es_estudiante=False) == 280.00


@pytest.mark.unitaria
def test_descuento_estudiante_despues_de_hora_gratis():
    assert calcular_total_reserva(1, es_estudiante=True) == 42.00
    assert calcular_total_reserva(4, es_estudiante=True) == 126.00


@pytest.mark.unitaria
def test_entradas_invalidas_r1():
    with pytest.raises(ValueError):
        calcular_total_reserva(0, es_estudiante=False)
    with pytest.raises(ValueError):
        calcular_total_reserva(-2, es_estudiante=True)
