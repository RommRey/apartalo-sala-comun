import pytest
from apartalo.reglas import calcular_reembolso


@pytest.mark.unitaria
def test_reembolso_100_con_6_horas_o_mas():
    assert calcular_reembolso(140.00, 6.0) == 140.00
    assert calcular_reembolso(140.00, 10.0) == 140.00


@pytest.mark.unitaria
def test_reembolso_50_entre_1_y_menos_de_6_horas():
    assert calcular_reembolso(140.00, 5.99) == 70.00
    assert calcular_reembolso(140.00, 1.0) == 70.00
    assert calcular_reembolso(126.00, 3.0) == 63.00


@pytest.mark.unitaria
def test_sin_reembolso_con_menos_de_1_hora():
    assert calcular_reembolso(140.00, 0.99) == 0.00
    assert calcular_reembolso(140.00, 0.0) == 0.00


@pytest.mark.unitaria
def test_entradas_invalidas_r2():
    with pytest.raises(ValueError):
        calcular_reembolso(-50.0, 2.0)
    with pytest.raises(ValueError):
        calcular_reembolso(100.0, -1.0)
