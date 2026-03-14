# Plan Detallado 24 Meses — AI/Robotics Engineer

**Estructura:** 4 Bloques → 24 meses de trabajo
**Meta a 24 meses:** Embodied AI Engineer competitivo, con portafolio real de 10 repos

---

## 4 Bloques del Programa

| Bloque | Contenido |
|--------|-----------|
| **I — Foundations** | Programación, matemáticas, CS, software engineering |
| **II — Core AI** | ML, deep learning, visión, transformers, LLMs |
| **III — Core Robotics** | Kinemática, dinámica, control, ROS 2, simulación, manipulación |
| **IV — Research & Systems** | RL, embodied AI, papers, repos serios, proyectos tipo laboratorio |

---

## Reglas del Programa

1. No avanzas por emoción; avanzas por **entregables**
2. Cada mes debe dejar **código, notas y un proyecto**
3. Todo va en **GitHub**
4. **Nada** de brincar entre 20 cursos
5. Primero software + matemáticas + IA; luego robótica fuerte

---

## Carga Semanal

| Modo | Horas/semana |
|------|-------------|
| Mínimo serio | 15 h |
| Ideal | 20–25 h |
| Obsesivo | 30+ h |

**Distribución ideal por semana:**
- 6 h teoría
- 6–8 h implementación
- 4 h ejercicios matemáticos
- 3 h proyecto
- 1–2 h documentación / paper

**Estructura semanal tipo:**
- Lunes: Teoría dura
- Martes: Ejercicios matemáticos + implementación
- Miércoles: Curso + código
- Jueves: Proyecto
- Viernes: Proyecto + debugging
- Sábado: Paper + resumen + repaso
- Domingo: Descanso o repaso ligero

---

## Currículum Transversal (corre durante 24 meses)

### Matemáticas continuas
Aunque se concentran al inicio, se repasan siempre:
- álgebra lineal, cálculo multivariable, probabilidad, optimización

### Lectura de papers
- Mes 10+: 1 paper/semana
- Mes 16+: 2 papers/semana
- Mes 18+: 1 reproducción ligera/mes

### C++
Introducir desde mes 16 en adelante, cuando se entra fuerte a robótica y ROS 2

### Software engineering serio (siempre)
Testing, logging, profiling, documentación, Docker, Git branches, experiment tracking

---

## Exámenes Trimestrales

Cada 3 meses:
1. Examen teórico 90–120 min
2. Ejercicio práctico con código
3. Mini proyecto
4. Defensa oral grabada explicando lo aprendido

**Para "pasar" una fase hay que:**
- Explicar el tema sin leer
- Implementarlo
- Detectar errores típicos
- Conectarlo con sistemas reales

---

## AÑO 1 — BASE BRUTAL

### Mes 1 — Python, terminal, Git, entorno
**Objetivo:** Dejar listo el sistema operativo de estudio

**Semana 1:** Instalar entorno, Python básico, terminal Linux/macOS, estructura de carpetas, venv, pip, archivos
**Semana 2:** Funciones, módulos, manejo de errores, lectura/escritura de archivos
**Semana 3:** POO básica, imports, scripts reutilizables, debugging
**Semana 4:** Git y GitHub, README, primer mini proyecto CLI

**Recursos:** Python tutorial oficial, NumPy básico (familiarización temprana)

**Entregables:**
- Repo principal `ai-robotics-journey`
- 30 ejercicios de Python
- App CLI simple
- README del sistema de estudio

**Criterio de salida:** No se intimida con la terminal ni Git

---

### Mes 2 — Estructuras de datos y algoritmos
**Objetivo:** Pensar como ingeniero

**Semana 1:** Listas, tuplas, dicts, sets, complejidad temporal
**Semana 2:** Stacks, queues, hash maps, recursión
**Semana 3:** Árboles, grafos, BFS/DFS
**Semana 4:** Sorting/searching, testing básico, clean code

**Entregables:**
- Implementaciones propias: stack, queue, árbol binario, BFS, DFS
- 40 ejercicios de dificultad baja-media
- Paquete Python con tests

---

### Mes 3 — Álgebra lineal I
**Recurso central:** MIT 18.06 Gilbert Strang

**Semana 1:** Vectores, matrices, sistemas lineales
**Semana 2:** Eliminación Gaussiana, rango, independencia lineal
**Semana 3:** Espacios vectoriales, bases, subespacios
**Semana 4:** Ejercicios + examen corto

**Entregables:**
- Notebook de eliminación Gaussiana desde cero
- Resumen propio 10–15 páginas
- Examen resuelto

---

### Mes 4 — Álgebra lineal II
**Semana 1:** Autovalores y autovectores
**Semana 2:** Diagonalización, proyecciones
**Semana 3:** Mínimos cuadrados, SVD
**Semana 4:** PCA desde cero

**Entregables:**
- PCA implementado
- Visualización geométrica
- Mini ensayo: "Álgebra lineal para IA y robótica"

---

### Mes 5 — Cálculo y optimización
**Contexto:** MIT 6.S191 asume cálculo y álgebra lineal como prerrequisitos

**Semana 1:** Límites, derivadas, regla de la cadena
**Semana 2:** Derivadas parciales, gradiente
**Semana 3:** Jacobiano, Hessiano
**Semana 4:** Descenso por gradiente desde cero

**Entregables:**
- Gradiente descendente implementado
- Notebook visualizando superficies
- Hoja resumen de derivadas clave

---

### Mes 6 — Probabilidad y estadística
**Semana 1:** Probabilidad condicional, Bayes
**Semana 2:** Variables aleatorias, esperanza, varianza
**Semana 3:** Distribuciones comunes, inferencia
**Semana 4:** Máxima verosimilitud, métricas

**Entregables:**
- Simulaciones Monte Carlo
- Notebook Bayes y distribuciones
- Resumen de estadística para ML

---

### Mes 7 — NumPy, pandas, matplotlib, scikit-learn
**Semana 1:** NumPy serio: arrays, broadcasting, slicing
**Semana 2:** pandas: carga, limpieza y transformación
**Semana 3:** Visualización básica, pipelines de datos
**Semana 4:** scikit-learn setup, train/test split, métricas

**Entregables:**
- Notebook de análisis exploratorio
- Pipeline de limpieza documentado
- Dataset limpio con README

---

### Mes 8 — ML clásico I
**Semana 1:** Regresión lineal
**Semana 2:** Regresión logística
**Semana 3:** Regularización, overfitting
**Semana 4:** Evaluación, validación cruzada

**Entregables:**
- Modelo de scoring
- Modelo de clasificación
- Reporte comparando métricas

---

### Mes 9 — ML clásico II
**Semana 1:** Árboles de decisión
**Semana 2:** Random forest
**Semana 3:** Boosting, SVM
**Semana 4:** Clustering, PCA aplicado

**Entregables:**
- Proyecto completo con dataset real
- Comparación de 4 modelos
- README técnico limpio

---

### Mes 10 — Deep Learning I
**Recursos:** MIT 6.S191, PyTorch tutorials

**Semana 1:** Perceptrón, MLP, activaciones
**Semana 2:** Forward pass, loss, backprop conceptual
**Semana 3:** Optimización, entrenamiento, batch size
**Semana 4:** Red simple desde cero con NumPy

**Entregables:**
- MLP desde NumPy
- Reporte: backprop explicado paso a paso

**→ Desde este mes: 1 paper/semana**

---

### Mes 11 — Deep Learning II con PyTorch
**Semana 1:** Tensors, autograd
**Semana 2:** Datasets, dataloaders
**Semana 3:** Training loops, evaluación, checkpoints
**Semana 4:** Experimento completo

**Entregables:**
- Plantilla reutilizable de entrenamiento
- Clasificador en PyTorch
- Análisis underfitting/overfitting

---

### Mes 12 — Computer Vision I
**Recursos:** CS231n, OpenCV oficial

**Semana 1:** Imágenes como tensores, convoluciones
**Semana 2:** CNNs, clasificación
**Semana 3:** Augmentations, transfer learning
**Semana 4:** OpenCV básico: webcam, filtros, bordes

**Entregables:**
- Clasificador de imágenes propio
- Demo webcam con OpenCV
- Análisis de errores

---

## AÑO 2 — DE IA A ROBÓTICA AVANZADA

### Mes 13 — Computer Vision II
**Semana 1:** Detección de objetos
**Semana 2:** Segmentación
**Semana 3:** Tracking, optical flow
**Semana 4:** Calibración de cámara

**Entregables:**
- Detector o tracker
- Calibración de cámara
- Mini portafolio de visión

---

### Mes 14 — Transformers, NLP y LLMs
**Recursos:** MIT 6.S191 (actualizado con LLMs), Hugging Face

**Semana 1:** Embeddings, tokenización, attention
**Semana 2:** Transformers, arquitectura general
**Semana 3:** Fine-tuning conceptual, RAG
**Semana 4:** Agentes y tool use

**Entregables:**
- Mini chatbot con RAG
- Reporte de transformers
- Demo con tool calling

---

### Mes 15 — Embodied AI y sistemas multiagente
**Nota:** Carlos ya trae ventaja por background en agentes, automatización y orquestación

**Semana 1:** Percepción → planeación → acción
**Semana 2:** Memoria, tool use, arquitectura modular
**Semana 3:** Sistemas multimodales
**Semana 4:** Agente que controle entorno simple

**Entregables:**
- Arquitectura de agente embodied
- Agente básico en simulación
- Diagrama técnico del sistema

---

### Mes 16 — Robótica matemática I
**Recurso:** Modern Robotics

**Semana 1:** Frames, rotaciones
**Semana 2:** Matrices homogéneas, transformaciones SE(3)
**Semana 3:** Twists, exponenciales
**Semana 4:** Práctica geométrica

**Entregables:**
- Librería propia de transformaciones 2D/3D
- Visualizador básico
- Resumen SE(3)

**→ Desde este mes: 2 papers/semana, introducir C++**

---

### Mes 17 — Robótica matemática II
**Semana 1:** Cinemática directa
**Semana 2:** Cinemática inversa
**Semana 3:** Jacobianos
**Semana 4:** Velocidades y fuerzas

**Entregables:**
- Brazo 2D con FK/IK
- Notebook explicando Jacobianos
- Demo visual

---

### Mes 18 — Dinámica y control I
**Recurso:** MIT Underactuated Robotics

**Semana 1:** Newton-Euler, Lagrange
**Semana 2:** Ecuaciones de movimiento
**Semana 3:** Estabilidad, control PID
**Semana 4:** Espacio de estados

**Entregables:**
- Péndulo invertido en simulación
- PID implementado
- Reporte de estabilidad

**→ Desde este mes: 1 reproducción de paper/mes**

---

### Mes 19 — ROS 2 I
**Recurso:** ROS 2 Jazzy official tutorials (seguir en orden)

**Semana 1:** Instalación, workspaces
**Semana 2:** Packages, nodes, topics
**Semana 3:** Services, actions
**Semana 4:** Launch files, práctica integrada

**Entregables:**
- Paquete propio
- Publisher/subscriber funcional
- Service y action

---

### Mes 20 — ROS 2 II + Simulación
**Nota:** URDF es el formato estándar en ROS 2 para describir robots

**Semana 1:** TF2, rosbag
**Semana 2:** URDF
**Semana 3:** RViz, sensores
**Semana 4:** Robot diferencial en simulación

**Entregables:**
- URDF propio
- Demo en RViz
- Robot móvil básico simulado

---

### Mes 21 — Planeación y navegación
**Recurso:** Modern Robotics (motion planning, trayectorias)

**Semana 1:** A*, grid planning
**Semana 2:** RRT/RRT*
**Semana 3:** Trayectorias, time scaling
**Semana 4:** Navegación integrada

**Entregables:**
- Planeador de rutas
- Comparación A* vs RRT
- Robot navegando en simulación

---

### Mes 22 — Manipulación robótica
**Recurso:** MIT Robotic Manipulation (Russ Tedrake)

**Semana 1:** Grasping, pick and place
**Semana 2:** Pose estimation
**Semana 3:** Deep perception for manipulation
**Semana 4:** Integración visión + grasp

**Entregables:**
- Pipeline pick-and-place en simulación
- Percepción + grasp integrado
- Reporte experimental

---

### Mes 23 — Reinforcement Learning
**Recurso:** Sutton & Barto + Spinning Up (OpenAI)

**Semana 1:** MDPs, Bellman equations
**Semana 2:** Monte Carlo, TD learning, Q-learning
**Semana 3:** Policy gradients, actor-critic
**Semana 4:** Entorno tipo CartPole implementado

**Entregables:**
- Q-learning desde cero
- Experimento de policy gradient
- Mini reporte de resultados

---

### Mes 24 — Capstone Final tipo Laboratorio
**Integra:** percepción, modelo, planeación, control y evaluación

**Opciones:**

**Opción A:** Robot móvil simulado
- Percepción por cámara
- Planeación
- Navegación
- Módulo de lenguaje
- Acción autónoma

**Opción B:** Brazo robótico simulado
- Visión
- Detección de objetos
- Grasp planning
- Pick-and-place
- Interfaz natural por lenguaje

**Opción C — Recomendada:** Sistema Embodied AI
- Percepción multimodal
- LLM como planner
- Controlador o política
- Simulación completa
- Reporte técnico tipo paper

**Entregables obligatorios:**
- Código limpio y modular
- Video demo
- README serio
- Reporte técnico 15–25 páginas
- Lista de mejoras futuras / roadmap 12 meses

---

## Portafolio Final (10 repos)

| # | Repositorio |
|---|-------------|
| 1 | `python-foundations` |
| 2 | `math-for-ai-robotics` |
| 3 | `ml-classical` |
| 4 | `deep-learning-pytorch` |
| 5 | `computer-vision` |
| 6 | `llm-agents` |
| 7 | `robotics-math-control` |
| 8 | `ros2-systems` |
| 9 | `manipulation-or-navigation` |
| 10 | `capstone-embodied-ai` |

---

## Resultado Esperado por Etapa

| Tiempo | Capacidad |
|--------|-----------|
| 6 meses | Programar y hacer ML básico con soltura |
| 12 meses | Construir sistemas de IA respetables |
| 18 meses | Fuerte en visión, entrando bien a robótica |
| 24 meses | Proyectos tipo embodied AI bastante serios |

---

## Secuencia Óptima para el Perfil de Carlos

```
1. Software brutal
2. Matemáticas brutal
3. IA brutal
4. Visión
5. Agentes / LLMs
6. Robótica
7. Control
8. Embodied AI
```

**Foco principal:** AI Engineer + Vision + Agents
**Foco secundario:** Robotics + ROS 2 + Manipulation

**Lo que NO hacer:**
- Brincar entre 20 cursos sin terminar ninguno
- Meterse a RL demasiado pronto
- Comprar robots caros sin dominar simulación
- Leer papers avanzados antes de dominar fundamentos
- Confundir "ver contenido" con "saber"
