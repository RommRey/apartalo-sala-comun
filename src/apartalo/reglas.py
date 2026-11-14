"""Reglas de negocio de Variante 5: Salas de estudio Sala Común."""


def calcular_total_reserva(horas: int, es_estudiante: bool = False) -> float:
    """Calcula el total de la reserva aplicando R1 (tarifa, hora gratis y descuento)."""
    if not isinstance(horas, int) or isinstance(horas, bool) or horas < 1:
        raise ValueError("La reserva debe ser de al menos 1 hora entera.")

    horas_cobradas = horas - 1 if horas >= 4 else horas
    subtotal = horas_cobradas * 70.0

    if es_estudiante:
        subtotal = subtotal * 0.60

    return round(subtotal, 2)


def calcular_reembolso(monto_pagado: float, horas_anticipacion: float) -> float:
    """Calcula el monto de reembolso según horas de anticipación (R2)."""
    if monto_pagado < 0 or horas_anticipacion < 0:
        raise ValueError("El monto pagado y las horas de anticipación no pueden ser negativos.")

    if horas_anticipacion >= 6.0:
        porcentaje = 1.0
    elif horas_anticipacion >= 1.0:
        porcentaje = 0.5
    else:
        porcentaje = 0.0

    return round(monto_pagado * porcentaje, 2)
