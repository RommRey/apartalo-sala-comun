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
