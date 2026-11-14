# 5. Sprint 1 (27 oct – 9 nov 2026)
> Ejercicio 5 · Temas 4 y 11

# 5. El Sprint 1

## A. Planeación del sprint

### 1. Objetivo del sprint
Entregar el motor funcional de cálculo de tarifas (con promoción por bloques y descuento estudiantil) y las reglas de reembolso por cancelación para Sala Común, validados con pruebas automatizadas.

### 2. Capacidad en horas
* **Duración del sprint:** 2 semanas (10 días hábiles, del 27 de octubre al 9 de noviembre de 2026).
* **Tiempo disponible bruto:** 3 horas diarias × 10 días = **30 horas**.
* **Descuento por otras actividades (clases universitarias, trabajo, tareas y ceremonias):** 8 horas.
* **Tiempo neto disponible:** $30 - 8 = \mathbf{22\text{ horas}}$.
* **Capacidad efectiva (dividida entre dos por factor de enfoque e imprevistos):** $22 / 2 = \mathbf{11\text{ horas efectivas}}$ (equivalente a una velocidad de referencia de **21 puntos**).

### 3. Compromiso
Se comprometen las **8 historias Must** (`HU-01` a `HU-08`) que cubren completamente **R1**, **R2** y la consulta de disponibilidad:
* **Total de puntos comprometidos:** **21 puntos** (coincide con el promedio histórico de velocidad de referencia de 21, 19 y 23 puntos).
* **Carga máxima por historia:** Ninguna historia seleccionada rebasa el límite máximo de **7 puntos** (la mayor es de 3 puntos).

### 4. Definición de Terminado (DoD)
Una historia se considera **Terminada** únicamente cuando cumple estos 5 puntos:
1. El código está implementado en `src/apartalo/reglas.py` siguiendo el ciclo TDD (`ROJO -> VERDE -> REFACTOR`).
2. Todas las pruebas unitarias (`@pytest.mark.unitaria`) y de aceptación (`@pytest.mark.aceptacion`) pasan en verde (`pytest`).
3. Cumple con la restricción no funcional de validación/robustez definida para el sprint (`RNF-01`).
4. Los cambios están integrados en la rama `main` del repositorio con commits descriptivos.
5. La tarjeta en el Project tiene registradas sus fechas reales de `Inicio` y `Terminado` y se encuentra en la columna `Liberación`.

* **Diferencia entre DoD y Criterios de Aceptación:** Los **Criterios de Aceptación** son específicos de cada historia y describen el comportamiento funcional esperado de esa regla (por ejemplo, en `HU-04`: *"aplicar 40 % de descuento después de restar la hora gratis"*), mientras que la **Definición de Terminado (DoD)** es un estándar global de calidad técnica que aplica por igual a **todas** las historias del sprint (tener código limpio, pruebas en verde, commit en `main`, etc.).

---

## B. Junta diaria (Bitácora)

| Día / Fecha | ¿Qué hice ayer? | ¿Qué haré hoy? | ¿Qué me lo impide? (Impedimentos) | Acción del SM |
| :--- | :--- | :--- | :--- | :--- |
| **Día 1 (27 oct)** | Definición de visión del producto y roles con Rubén. | Refinar las historias de R1 y R2 y configurar el tablero Kanban con límites WIP. | Ninguno. | Verifica que los límites WIP queden configurados (`2, 1, 2`). |
| **Día 2 (29 oct)** | Tablero Kanban configurado y backlog priorizado con MoSCoW. | Escribir escenarios BDD en `features/` y preparar la estructura base en Python. | Duda sobre el orden de aplicación en R1 (¿primero el 40 % o primero la hora gratis?). | El SM facilita consulta rápida con el PO (Rubén), confirmando que primero se resta la hora gratis y después se aplica el 40 %. |
| **Día 3 (31 oct)** | Escenarios BDD creados para tarifas y cancelaciones. | Implementar `HU-02` y `HU-03` (tarifa base de $70/h y 1 hora gratis en 4+ horas) con TDD. | Ninguno. | Monitorea que no se rebase el WIP = 1 en Desarrollo. |
| **Día 4 (03 nov)** | `HU-02` y `HU-03` pasaron pruebas unitarias. | Implementar `HU-04` (descuento del 40 % a estudiantes con credencial vigente) y refactorizar. | Conflicto al hacer `git push` por ediciones previas en la web de GitHub. | El SM guía la sincronización con `git pull --rebase origin main` para desbloquear el repositorio. |
| **Día 5 (06 nov)** | Regla R1 completa y probada en verde. | Programar regla R2 (`HU-05`, `HU-06`, `HU-07`: reembolsos del 100 %, 50 % y 0 %) con ciclos TDD. | Ninguno. | Revisa el avance contra la velocidad planeada de 21 puntos. |
| **Día 6 (09 nov)** | Reglas R1 y R2 implementadas y pruebas de aceptación en verde. | Ejecutar pruebas de regresión, verificar cobertura de caminos y preparar cierre del sprint. | Ninguno. | Coordina el paso de tarjetas de `Pruebas listo` a `Liberación`. |

---

## C. Revisión del sprint

### 6. Revisión de historias comprometidas
* **HU-01 (Reservar sala por bloques de 1 hora):** **Aceptada.** Cumple con validación de salas 1 a 4 y bloques enteros mínimos de 1 hora (evidencia en `src/apartalo/reglas.py` y `pytest`).
* **HU-02 (Tarifa base $70 MXN/hora):** **Aceptada.** Calcula múltiplos exactos de $70.00 MXN redondeados a 2 decimales (evidencia en `tests/unitarias/`).
* **HU-03 (1 hora gratis en 4+ horas):** **Aceptada.** Descuenta 1 hora automáticamente a partir de 4 horas consecutivas (evidencia en `tests/aceptacion/`).
* **HU-04 (40 % descuento estudiantes):** **Aceptada.** Aplica el 40 % después de descontar la hora gratis cuando hay credencial vigente (evidencia en `pytest` y commits TDD).
* **HU-05 (Reembolso 100 % con ≥ 6 horas):** **Aceptada.** Devuelve el 100 % cuando `horas_anticipacion >= 6` (evidencia en tabla FIT y `pytest`).
* **HU-06 (Reembolso 50 % entre 1 y < 6 horas):** **Aceptada.** Devuelve el 50 % redondeado a 2 decimales en el rango `[1, 6)` (evidencia en `pytest`).
* **HU-07 (Sin reembolso con < 1 hora):** **Aceptada.** Devuelve `$0.00` cuando falta menos de 1 hora (evidencia en prueba de regresión).
* **HU-08 (Consultar disponibilidad):** **Aceptada.** Permite verificar bloques libres por sala y fecha sin traslapes.

### 7. Cambio solicitado por el cliente (Nueva historia en el backlog)
* **Feedback de Rubén en la revisión:** Al ver el cálculo con credencial vigente, Rubén comentó: *"Muchos estudiantes llegan con credencial de otra universidad o sin resello del semestre actual; quiero poder registrar un código de validación o folio de credencial en la reserva"*.
* **Nueva historia agregada al backlog (`HU-15`):** *Como Dueño (Rubén), quiero registrar el folio de resello semestral de la credencial universitaria al aplicar el descuento estudiantil, para auditar qué alumnos recibieron la tarifa preferencial.* (Agregada al Backlog con prioridad `Should` y `2` puntos).

---

## D. Retrospectiva

### 8. ¿Qué salió bien? y ¿Qué hay que mejorar?
* **¿Qué salió bien?**
  * Aplicar TDD desde el inicio evitó errores en los valores límite críticos (como `5.99` vs `6.0` horas en cancelación y `3` vs `4` horas en tarifas).
  * Mantener el límite WIP en `1` para Desarrollo mantuvo el enfoque total en una regla a la vez.
* **¿Qué hay que mejorar?**
  * Sincronizar el repositorio local (`git pull`) antes de empezar a trabajar para evitar conflictos al hacer `push`.
  * Refinar desde el inicio los casos borde de entradas inválidas (horas negativas o cero) antes de codificar.

### 9. Dos acciones concretas para el Sprint 2
1. **Checklist previo a codificar:** Antes de iniciar cualquier historia de R3 en el Sprint 2, escribir explícitamente en el issue sus valores límite y entradas inválidas.
2. **Automatización de flujo Git:** Ejecutar siempre `git pull --rebase` al abrir Codespaces y correr `pytest` localmente antes de cada `git push` a `main`.
