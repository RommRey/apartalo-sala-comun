## 3.2 Límites WIP y justificación

Como soy un equipo de una sola persona trabajando en el desarrollo:
* **Aceptación (Límite: 2):** Me permite tener máximo dos historias listas para tomar o en revisión de criterios sin acumular trabajo sin empezar.
* **Desarrollo (Límite: 1):** Al ser un solo desarrollador aplicando TDD, enfocarme en **una sola historia a la vez** evita el cambio de contexto (*context switching*) y asegura terminar rápido cada ciclo Rojo-Verde-Refactor.
* **Pruebas (Límite: 2):** Permite validar la historia recién terminada y mantener una segunda en revisión de aceptación/regresión sin crear cuellos de botella antes de liberar.

## 3.3 Políticas explícitas

* **De Historias a Aceptación:** La historia está redactada en formato *Como-Quiero-Para*, tiene al menos 2 criterios de aceptación claros, revisión INVEST completa y está priorizada en el Sprint 1.
* **De Aceptación a Desarrollo:** Se han escrito sus escenarios BDD en `features/`, se ha estimado en puntos y existe capacidad disponible en la columna *Desarrollo* (WIP < 1).
* **De Desarrollo a Desarrollo listo:** El código de la funcionalidad está implementado en `src/apartalo/reglas.py`, sigue el ciclo TDD y todas las pruebas unitarias pasan en verde.
* **De Desarrollo listo a Pruebas:** Hay capacidad en *Pruebas* (WIP < 2) y el desarrollador toma la tarjeta para ejecutar las pruebas de aceptación (`pytest`).
* **De Pruebas a Pruebas listo:** Todas las pruebas unitarias, de aceptación y de regresión pasan en verde sin errores y el código está en la rama `main`.
* **De Pruebas listo a Liberación:** El Product Owner verifica que se cumplen todos los criterios de aceptación y la Definición de Terminado (DoD), registrando la fecha en el campo `Terminado`.

## 3.4 Las seis prácticas de Kanban

| Práctica de Kanban | Cómo aplica en mi tablero |
| :--- | :--- |
| **1. Visualizar el flujo de trabajo** | Mediante el tablero Board con las 7 columnas (`Historias` hasta `Liberación`), distinguiendo columnas activas de columnas búfer (`listo`). |
| **2. Limitar el trabajo en curso (WIP)** | Configurando límites numéricos estrictos en `Aceptación` (2), `Desarrollo` (1) y `Pruebas` (2). |
| **3. Gestionar el flujo** | Observando qué tarjetas se detienen en los búferes, registrando fechas de `Inicio` y `Terminado` para medir el tiempo de ciclo (*Cycle Time*). |
| **4. Hacer explícitas las políticas** | Documentando en este archivo (`03_tablero.md`) las reglas exactas de entrada y salida de cada columna para no mover tarjetas a medias. |
| **5. Implementar ciclos de retroalimentación** | A través de las juntas diarias (bitácora), la revisión del sprint con criterios de aceptación y la retrospectiva al cierre. |
| **6. Mejorar colaborativamente (evolucionar experimentalmente)** | Analizando las métricas exportadas en el Ejercicio 8 (cumplimiento y tiempo de ciclo) para ajustar los límites WIP y la carga del Sprint 2. |
