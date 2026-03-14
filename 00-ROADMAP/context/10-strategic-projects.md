# 10 Proyectos Estratégicos — AI/Robotics Engineer

Organizados en dificultad creciente.
Tiempo total estimado: 18–24 meses de estudio serio.

---

## Etapa 1 — Fundamentos de IA (Proyectos 1–3)

### Proyecto 1 — Machine Learning desde cero
**Repo:** `machine-learning-from-scratch`
**Alineado a:** Meses 7–9 del plan

**Objetivo:** Entender ML sin depender de librerías.

**Implementar (solo Python + NumPy):**
- Regresión lineal
- Regresión logística
- K-means
- Árbol de decisión
- PCA

**Estructura:**
```
machine-learning-from-scratch/
├── linear_regression/
├── logistic_regression/
├── decision_tree/
├── kmeans/
└── pca/
```

**Qué demuestra:** Comprensión matemática real, optimización, gradiente. Impresiona mucho a ingenieros senior.

---

### Proyecto 2 — Pipeline profesional de Deep Learning
**Repo:** `deep-learning-training-pipeline`
**Alineado a:** Meses 10–11 del plan

**Objetivo:** Entrenar modelos como en producción.

**Componentes:**
- PyTorch training loop modular
- Data loaders configurables
- Logging estructurado
- Experiment tracking (Weights & Biases o MLflow)
- Checkpoints automáticos

**Estructura:**
```
deep-learning-training-pipeline/
├── models/
├── datasets/
├── training/
├── evaluation/
└── utils/
```

**Qué demuestra:** Reproducibilidad, buenas prácticas, ingeniería ML de producción.

---

### Proyecto 3 — Sistema completo de visión
**Repo:** `computer-vision-lab`
**Alineado a:** Meses 12–13 del plan

**Objetivo:** Construir pipelines completos de visión.

**Componentes:**
- Clasificación de imágenes (CNN propia)
- Detección de objetos
- Segmentación
- Tracking de objetos

**Herramientas:** PyTorch + OpenCV

**Demo final:** App que detecta objetos, sigue objetos y mide distancias.

---

## Etapa 2 — Sistemas de IA (Proyectos 4–6)

### Proyecto 4 — Sistema RAG avanzado
**Repo:** `rag-systems-lab`
**Alineado a:** Mes 14 del plan

**Objetivo:** Dominar LLMs con datos privados.

**Componentes:**
- Embeddings (seleccionar modelo)
- Vector database (Chroma, Pinecone, Weaviate)
- Pipeline de retrieval
- Generation con LLM
- Evaluación de calidad de respuestas

**Aplicación ejemplo:**
- Asistente legal con documentos
- Asistente médico con historial
- Asistente empresarial con manuales

---

### Proyecto 5 — Sistema multiagente
**Repo:** `multi-agent-systems`
**Alineado a:** Mes 15 del plan

**Objetivo:** Construir sistemas de agentes cooperativos.

**Arquitectura:**
```
User
 ↓
Planner Agent
 ↓
Worker Agents
 ↓
Tools (APIs, databases, search)
```

**Componentes:**
- Planner agent (orquestador)
- Tool use modular
- Memoria compartida / por agente
- Coordinación entre agentes

**Aplicación ejemplo:**
Agente que investiga un tema → analiza → escribe reporte técnico estructurado.

---

### Proyecto 6 — AI Automation Engine
**Repo:** `ai-automation-engine`
**Alineado a:** Mes 15 (conexión directa con empresa)

**Objetivo:** Conectar IA con operaciones reales de negocio.

**Componentes:**
- Agentes de ventas (responden leads)
- Clasificación y calificación de leads
- CRM automation
- Seguimiento automático de prospectos

**Resultado:**
Sistema que responde leads, califica prospectos y agenda citas sin intervención humana.

**Nota estratégica:** Este proyecto es el primer prototipo real de la empresa futura.

---

## Etapa 3 — Robótica e inteligencia física (Proyectos 7–8)

### Proyecto 7 — Simulador robótico matemático
**Repo:** `robotics-simulation-lab`
**Alineado a:** Meses 16–18 del plan

**Objetivo:** Entender cinemática y control a nivel matemático.

**Implementar:**
- Brazo robótico 2D (luego 3D)
- Cinemática directa (FK)
- Cinemática inversa (IK)
- Control PID

**Resultado:** Simulación interactiva de robot con visualización.

---

### Proyecto 8 — Robot autónomo en simulación
**Repo:** `autonomous-robot-system`
**Alineado a:** Meses 19–21 del plan

**Objetivo:** Integrar percepción, planeación, navegación y control.

**Componentes:**
- Percepción (cámara + sensores)
- Planificación de trayectoria (A* o RRT)
- Navegación autónoma
- Control de movimiento

**Stack:** ROS 2 + Gazebo + OpenCV

**Demo final:** Robot que detecta obstáculos, navega y toma decisiones autónomas.

---

## Etapa 4 — Inteligencia avanzada (Proyectos 9–10)

### Proyecto 9 — Agente embodied en simulación
**Repo:** `embodied-ai-agent`
**Alineado a:** Meses 22–23 del plan

**Objetivo:** Construir agente que percibe, razona y actúa en entorno simulado.

**Arquitectura:**
```
Vision → LLM Planner → Actions
```

**Componentes:**
- Percepción visual (cámara → descripción)
- LLM como planner (razona sobre lo que ve)
- Acciones ejecutadas en entorno simulado

**Resultado:** Agente que observa el entorno, planea acciones y las ejecuta autónomamente.

---

### Proyecto 10 — AI Operating System (CAPSTONE y PROTOTIPO DE EMPRESA)
**Repo:** `ai-operating-system`
**Alineado a:** Mes 24 (capstone) y Año 2 del plan de empresa

**Objetivo:** Crear el primer prototipo real de la empresa futura.

**Componentes:**
- Sistema multiagente central (orquestador)
- Automatización de procesos empresariales
- Dashboards de monitoreo
- Integración con APIs externas (CRM, email, calendarios)

**Módulos:**
```
ai-operating-system/
├── agent-core/         ← motor de agentes
├── planning/           ← planificación de tareas
├── workflows/          ← flujos de trabajo automatizados
├── integrations/       ← APIs externas
└── dashboard/          ← interfaz de monitoreo
```

**Uso:**
Empresa instala el sistema → obtiene agentes de ventas + operativos + analíticos trabajando 24/7.

---

## Resumen: 10 proyectos ordenados

| # | Repo | Meses | Etapa |
|---|------|-------|-------|
| 1 | machine-learning-from-scratch | 7–9 | Fundamentos IA |
| 2 | deep-learning-training-pipeline | 10–11 | Fundamentos IA |
| 3 | computer-vision-lab | 12–13 | Fundamentos IA |
| 4 | rag-systems-lab | 14 | Sistemas IA |
| 5 | multi-agent-systems | 15 | Sistemas IA |
| 6 | ai-automation-engine | 15 | Sistemas IA → Empresa |
| 7 | robotics-simulation-lab | 16–18 | Robótica |
| 8 | autonomous-robot-system | 19–21 | Robótica |
| 9 | embodied-ai-agent | 22–23 | Embodied AI |
| 10 | ai-operating-system | 24 | Capstone → Empresa |

---

## Tiempo estimado por proyecto

| Tamaño | Tiempo |
|--------|--------|
| Proyecto pequeño (1–3) | 3–4 semanas |
| Proyecto mediano (4–6) | 6–8 semanas |
| Proyecto grande (7–10) | 2–3 meses |

**Total estimado:** 18–24 meses

---

## Conexión proyectos ↔ empresa

Los últimos proyectos son **prototipos reales** del negocio:

- Proyecto 6 (`ai-automation-engine`) → MVP de ventas del producto
- Proyecto 10 (`ai-operating-system`) → Producto central de la empresa
- Proyectos 7–9 → Fundación técnica de la Fase 2 (autonomía física)
