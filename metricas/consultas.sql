-- Ejercicio 8 · Consultas sobre la fotografía de tu tablero.

-- a) Puntos comprometidos en el Sprint 1
SELECT SUM(puntos) AS puntos_comprometidos
FROM tablero
WHERE sprint = 'Sprint 1';

-- b) Puntos entregados (estado = 'Liberación')
SELECT SUM(puntos) AS puntos_entregados
FROM tablero
WHERE sprint = 'Sprint 1' AND estado = 'Liberación';

-- c) Porcentaje de cumplimiento (entregados ÷ comprometidos)
SELECT
  ROUND(
    100.0 * SUM(CASE WHEN estado = 'Liberación' THEN puntos ELSE 0 END)
    / NULLIF(SUM(puntos), 0),
    2
  ) AS porcentaje_cumplimiento
FROM tablero
WHERE sprint = 'Sprint 1';

-- d) Tiempo de ciclo promedio en días (de inicio a terminado) de las historias entregadas
SELECT
  ROUND(AVG(julianday(terminado) - julianday(inicio)), 2) AS ciclo_promedio_dias
FROM tablero
WHERE sprint = 'Sprint 1'
  AND estado = 'Liberación'
  AND inicio IS NOT NULL
  AND terminado IS NOT NULL;

-- e) Subconjunto: historias con prioridad 'Must', con sus puntos y su estado
SELECT titulo, puntos, estado
FROM tablero
WHERE prioridad = 'Must'
ORDER BY titulo;
