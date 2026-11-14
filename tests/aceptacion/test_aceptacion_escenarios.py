import pytest
from apartalo.reglas import calcular_total_reserva, calcular_reembolso


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "horas,estudiante,total_esperado",
    [
        (1, "no", 70.00),
        (3, "no", 210.00),
        (4, "no", 210.00),
        (4, "si", 126.00),
        (5, "si", 168.00),
        (1, "si", 42.00),
    ],
)
def test_escenario_tarifa_reserva(horas, estudiante, total_esperado):
    # Dado que la tarifa base por hora es de 70 pesos mexicanos
    es_est = estudiante == "si"
    # Cuando reservo una sala por <horas> horas y mi condición de estudiante es <estudiante>
    total = calcular_total_reserva(horas, es_estudiante=es_est)
    # Entonces el total a pagar debe ser <total_esperado> pesos mexicanos
    assert total == total_esperado


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "pagado,horas_antes,reembolso_esperado",
    [
        (140.00, 6.0, 140.00),
        (140.00, 10.0, 140.00),
        (140.00, 5.99, 70.00),
        (140.00, 1.0, 70.00),
        (140.00, 0.99, 0.00),
        (126.00, 3.0, 63.00),
    ],
)
def test_escenario_cancelacion_reembolso(pagado, horas_antes, reembolso_esperado):
    # Dado que pagué una reserva por un monto de <pagado> pesos mexicanos
    # Cuando cancelo la reserva con <horas_antes> horas de anticipación
    reembolso = calcular_reembolso(pagado, horas_antes)
    # Entonces el reembolso debe ser de <reembolso_esperado> pesos mexicanos
    assert reembolso == reembolso_esperado
