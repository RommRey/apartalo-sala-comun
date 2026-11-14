# 6. Pruebas de aceptación y TDD

## 6.2 Ciclos TDD (Historial de commits)

| Paso del ciclo y mensaje | Enlace al commit |
| :--- | :--- |
| `ROJO: prueba de calculo de tarifa R1 con hora gratis y descuento estudiante` | [ff4d018](https://github.com/RommRey/apartalo-sala-comun/commit/ff4d018dfaeb134c690c32c6e9ad78965aff1d2d) |
| `VERDE: implementa calculo de tarifa R1 con 1 hora gratis y 40% descuento` | [891f84d](https://github.com/RommRey/apartalo-sala-comun/commit/891f84d75afb2fd0d423a78fe66e53c15a8cfe94) |
| `ROJO: prueba de reembolso por cancelacion R2 con limites de 6h y 1h` | [e915646](https://github.com/RommRey/apartalo-sala-comun/commit/e9156465969d72058f81c6ed466c4dd4b825c898) |
| `VERDE: implementa regla R2 de reembolsos por cancelacion` | [c257b34](https://github.com/RommRey/apartalo-sala-comun/commit/c257b34f482afa6ec9b6dffb4bc087538ee5574c) |
| `REFACTOR: extrae constantes de tarifas, promocion y ventanas de cancelacion` | [2c057de](https://github.com/RommRey/apartalo-sala-comun/commit/2c057decae59578e199ccf012357ea6ebf780d6e) |

## 6.6 Cobertura de caminos

Analizando la función `calcular_reembolso(monto_pagado, horas_anticipacion)` en `src/apartalo/reglas.py`:
* **Camino 1 (`raise ValueError`):** Cuando `monto_pagado < 0` o `horas_anticipacion < 0`. Cubierto por `test_entradas_invalidas_r2`.
* **Camino 2 (`porcentaje = 1.0` -> `return`):** Cuando `horas_anticipacion >= 6.0`. Cubierto por `test_reembolso_100_con_6_horas_o_mas`.
* **Camino 3 (`porcentaje = 0.5` -> `return`):** Cuando `1.0 <= horas_anticipacion < 6.0`. Cubierto por `test_reembolso_50_entre_1_y_menos_de_6_horas`.
* **Camino 4 (`porcentaje = 0.0` -> `return`):** Cuando `horas_anticipacion < 1.0`. Cubierto por `test_sin_reembolso_con_menos_de_1_hora`.

**Resultado:** Se recorren **4 de 4 caminos (100 % de cobertura de caminos)**.

## 6.7 Prueba de regresión

* **Defecto simulado/prevenido:** Cambiar el operador de límite `>= 6.0` por `> 6.0` en `calcular_reembolso` provocaba que cancelar con exactamente 6.0 horas de anticipación devolviera solo el 50 % ($70.00) en lugar del 100 % ($140.00).
* **Prueba que lo atrapa:** `test_regresion_limite_exacto_6_horas` (marcada con `@pytest.mark.regresion` en `tests/unitarias/test_regresion.py`), que verifica `calcular_reembolso(140.00, 6.0) == 140.00`.
