# Plan de Lanzamiento — Sesión Cero
**Fecha de inicio:** Marzo 2026
**Estado:** Activo

---

## Principio Central: Dos Relojes, No Dos Cerebros

Track académico y track empresarial corren en paralelo pero en tiempo **separado**.
- **Modo Estudiante:** Lunes–Viernes, bloques de estudio profundo. Objetivo: entregables técnicos.
- **Modo Founder:** Viernes tarde + Sábado mañana (3–5h). Objetivo: validación de mercado.

En Mes 1–6, el track empresarial no requiere código. Son conversaciones, investigación, pensamiento estratégico.

---

## TRACK ACADÉMICO — Mes 1

### Objetivo real del mes
Al final del mes: sentarse ante un problema Python nuevo y resolverlo sin buscar cómo hacer cada cosa básica. Nivel 1 real, no fingido.

### Capa 1 — Entorno (Días 1–3)
- WSL2 o Linux nativo
- Python 3.11+
- VS Code + extensiones (Python, Pylance, GitLens)
- Git configurado globalmente
- Primer repo en GitHub, primer commit desde terminal
- conda o venv para ambientes virtuales

### Capa 2 — Python fundamental (Días 4–10)
- Variables, tipos (int, float, str, bool, None), operadores
- Control de flujo: if/elif/else, for, while, break, continue
- **Funciones** — concepto más importante del mes:
  - def, return, parámetros, scope
  - *args, **kwargs
  - funciones como valores (primera clase)
  - docstrings correctos

### Capa 3 — Estructuras de datos (Días 11–18)
- Listas, diccionarios, tuplas, conjuntos
- Comprensiones de lista y diccionario
- f-strings y formateo moderno
- Manejo de archivos (open, read, write)
- Módulos y paquetes (import, estructura multi-archivo)

### Capa 4 — OOP y cierre (Días 19–25)
- Clases, instancias, métodos, atributos
- Herencia básica
- try/except/finally, excepciones comunes
- PEP 8 + ruff/flake8
- pytest básico (primeros tests)
- Linux/Bash: pipes, scripts básicos, variables de entorno

---

### Semana por Semana

**Semana 1 — Setup + Python básico**
- Días 1–2: Entorno completo. Primer repo en GitHub.
- Días 3–5: Variables, tipos, control de flujo. Por cada concepto: mínimo 3 ejercicios.
- Día 6: Push ejercicios semana 1.
- Entregable: `exercises/week-01/` con 10+ ejercicios.

**Semana 2 — Funciones + Estructuras (mini-proyecto 1)**
- Funciones a fondo (la semana más importante).
- Listas, dicts, comprensiones.
- Mini-proyecto 1: **Todo List en terminal** — agregar/completar/listar/persistir tareas en .txt.

**Semana 3 — OOP + Git workflow (mini-proyecto 2)**
- Clases y objetos. Módulos. Error handling.
- Git: branches, merge, PRs, .gitignore.
- Mini-proyecto 2: **File Organizer** — script que organiza archivos por extensión en subcarpetas usando `pathlib`.

**Semana 4 — Integración + Cierre (mini-proyecto 3)**
- Virtual environments, requirements.txt.
- pytest básico.
- Mini-proyecto 3: **Text Analyzer** — lee .txt/.csv, calcula estadísticas (frecuencia, longitud), produce reporte. Sin pandas.
- Cierre: README profesional del repo.

---

### Entregable Final Mes 1
```
python-foundations/
├── exercises/
│   ├── week-01/   (10+ ejercicios)
│   ├── week-02/   (10+ ejercicios)
│   ├── week-03/   (10+ ejercicios)
│   └── week-04/   (10+ ejercicios)
├── mini-projects/
│   ├── todo-list/
│   ├── file-organizer/
│   └── text-analyzer/
├── notes.md
└── README.md
```

**Criterio de aprobación:** Resolver un problema Python nuevo sin buscar cada cosa básica.

---

### Recurso principal Mes 1
- Python oficial: https://docs.python.org/3/tutorial/
- Ejercicios: https://exercism.org/tracks/python (complemento)

### Lo que NO hacer en Mes 1
1. No saltar a NumPy/pandas — NumPy es Mes 7
2. No tomar múltiples cursos en paralelo
3. No construir el producto empresarial todavía

---

## TRACK EMPRESARIAL — Mes 1 (sin código)

### Objetivo
Iniciar customer discovery del vertical elegido. 5 conversaciones reales.

### Actividad 1 — Elegir vertical (Semana 1)
Criterio: acceso directo, no tamaño del mercado.
Verticales disponibles: clínicas, despachos legales, inmobiliarias, educación, agricultura.
Elegir el que tiene al menos 1 contacto conocido para la primera conversación.

### Actividad 2 — Customer Discovery (Semanas 2–4)
**Meta:** 5 conversaciones de 30–45 min.
**Regla:** No vender, no mostrar producto. Solo preguntar y escuchar.

Las 5 preguntas guía:
1. ¿Qué tareas repetitivas de tu jornada sientes que son pérdida de tiempo?
2. ¿Qué parte de tu trabajo te frustra más? ¿Por qué no está automatizado?
3. ¿Usas software hoy para esto? ¿Qué te falta?
4. Si pudieras eliminar una tarea completamente, ¿cuál sería?
5. ¿Cuánto vale resolver ese problema (tiempo, dinero, estrés)?

Documentar cada conversación en archivo. Patrones repetidos = señal de problema real.

### Actividad 3 — Mapa del Problema (Semana 4)
Documento de 1 página: "El problema que voy a resolver."
Incluye: quién lo tiene, qué hace hoy, por qué esa solución es insuficiente, qué solución ideal describió el cliente.

**Tiempo requerido:** 4–6 horas semanales.

---

## Semana 1 Concreta (arranca hoy)

| Día | Académico | Empresarial |
|-----|-----------|-------------|
| Hoy (Jue 12) | Setup: WSL2 + Python + VS Code + Git | — |
| Vie 13 | Setup completo. Primer repo + primer commit. | Decide vertical. Lista 10 contactos del sector. |
| Sáb 14 | Variables, tipos, operadores — 20 ejercicios | Manda 3 mensajes para agendar conversaciones |
| Dom 15 | Descanso | — |
| Lun 16 | if/elif/else + for + while — 15 ejercicios | — |
| Mar 17 | Funciones (deep dive) | Primera conversación si está agendada |
| Mié 18 | Más funciones + listas + inicio mini-proyecto 1 | — |

---

## Evaluación de Fin de Mes 1

Para declarar Mes 1 aprobado, se requiere:
- [ ] Repo `python-foundations` en GitHub con estructura completa
- [ ] 3 mini-proyectos funcionando
- [ ] 40+ ejercicios en total
- [ ] Resolver problema nuevo sin tutorial
- [ ] 5 conversaciones de customer discovery documentadas
- [ ] Documento "El problema que voy a resolver" (1 página)

---

## Conexión con Mes 2+

Mes 1 construye la base que hace posible todo lo demás:
- El Python de Mes 1 es el lenguaje de todo el plan de 24 meses
- Las conversaciones de Mes 1 determinan el vertical del producto
- El repo de Mes 1 es la primera pieza del portafolio público

**Siguiente sesión:** Al final de Mes 1, evaluación formal antes de declarar Mes 2.
