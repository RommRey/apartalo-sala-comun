# 4. Refinamiento y escenarios
> Ejercicio 4 · Tema 7 · 🎩 PO y 🎩 desarrollador
> Los escenarios BDD van en la carpeta `features/`.

## 4.1 Priorización MoSCoW

* **Criterio usado:** Se asignó **Must** a las historias indispensables para operar el negocio y cumplir las reglas de negocio obligatorias del Sprint 1 (**R1**: cálculo de tarifas, hora gratis y descuento estudiantil; **R2**: reembolsos por cancelación; y consulta de disponibilidad). Se dejó en **Should** las reglas de límite operativo (**R3**: máximo 4 horas/día y cupo de 6 personas) y reportes administrativos; en **Could** las validaciones complementarias y recordatorios; y en **Won't** las épicas complejas sin definir (puertas con QR y chat).

## 4.4 Cálculo de carga máxima y división (Split)

* **Velocidades de referencia:** 21, 19 y 23 puntos[cite: 9].
* **Velocidad promedio:** $(21 + 19 + 23) / 3 = \mathbf{21\text{ puntos}}$.
* **Carga máxima por historia (1/3 de la velocidad promedio):** $21 / 3 = \mathbf{7\text{ puntos}}$.
* **Historia dividida:** La historia original de cobro integral de reservas (8 puntos, rebasaba el límite de 7 puntos) se cerró como `not planned` ("Dividida en #2, #3 y #4") y se dividió en tres historias pequeñas y estimables: cálculo de tarifa base (`HU-02`, 2 pts), promoción de 1 hora gratis en 4+ horas (`HU-03`, 3 pts) y descuento del 40 % a estudiantes (`HU-04`, 3 pts).

## 4.6 Tabla FIT — Regla R2 (Cancelación y reembolso)

| Monto pagado ($) | Horas de anticipación | Porcentaje esperado | Reembolso esperado ($) | Resultado real (`pytest`) |
| :---: | :---: | :---: | :---: | :---: |
| `140.00` | `6.0` (límite exacto) | 100 % | `140.00` | ✅ Pasó (`140.00`) |
| `140.00` | `10.0` | 100 % | `140.00` | ✅ Pasó (`140.00`) |
| `140.00` | `5.99` (límite superior 50 %) | 50 % | `70.00` | ✅ Pasó (`70.00`) |
| `140.00` | `1.0` (límite inferior 50 %) | 50 % | `70.00` | ✅ Pasó (`70.00`) |
| `140.00` | `0.99` (límite sin reembolso) | 0 % | `0.00` | ✅ Pasó (`0.00`) |
| `126.00` | `3.0` | 50 % | `63.00` | ✅ Pasó (`63.00`) |
