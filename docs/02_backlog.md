## 2.1 Roles

| Rol | Quién es | Qué desea |
| :--- | :--- | :--- |
| **Estudiante** | Alumno universitario con credencial vigente de Ciudad Universitaria. | Reservar salas de estudio por hora con tarifa preferencial y promociones por bloques seguidos. |
| **Cliente General** | Usuario externo o profesionista que busca un espacio de trabajo o juntas. | Apartar una sala de forma rápida con tarifa estándar y conocer las políticas de cancelación. |
| **Dueño (Rubén)** | Propietario y administrador del local *Sala Común* (4 salas). | Evitar apartados fantasma (*no-shows*), automatizar el cobro correcto y controlar la ocupación. |
| **Sistema Apártalo** | Motor automatizado de reservas, tarifas y reembolsos (rol no humano). | Validar horarios, aplicar descuentos/promociones y calcular reembolsos sin errores. |

---

## 2.4 Plantilla invertida: historias que me faltaban

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
| :--- | :--- | :--- |
| Evitar llegar a *Sala Común* y encontrar todas las salas ocupadas en semana de exámenes. | **Para poder** asegurar un espacio antes de trasladarme en época de exámenes, **como** Estudiante, **quiero** consultar la disponibilidad en tiempo real de las 4 salas por fecha y hora. | #HU-08 |
| Recuperar el espacio y tener visibilidad financiera cuando un usuario cancela o no llega. | **Para poder** controlar la ocupación real y los reembolsos emitidos en el día, **como** Dueño (Rubén), **quiero** consultar un listado de reservas activas, canceladas y reembolsos aplicados. | #HU-11 |

**¿Cómo me ayudó ordenar por beneficio?**
Al enfocarnos primero en el valor real para el usuario (no perder el traslado en exámenes o no perder ingresos por salas vacías), descubrimos funciones operativas indispensables de consulta y monitoreo que no estaban explícitas en las reglas de cálculo R1, R2 y R3[cite: 9, 10].

---

## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
| :--- | :--- |
| **Sala** | Cada uno de los 4 espacios físicos de estudio o juntas dentro de *Sala Común*, con cupo máximo de 6 personas[cite: 9]. |
| **Bloque de reserva** | Unidad mínima de contratación equivalente a 1 hora completa de uso ($70 MXN tarifa base)[cite: 9]. |
| **Credencial vigente** | Identificación universitaria activa que acredita al usuario como estudiante para recibir 40 % de descuento[cite: 9]. |
| **Hora gratis por volumen** | Beneficio automático que descuenta el costo de 1 hora al reservar 4 o más horas seguidas (se aplica antes del descuento estudiantil)[cite: 9]. |
| **Ventana de cancelación** | Tiempo de anticipación previo al inicio de la reserva que define el reembolso (100 % con ≥ 6 h, 50 % entre 1 y < 6 h, 0 % con < 1 h)[cite: 9]. |

---

## 2.6 El iceberg

* **En la punta:** Las historias de usuario enfocadas en las reglas de negocio críticas (**R1**: cálculo de tarifas por hora, promoción de 4+ horas y descuento del 40 % a estudiantes; **R2**: cálculo de reembolsos por cancelación; y la reserva básica de salas), ya que tienen prioridad `Must` y entran directamente al **Sprint 1**[cite: 1, 9].
* **En el fondo:** Las reglas secundarias de límite de capacidad/tiempo (**R3**: tope de 4 horas seguidas y 6 personas por sala) con prioridad `Should`/`Could`, además de las **épicas** grandes y poco definidas que surgieron de ideas iniciales de Rubén (integración de cerraduras inteligentes con código QR y chat interno para estudiantes) con prioridad `Won't` / sin sprint asignado[cite: 1, 9, 10].
* **Por qué:** Siguiendo el principio ágil de entregar valor temprano y maximizar el trabajo no realizado, arriba del iceberg va lo indispensable para resolver el problema de cobros, descuentos y *no-shows* de inmediato, mientras que al fondo quedan las funcionalidades complejas o sin validar para no frenar el primer sprint[cite: 9, 10].
