# Apártalo — Sala común

Qué es: Aplicación web/móvil de reservas para Sala Común, un espacio con 4 salas de estudio y juntas cerca de Ciudad Universitaria.

Para quién: Estudiantes universitarios y público general que buscan espacios de estudio o trabajo, así como para Rubén (dueño del negocio).

Qué problema resuelve: Elimina la saturación y el desperdicio de salas por apartados fantasma (no-shows) en temporadas críticas como exámenes finales, automatizando el cálculo de tarifas, descuentos estudiantiles y reglas de cancelación.

¿Por qué no cascada?
Causa 1 — Incertidumbre en los requisitos y reglas de negocio: Rubén aún tiene dudas clave sobre el modelo de negocio (por ejemplo, si cobrar por hora o por día) y propone ideas sin validar (chat, puertas con QR). Cascada exige congelar todos los requisitos al inicio, lo que llevaría a construir funcionalidades costosas que podrían descartarse después.

Causa 2 — Entrega tardía de valor: En cascada, el software funcional se entrega hasta el final de todo el proyecto. Rubén necesita resolver de inmediato el descontrol de reservas y cobros antes de la próxima temporada de exámenes finales, por lo que necesita entregas incrementales rápidas.

Uso de prototipos: Sí usaría prototipos rápidos (de baja fidelidad / wireframes) antes de programar la interfaz de reserva o el acceso por QR, para validar con Rubén y con estudiantes de CU si el flujo de selección de bloques por hora y validación de credencial es claro e intuitivo antes de invertir código.

## Manifiesto del proyecto
Valor 1 — Software funcionando sobre documentación extensiva: Decisión concreta: Entregar las reglas de cálculo de tarifa (R1) y reembolso por cancelación (R2) programadas y verificadas con pruebas automatizadas (pytest) al cierre del Sprint 1, en lugar de redactar un documento extenso de especificación de requerimientos.
Valor 2 — Respuesta ante el cambio sobre seguir un plan: Decisión concreta: Dejar la regla de límite de horas y capacidad (R3) y las dudas de Rubén (como el cobro por día o el chat) en el Product Backlog para ajustarlas en futuros sprints según el uso real de las salas, sin detener el avance actual.
Principio 1 — Nuestra mayor prioridad es satisfacer al cliente mediante la entrega temprana y continua de software con valor: Decisión concreta: Priorizar en el Sprint 1 el motor de reservas, tarifas con descuento de estudiante y cancelaciones, que es lo que resuelve directamente el problema de saturación y pérdidas económicas de Rubén.
Principio 2 — La simplicidad, o el arte de maximizar la cantidad de trabajo no realizado, es esencial: Decisión concreta: Posponer integraciones complejas de hardware (como abrir puertas con QR) o módulos secundarios (como un chat interno) para enfocarnos únicamente en las reglas esenciales de negocio en esta primera iteración

## Frameworks
De Scrum: Roles definidos (Product Owner, Equipo de Desarrollo), iteraciones cortas de tiempo fijo (Sprints de 2 semanas), Product Backlog priorizado, estimación por puntos de historia y revisión de velocidad.   
De Kanban: Visualización continua del flujo de trabajo mediante un tablero con columnas de estado (incluyendo columnas búfer como Desarrollo listo y Pruebas listo) y límites WIP (Work In Progress) en Aceptación, Desarrollo y Pruebas para evitar cuellos de botella.
De XP (Extreme Programming): Desarrollo guiado por pruebas (TDD con ciclos Rojo - Verde - Refactor), historias de usuario con criterios de aceptación claros y enfoque en código limpio y refactorización continua.
Nombre de la combinación de Scrum y Kanban: Scrumban.

## Requisito o solución 

1. "En exámenes finales no me alcanzan las salas y hay gente que las aparta y no llega."Clasificación: Requisito (describe el problema/necesidad real del negocio: alta demanda en picos y no-shows).
2.  "Quiero que la app tenga chat para que los estudiantes se organicen."Clasificación: Solución (propone una herramienta específica —un chat—).Requisito detrás: Los estudiantes necesitan coordinarse con los integrantes de su equipo para saber quién asistirá y a qué hora/sala quedó hecha la reserva
3.  "Los estudiantes deberían pagar menos."Clasificación: Requisito (expresa una necesidad de negocio/política de precios diferenciada para el segmento estudiantil, sin imponer aún el mecanismo técnico).
4.  "Que la puerta se abra sola con un código QR."Clasificación: Solución (impone una tecnología específica —cerradura inteligente con QR—).Requisito detrás: Controlar el acceso físico a las 4 salas para asegurar que únicamente entren las personas con una reserva válida y vigente, sin depender de supervisión manual constante.
5.  "No sé si cobrar por hora o por día."Clasificación: Requisito (indefinido / duda de modelo de cobro) (plantea la necesidad de definir el esquema de tarificación por tiempo de uso, lo cual se aterrizó en R1 cobrando por bloques de hora).
   
## Incertidumbre (Matriz de Stacey)
Ubicación en el diagrama: Cae en la zona Complicada (cercana al límite con Compleja respecto al qué, y Simple/Complicada respecto al cómo).Eje del qué (Requisitos): Incertidumbre media. Aunque el núcleo de reservas y reglas de cobro/cancelación ya se definió en R1 y R2, Rubén empezó con dudas comerciales (hora vs. día) y peticiones poco aterrizadas (chat, QR
Eje del cómo (Tecnología): Incertidumbre baja-media. Apártalo ya tiene una base tecnológica probada de apps de reservas para negocios locales, por lo que implementar lógica de tarifas y cancelaciones es conocido, aunque integrar cerraduras QR a futuro elevaría la complejidad técnica.
¿Qué harías para bajar la incertidumbre del qué en este sprint? Ejecutar un Sprint 1 enfocado exclusivamente en las reglas ya acordadas (R1 y R2), mostrar a Rubén un incremento funcional con datos reales de tarifas y reembolsos al final del sprint para validar si el esquema por hora y el descuento del 40 % funcionan comercialmente, y usar prototipos rápidos antes de construir cualquier función secundaria.  
