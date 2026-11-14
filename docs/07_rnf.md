# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador
# 7. Requisitos no funcionales

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| #17 | Procesar 10,000 cálculos de tarifa y reembolso en menos de 1.0 segundo (superando el pico de 60 reservas/hora del domingo a las 20:00). | Externa | Desempeño | #1, #2, #5 | Prueba de carga/benchmark cronometrada con `pytest` (`time.perf_counter()`). |
| #18 | El 100 % de las entradas inválidas (horas ≤ 0, montos o anticipación negativos) lanzan `ValueError` sin producir montos erróneos. | Externa | Fiabilidad (Robustez) | #2, #6 | Pruebas de partición de equivalencia y valores frontera con entradas fuera de dominio. |
| #19 | Complejidad ciclomática ≤ 5 por función en `src/apartalo/reglas.py` y 100 % de cobertura de caminos. | Interna | Mantenibilidad | #3, #4 | Refactorización continua en cada ciclo TDD (`REFACTOR:`) y revisión estática de caminos. |

## 7.3 La que compruebo con código

* **Restricción:** #17 (RNF-01: Desempeño en hora pico)
* **Prueba:** `tests/rnf/test_rnf_desempeno.py`

## 7.4 Una por sprint

* **La que agrego a mi DoD en el Sprint 1:** **RNF-01 (#17)**, porque mide directamente el desempeño del motor de cálculo de tarifas y cancelaciones que ya está programado en este sprint y se verifica automáticamente en cada ejecución de `pytest`.
* **Las que dejo para después y por qué:** **RNF-02 (#18)** (robustez global a nivel de formularios/API) y **RNF-03 (#19)** (auditoría automatizada de complejidad en CI), porque requieren contar con la interfaz de usuario y el flujo de integración continua que se construirán en el Sprint 2.
