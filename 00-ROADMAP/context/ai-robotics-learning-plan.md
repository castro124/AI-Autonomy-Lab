# Master Learning Plan: AI/Robotics Engineer (PhD-Like Level)

**Owner:** Carlos
**Goal:** Convertirse en AI/Robotics Engineer de nivel senior/research
**Horizonte:** 3–5 años para nivel muy fuerte. Meta real: Nivel 4–5 del sistema de evaluación.
**Estrategia recomendada:** AI Engineer brutal primero → luego Robótica y Embodied AI encima

---

## Meta Final

Ser capaz de:
- Construir modelos de ML y DL desde cero y con frameworks
- Entender matemáticamente lo que hacen
- Desarrollar sistemas reales de percepción, decisión y control
- Programar robots en simulación y en hardware
- Leer papers y reproducir resultados
- Diseñar productos y sistemas autónomos útiles

---

## Sistema de Evaluación por Niveles

| Nivel | Descripción |
|-------|-------------|
| **Nivel 1** | Entiende conceptos y hace notebooks |
| **Nivel 2** | Implementa modelos y proyectos sin tutorial completo |
| **Nivel 3** | Lee documentación oficial, corrige errores y optimiza |
| **Nivel 4** | Reproduce papers y diseña sus propios sistemas |
| **Nivel 5** | Construye productos, research repos y arquitectura propia |

**Meta de Carlos: Nivel 4–5**

---

## Orden Exacto de Estudio

```
1.  Python + Git + Linux
2.  Álgebra lineal + cálculo + probabilidad
3.  ML clásico
4.  Deep Learning
5.  Computer Vision
6.  Robótica matemática
7.  ROS 2
8.  Control avanzado
9.  Manipulación
10. Reinforcement Learning
11. LLMs + agentes + embodied AI
12. Papers + especialización
```

---

## Fases Detalladas

### Fase 0 — Preparación mental y sistema de trabajo (1 semana)

**Setup requerido:**
- Repositorio principal en GitHub para todo el progreso
- Segundo repositorio para mini-proyectos
- Cuaderno de notas técnico
- Sistema de repetición (Anki o notas activas)
- Ritmo mínimo fijo: 2–4 horas diarias, 6 días/semana

**Regla:** Cada bloque teórico termina con código y proyecto.

---

### Fase 1 — Fundamentos de programación y CS (2–4 meses)

**Objetivo:** Python, Linux, Git y estructuras de datos como herramientas naturales.

**Temario:**
- Python: sintaxis, funciones, clases, módulos, comprensión de listas, manejo de errores, archivos, entornos virtuales
- Git y GitHub
- Linux / terminal
- Estructuras de datos: arrays, listas enlazadas, pilas, colas, hash maps, árboles, grafos
- Algoritmos: búsqueda, ordenamiento, recursión, backtracking, complejidad temporal y espacial
- Software engineering: testing, debugging, logging, modularidad, OOP, clean code

**Recursos base:** Documentación oficial de Python

**Proyectos obligatorios:**
- Calculadora científica en CLI
- Gestor de tareas en Python
- Scraper simple
- Implementación propia de: stack, queue, binary tree, BFS/DFS
- Pequeño paquete en Python publicado en GitHub

**Criterio para pasar:** Resolver problemas medianos sin copiar código y estructurar un proyecto limpio.

---

### Fase 2 — Matemáticas de verdad (4–8 meses, en paralelo)

**2.1 Álgebra lineal**
Recurso: MIT OCW Gilbert Strang
Temario: vectores, espacios vectoriales, matrices, sistemas lineales, independencia lineal, bases, transformaciones lineales, autovalores, autovectores, SVD, matrices positivas definidas, proyecciones, least squares
Meta: usar en PCA, regresión, transformaciones 3D, cinemática

**2.2 Cálculo**
Temario: límites, derivadas, reglas, gradiente, Jacobiano, Hessiano, integrales, series, multivariable, optimización
Meta: entender backpropagation, dinámica, control y optimización

**2.3 Probabilidad y estadística**
Temario: probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones, inferencia, MLE, intervalos, testing, Monte Carlo
Meta: leer ML con soltura

**2.4 Optimización**
Temario: convexidad, descenso por gradiente, SGD, Adam, restricciones, Lagrange, programación lineal y no lineal

**Proyectos:**
- Regresión lineal desde cero
- PCA desde cero
- Optimización por gradiente de función no trivial
- Notebook explicando eigenvalues con visualizaciones

---

### Fase 3 — Machine Learning clásico (3–5 meses)

**Temario:**
Preparación de datos, train/val/test, métricas, overfitting/regularización, regresión lineal y logística, árboles, random forest, boosting, SVM, k-means, PCA, feature engineering, interpretabilidad, pipelines

**Stack:** scikit-learn, pandas, numpy, matplotlib

**Proyectos:**
Score de leads, churn prediction, detección de fraude, modelo de pricing, segmentación de clientes

**Criterio:** Explicar por qué un modelo falla, no solo entrenarlo.

---

### Fase 4 — Deep Learning serio (6–10 meses)

**4.1 Entrada práctica**
- fast.ai Practical Deep Learning
- PyTorch basics: tensors, autograd, datasets, training loops, optimizers, checkpoints, torch.compile

**Recursos:** PyTorch tutorials oficiales, Deep Learning Book (Goodfellow, Bengio, Courville)

**4.2 Teoría profunda**
Perceptrón, MLP, activaciones, inicialización, batch norm, regularización, optimización, CNNs, RNNs, attention, transformers, representación, embeddings, scaling laws, fine-tuning, distillation

**4.3 Especializaciones dentro de DL**
Computer Vision, NLP/LLMs, Time series, Multimodal, Reinforcement Learning

**Recurso visión:** CS231n

**Proyectos:**
- CNN para clasificación propia
- Detector de objetos
- Segmentación semántica
- Fine-tuning de modelo de visión
- Pequeño chatbot RAG
- Modelo de forecasting
- Mini-transformer desde cero

**Criterio:** Implementar red completa en PyTorch + entrenar + diagnosticar + explicar gradientes, pérdida y arquitectura.

---

### Fase 5 — Computer Vision para robótica (3–6 meses)

**Recurso base:** OpenCV oficial

**Temario:**
Procesamiento básico de imagen, filtros, histogramas, bordes, features y matching, homografías, cámara pinhole, calibración, geometría epipolar, reconstrucción 3D, optical flow, tracking, SLAM intro
Visión profunda: clasificación, detección, segmentación, pose estimation

**Proyectos:**
- Detector de objetos en webcam
- Sistema de seguimiento
- Estimación de distancia con cámara
- Calibración real de cámara
- Percepción para robot móvil en simulación

---

### Fase 6 — Robótica matemática y física (6–9 meses)

**Recurso:** Modern Robotics

**6.1 Cinemática:** marcos de referencia, rotaciones, matrices homogéneas, cinemática directa/inversa, Jacobianos
**6.2 Dinámica:** Newton-Euler, Lagrange, ecuaciones de movimiento, fuerzas y torques
**6.3 Planeación:** espacio de configuraciones, planeación geométrica, A*, RRT/RRT*, trayectorias
**6.4 Control:** PID, espacio de estados, estabilidad, control óptimo, MPC intro

**Proyectos:**
- Brazo 2D con cinemática directa/inversa
- Simulador de péndulo invertido
- Control PID de sistema
- Planeador de trayectoria para robot móvil

---

### Fase 7 — ROS 2 y software de robótica (3–6 meses)

**Recurso:** ROS 2 official tutorials (versión Jazzy recomendada)

**Temario:**
Instalación en Linux, workspaces, packages, nodes, topics, services, actions, parameters, launch files, TF2, rosbag, URDF, RViz, Gazebo/simulación, navegación, MoveIt intro

**Proyectos:**
- Nodo publicador/suscriptor
- Servicio y acción
- Robot diferencial en simulación
- Stack de navegación básico
- Brazo robótico simple en simulación

**Meta:** Montar un sistema completo con percepción, decisión y control.

---

### Fase 8 — Control, locomoción y sistemas complejos (4–8 meses)

**Recurso:** MIT Underactuated Robotics

**Temario:**
Sistemas no lineales, estabilidad de Lyapunov, control robusto, trajectory optimization, dynamic programming, locomoción, sistemas subactuados, contacto y fricción

**Proyectos:**
- Cart-pole
- Acrobot
- Walking policy en simulación
- Trajectory optimization para brazo o robot móvil

---

### Fase 9 — Manipulación robótica (3–6 meses)

**Recurso:** MIT Robotic Manipulation (Russ Tedrake)

**Temario:**
Grasping, contact mechanics, manipulation planning, visual servoing, pick-and-place, force control, state estimation, perception for manipulation

**Proyectos:**
- Pick and place en simulación
- Clasificación + grasp pipeline
- Política de manipulación simple

---

### Fase 10 — Reinforcement Learning (4–8 meses)

**Recurso:** Sutton & Barto (referencia central)

**Temario:**
MDPs, Bellman equations, dynamic programming, Monte Carlo, TD learning, Q-learning, policy gradients, actor-critic, model-based RL, offline RL, RL para robótica

**Proyectos:**
- FrozenLake / CartPole desde cero
- DQN
- PPO
- Policy para locomoción simple
- RL en manipulación simulada

**Nota:** No empezar por RL. Llegar cuando ya seas fuerte en DL, control y simulación.

---

### Fase 11 — LLMs, agentes y autonomía (3–6 meses)

**Área de mayor interés para Carlos por su perfil.**

**Temario:**
Transformers, embeddings, fine-tuning, RAG, tool use, planning, memory, agents, VLMs, embodied AI, interfaces lenguaje-robot

**Proyectos:**
- Agente que controle simulación con lenguaje
- Sistema percepción + planner + acción
- Copiloto para robot móvil
- Pipeline multimodal: cámara + lenguaje + policy

---

### Fase 12 — Investigación y nivel "PhD-like" (permanente)

**Temario:**
Cómo leer papers, cómo reproducir papers, diseño experimental, ablation studies, benchmark design, writing técnico, revisión bibliográfica, reproducibilidad, open-source research workflow

**Objetivos:**
- Leer 2–4 papers por semana
- Reproducir al menos 1 paper al mes
- Publicar repositorios limpios
- Escribir reportes técnicos tipo paper

---

## Especializaciones Finales

| Línea | Contenido |
|-------|-----------|
| **A — AI Engineer** | DL, NLP, LLMs, agentes, sistemas multimodales |
| **B — Robotics Engineer** | ROS 2, control, planeación, percepción, manipulación |
| **C — Embodied AI (recomendada)** | Visión + LLMs + RL + Robótica + planeación + sistemas autónomos |

**Recomendación para Carlos:** Línea C — Embodied AI
Ventaja estratégica: ya viene cargado hacia software e inteligencia → montar robótica encima.

---

## Stack Técnico a Dominar

| Área | Herramientas |
|------|-------------|
| **Programación** | Python, C++, Bash, SQL básico |
| **IA** | numpy, pandas, scikit-learn, PyTorch |
| **Visión** | OpenCV |
| **Robótica** | ROS 2, Gazebo, RViz, MoveIt, URDF |
| **Ingeniería** | Git, Docker, Linux, testing, profiling |

---

## Hardware (progresivo)

| Etapa | Equipamiento |
|-------|-------------|
| **Inicial** | Laptop decente, Linux o dual boot, GPU cloud |
| **Intermedia** | PC con GPU, cámara, Raspberry Pi / Jetson Nano, sensores básicos |
| **Avanzada** | Brazo robótico educativo, robot móvil, cámara depth, IMU / LiDAR |

---

## Recursos Columna Vertebral

1. Python docs oficiales
2. MIT Linear Algebra — Gilbert Strang
3. fast.ai — Practical Deep Learning
4. PyTorch tutorials oficiales
5. Deep Learning Book — Goodfellow, Bengio, Courville
6. CS231n — Stanford (Computer Vision)
7. Modern Robotics
8. ROS 2 official tutorials
9. MIT Underactuated Robotics
10. MIT Robotic Manipulation — Russ Tedrake
11. Sutton & Barto — Reinforcement Learning

---

## Estructura Semanal Ideal

| Día | Actividad |
|-----|-----------|
| Lun, Mié, Vie | Teoría dura |
| Mar, Jue | Código |
| Sáb | Proyecto |
| Dom | Repaso + paper |

**Sesión diaria ideal:**
- 45 min teoría
- 90 min implementación
- 30 min notas / resumen
- 30 min ejercicios o debugging

---

## Tiempo Realista

| Tiempo | Nivel alcanzado |
|--------|----------------|
| 6 meses | Programar y hacer ML básico |
| 12 meses | Proyectos buenos de IA |
| 18–24 meses | Perfil muy respetable |
| 3–5 años | Nivel senior fuerte con proyectos reales, papers y sistemas complejos |

**Lo que más pesa para nivel PhD-like:**
1. Profundidad matemática
2. Papers
3. Proyectos difíciles de extremo a extremo
