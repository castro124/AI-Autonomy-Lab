# B.S. in Artificial Intelligence & Autonomous Robotics
## Programa Académico Intensivo — 8 Semestres

---

**Institución de referencia:** MIT EECS (Course 6) · Stanford AI Lab · UC Berkeley BAIR
**Duración:** 8 semestres · 24 meses (formato intensivo acelerado)
**Créditos totales:** 180 unidades
**Estado actual:** Semestre 1 — Semana 1

---

## Descripción del Programa

Programa de formación intensiva modelado sobre los currículos de MIT, Stanford y UC Berkeley en Inteligencia Artificial, Sistemas Autónomos y Robótica. El programa combina rigor matemático, implementación computacional profunda e investigación aplicada. Al graduarse, el estudiante tiene capacidad de nivel PhD-like para diseñar, construir y desplegar sistemas de IA autónoma en entornos físicos y digitales.

**Líneas de especialización:**
- **Línea A:** AI Systems Engineer (ML · DL · LLMs · Agents)
- **Línea B:** Robotics Engineer (Kinematics · Control · ROS 2 · Manipulation)
- **Línea C (objetivo):** Embodied AI Engineer — intersección de visión, lenguaje, control y autonomía

---

## YEAR 1 — Foundations & Core AI

---

### SEMESTRE 1
**Foundations of Computing & Linear Algebra I**
*Meses 1–3 · 22 unidades*

---

#### 6.100A — Introduction to Programming in Python
**Instructor:** Prof. Ana Bell — MIT EECS
**Unidades:** 5
**Descripción:** Fundamentos de programación en Python. Variables, tipos, estructuras de control, funciones, objetos, módulos, manejo de archivos y errores. Énfasis en pensar computacionalmente y resolver problemas desde cero.
**Recursos:** Python Official Docs · Exercism Python Track
**Entregables:** 40+ ejercicios progresivos · repo `python-foundations`

---

#### 6.1010 — Fundamentals of Software Engineering
**Instructor:** Prof. Adam Hartz — MIT EECS
**Unidades:** 5
**Descripción:** Terminal Linux/Bash · Git y GitHub · virtual environments · testing con pytest · PEP 8 y código limpio · estructura de proyectos profesionales.
**Recursos:** Pro Git Book · Linux Command Line
**Entregables:** Configuración de entorno profesional · workflow Git establecido

---

#### 18.06 — Linear Algebra I
**Instructor:** Prof. Gilbert Strang — MIT Mathematics
**Unidades:** 6
**Descripción:** Sistemas de ecuaciones lineales · vectores y espacios vectoriales · transformaciones lineales · matrices · eliminación gaussiana · factorizaciones LU. Base matemática de todo machine learning.
**Recursos:** MIT OCW 18.06 · Strang, *Introduction to Linear Algebra* (5th ed.)
**Entregables:** Problem sets semanales · implementaciones NumPy

---

#### 6.100L — Computing Lab I
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Lab semanal de implementación. 3 mini-proyectos en Python puro: Todo List CLI · File Organizer · Text Analyzer.
**Entregables:** 3 proyectos funcionales · documentados · en GitHub

---

**Prerrequisitos:** Ninguno
**Al completar este semestre:** Python nivel intermedio · Git fluido · bases de álgebra lineal

---

### SEMESTRE 2
**Mathematics for AI & Algorithms**
*Meses 4–6 · 22 unidades*

---

#### 18.06B — Linear Algebra II
**Instructor:** Prof. Gilbert Strang — MIT Mathematics
**Unidades:** 5
**Descripción:** Determinantes · valores y vectores propios · diagonalización · SVD (Singular Value Decomposition) · PCA. SVD y eigendecomposition son la base de redes neuronales, compresión y reducción de dimensionalidad.
**Recursos:** MIT OCW 18.06 (lectures 15–34) · 3Blue1Brown *Essence of Linear Algebra*

---

#### 18.01 — Single Variable Calculus & Optimization
**Instructor:** Prof. David Jerison — MIT Mathematics
**Unidades:** 5
**Descripción:** Derivadas · regla de la cadena · gradientes · optimización (mínimos y máximos) · descenso por gradiente. La regla de la cadena es backpropagation. El descenso por gradiente es el corazón de todo entrenamiento de redes neuronales.
**Recursos:** MIT OCW 18.01 · Khanacademy Calculus

---

#### 6.3700 — Introduction to Probability
**Instructor:** Prof. Yury Polyanskiy — MIT EECS
**Unidades:** 6
**Descripción:** Probabilidad · variables aleatorias · distribuciones (Gaussian, Bernoulli, Poisson) · esperanza · Bayes · cadenas de Markov. Todo modelo probabilístico en ML viene de aquí.
**Recursos:** MIT OCW 6.041 · *Introduction to Probability* (Bertsekas & Tsitsiklis)

---

#### 6.006 — Introduction to Algorithms
**Instructor:** Prof. Erik Demaine — MIT EECS
**Unidades:** 6
**Descripción:** Estructuras de datos · complejidad temporal/espacial (Big-O) · sorting · búsqueda · grafos · árboles · hashing · recursión. Todo ingeniero de sistemas serio domina esto.
**Recursos:** MIT OCW 6.006 · *Introduction to Algorithms* (CLRS)

---

#### 6.1810 — Operating Systems Engineering (Módulo Intensivo)
**Instructor:** Prof. Frans Kaashoek & Prof. Robert Morris — MIT EECS
**Unidades:** 4
**Formato:** Módulo intensivo de 3 semanas integrado en Semestre 2
**Descripción:** Fundamentos de sistemas operativos relevantes para AI engineering: gestión de memoria · procesos e hilos · concurrencia y race conditions · networking básico (TCP/IP, sockets) · file systems. No es el curso completo de OS — es la capa que necesita todo ingeniero que construye sistemas de IA sobre infraestructura real.
**Recursos:** MIT OCW 6.1810 (xv6) · *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau) — gratis online
**Por qué aquí:** Entender memoria y concurrencia hace mejor todo lo que viene después — ML pipelines, backends, agentes, ROS 2.

---

**Prerrequisitos:** Semestre 1
**Al completar:** Base matemática sólida para ML · algoritmos fundamentales · fundamentos de sistemas

---

## YEAR 2 — Core Machine Learning & Deep Learning

---

### SEMESTRE 3
**Machine Learning Fundamentals**
*Meses 7–9 · 24 unidades*

---

#### 6.7900 — Machine Learning
**Instructor:** Prof. Tommi Jaakkola — MIT EECS
**Unidades:** 6
**Descripción:** NumPy · pandas · matplotlib · scikit-learn · regresión lineal y logística · SVMs · árboles de decisión · random forests · clustering · PCA aplicado · pipeline de ML completo. Primer contacto real con datos.
**Recursos:** scikit-learn docs · *Hands-On Machine Learning* (Géron)

---

#### 6.s898 — Applied Machine Learning
**Instructor:** Prof. Stefanie Jegelka — MIT EECS
**Unidades:** 6
**Descripción:** ML clásico avanzado · validación cruzada · regularización (L1/L2) · feature engineering · imbalanced datasets · métricas de evaluación. Cómo construir pipelines de ML que funcionan en producción.
**Recursos:** fast.ai Practical Deep Learning (parte 1) · Kaggle Learn

---

#### 6.102 — Software Construction
**Instructor:** Prof. Rob Miller — MIT EECS
**Unidades:** 6
**Descripción:** Diseño de software · abstracciones · testing avanzado · documentación · debugging · code review. Cómo escribir código que otros (y tú mismo en 6 meses) pueden entender y mantener.
**Recursos:** MIT OCW 6.102

---

#### 6.100L — Computing Lab III
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Proyecto integrador: **machine-learning-from-scratch** — implementar regresión lineal, logística, árbol de decisión y red neuronal simple en NumPy puro, sin scikit-learn.
**Entregables:** Proyecto 1 del portafolio estratégico

---

**Prerrequisitos:** Semestres 1–2
**Al completar:** Capaz de construir y evaluar modelos ML completos desde datos crudos

---

### SEMESTRE 4
**Deep Learning Systems**
*Meses 10–12 · 24 unidades*

---

#### 6.S191 — Introduction to Deep Learning
**Instructores:** Prof. Alexander Amini & Prof. Ava Soleimany — MIT EECS
**Unidades:** 6
**Descripción:** Redes neuronales · backpropagation · PyTorch · CNNs · RNNs · regularización · optimizadores (Adam, SGD) · transfer learning · deployment básico. El curso de deep learning del MIT, mismo material que los estudiantes del MIT.
**Recursos:** introtodeeplearning.com · PyTorch Official Tutorials

---

#### 6.5940 — TinyML and Efficient Deep Learning
**Instructor:** Prof. Song Han — MIT EECS
**Unidades:** 6
**Descripción:** Arquitecturas profundas · training pipelines completos · PyTorch avanzado · quantization · pruning · model optimization. Cómo construir sistemas DL que funcionan en el mundo real.
**Recursos:** MIT OCW 6.5940 · *Deep Learning* (Goodfellow, Bengio, Courville)

---

#### 6.8301 — Advances in Computer Vision I
**Instructor:** Prof. Phillip Isola — MIT EECS
**Unidades:** 6
**Descripción:** OpenCV · procesamiento de imágenes · CNN para clasificación · arquitecturas (ResNet, VGG, EfficientNet) · detección de objetos · data augmentation. Visión computacional desde los fundamentos.
**Recursos:** CS231n (Stanford) · OpenCV Official Docs

---

#### 6.100L — Deep Learning Lab
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Proyecto 2: **deep-learning-training-pipeline** · Proyecto 3: **computer-vision-lab** (inicio).
**Entregables:** Proyectos 2 y 3 del portafolio

---

**Prerrequisitos:** Semestres 1–3
**Al completar:** PyTorch fluido · pipeline DL completo · visión básica dominada

---

## YEAR 3 — Advanced AI: Language, Agents & Vision

---

### SEMESTRE 5
**Language Models, Vision & Multi-Agent Systems**
*Meses 13–15 · 24 unidades*

---

#### CS231n — Convolutional Neural Networks for Visual Recognition
**Instructores:** Prof. Fei-Fei Li · Prof. Andrej Karpathy (Stanford)
**Unidades:** 6
**Descripción:** Visión computacional avanzada · segmentación semántica · detección (YOLO, Faster R-CNN) · tracking · visión 3D · NeRF basics. El curso de referencia mundial en computer vision.
**Recursos:** cs231n.github.io

---

#### 6.8610 — Quantitative Methods for NLP
**Instructor:** Prof. Jacob Andreas — MIT EECS
**Unidades:** 6
**Descripción:** Transformers · atención · BERT · GPT · embeddings · fine-tuning · RAG (Retrieval-Augmented Generation) · sistemas de preguntas y respuestas. LLMs desde los fundamentos matemáticos.
**Recursos:** *Attention Is All You Need* (Vaswani et al.) · Hugging Face Transformers

---

#### 6.S898 — Multi-Agent Systems & Embodied AI
**Instructor:** Prof. Leslie Pack Kaelbling — MIT CSAIL
**Unidades:** 6
**Descripción:** LangChain · LangGraph · sistemas multiagente · orquestación de agentes · tool use · memory · planning. Primer contacto directo con embodied AI.
**Recursos:** LangGraph docs · *SayCan* (Ahn et al.) · *PaLM-E* (Driess et al.)

---

#### 6.100L — AI Systems Lab
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Proyecto 4: **rag-systems-lab** · Proyecto 5: **multi-agent-systems** · Proyecto 6: **ai-automation-engine** (MVP empresarial).
**Entregables:** Proyectos 4, 5 y 6 del portafolio

---

**Prerrequisitos:** Semestres 1–4
**Al completar:** Capaz de construir sistemas LLM, agentes y pipelines de visión avanzada

---

### SEMESTRE 6
**Robotics Mathematics, Control & RL Introduction**
*Meses 16–18 · 28 unidades*

---

#### 6.832 — Underactuated Robotics
**Instructor:** Prof. Russ Tedrake — MIT CSAIL
**Unidades:** 6
**Descripción:** SE(3) y cinemática · dinámica de robots · álgebra de Lie · matrices de transformación · espacio de configuración · DH parameters. La matemática que hace posible la robótica moderna.
**Recursos:** underactuated.mit.edu · *Modern Robotics* (Lynch & Park)

---

#### 6.4210 — Robotic Manipulation
**Instructor:** Prof. Russ Tedrake — MIT CSAIL
**Unidades:** 6
**Descripción:** Cinemática directa e inversa · Jacobiano · dinámica de manipuladores · control PID · control adaptativo · planning en espacio de configuración.
**Recursos:** manipulation.mit.edu

---

#### 6.302 — Dynamics and Control Systems
**Instructor:** Prof. Alexandre Megretski — MIT EECS
**Unidades:** 6
**Descripción:** Sistemas de control · transformada de Laplace · controladores PID · estabilidad · control moderno (LQR, MPC) · control de robots físicos.
**Recursos:** MIT OCW 6.302

---

#### 6.100L — Robotics Math Lab
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Implementación de cinemática forward/inverse en Python · visualización de transformaciones · simulación básica en PyBullet.
**Entregables:** Inicio Proyecto 7: **robotics-simulation-lab**

---

#### 6.7950 intro — Introduction to Reinforcement Learning
**Instructor:** Prof. Alborz Geramifard — MIT EECS
**Unidades:** 4
**Formato:** Módulo introductorio de 3 semanas — profundización completa en Semestre 8
**Descripción:** MDPs · Bellman equations · Q-learning · política y valor · exploración vs explotación. Introducción aquí porque RL conecta directamente con control robótico y toma de decisiones en entornos físicos. Ver los conceptos junto a robótica hace que ambos se entiendan mejor.
**Recursos:** Sutton & Barto capítulos 1–6 · *Reinforcement Learning* (gratis online)

---

**Prerrequisitos:** Semestres 1–5
**Al completar:** Matemática robótica dominada · manipuladores · introducción sólida a RL

---

## YEAR 4 — Autonomous Systems & Research

---

### SEMESTRE 7
**Autonomous Robotic Systems**
*Meses 19–21 · 24 unidades*

---

#### 6.4200 — Robotics Science and Systems
**Instructor:** Prof. Luca Carlone — MIT CSAIL
**Unidades:** 6
**Descripción:** ROS 2 completo · nodos · topics · services · actions · URDF · TF2 · Nav2 · MoveIt · integración sensor-actuador. El framework estándar de la industria robótica.
**Recursos:** ROS 2 Jazzy Official Docs · The Construct ROS 2

---

#### 6.141 — Robotics: Science and Systems Lab
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Simulación en Gazebo y MuJoCo · integración ROS 2 + simulación · SLAM basics · navegación autónoma en entornos simulados · deploy en hardware (Raspberry Pi / Jetson).
**Recursos:** Gazebo Docs · MuJoCo Docs

---

#### 6.8210 — Planning & Navigation for Autonomous Systems
**Instructor:** Prof. Nicholas Roy — MIT CSAIL
**Unidades:** 6
**Descripción:** Path planning (A*, RRT, RRT*) · SLAM · mapas de ocupación · motion planning bajo incertidumbre · navegación con obstáculos dinámicos.
**Recursos:** Nav2 Docs · *Planning Algorithms* (LaValle)

---

#### 6.5840 — Distributed Systems (Módulo Intensivo)
**Instructor:** Prof. Robert Morris & Prof. Frans Kaashoek — MIT EECS
**Unidades:** 4
**Formato:** Módulo intensivo de 4 semanas integrado en Semestre 7
**Descripción:** RPC · consensus algorithms · Raft · fault tolerance · replicación · microservices · sistemas distribuidos en la práctica. Esencial para construir el AI Operating System — un sistema que orquesta agentes, modelos y datos a escala necesita entender cómo los sistemas distribuidos manejan fallas, consistencia y coordinación.
**Recursos:** MIT 6.5840 (antes 6.824) — labs en Go disponibles online · *Designing Data-Intensive Applications* (Kleppmann)
**Conexión directa:** AI Operating System (Proyecto 10) usa estos principios en su arquitectura.

---

#### 6.100L — Autonomous Systems Lab
**Instructor:** Staff
**Unidades:** 6
**Descripción:** Proyecto 8: **autonomous-robot-system** — robot navegando autónomamente en Gazebo con ROS 2, SLAM, evitación de obstáculos.
**Entregables:** Proyecto 8 del portafolio

---

**Prerrequisitos:** Semestres 1–6
**Al completar:** Capaz de construir sistemas robóticos autónomos con ROS 2 · fundamentos de sistemas distribuidos

---

### SEMESTRE 8
**Research, Reinforcement Learning & Capstone**
*Meses 22–24 · 24 unidades*

---

#### CS285 — Deep Reinforcement Learning
**Instructor:** Prof. Sergey Levine — UC Berkeley
**Unidades:** 6
**Descripción:** MDPs · Q-learning · policy gradients · PPO · actor-critic · model-based RL · RL para robótica. El curso de RL más riguroso disponible públicamente.
**Recursos:** rail.eecs.berkeley.edu/deeprlcourse · *Reinforcement Learning* (Sutton & Barto)

---

#### 6.S894 — Embodied AI Systems (Seminar)
**Instructor:** Prof. Antonio Torralba — MIT CSAIL
**Unidades:** 6
**Descripción:** Lectura y reproducción de papers fundacionales: RT-1, RT-2, PaLM-E, SayCan, Gato. Embodied AI como intersección de visión, lenguaje, planificación y control físico. Seminario de investigación.
**Recursos:** arXiv · Papers With Code · Semantic Scholar
**Papers clave:** RT-1 (2022) · RT-2 (2023) · PaLM-E (2023) · SayCan (2022) · Gato (2022)

---

#### 6.ThG — Capstone Project: AI Operating System
**Instructor:** Committee
**Unidades:** 6
**Descripción:** Proyecto 9: **embodied-ai-agent** · Proyecto 10: **ai-operating-system** — primer prototipo del producto central de la empresa. Defensa oral grabada ante committee.
**Tres componentes obligatorios del capstone:**
1. **Arquitectura distribuida** — microservices, orquestación de agentes, API gateway
2. **Observabilidad** — logs estructurados, métricas, tracing distribuido (OpenTelemetry)
3. **Deployment real** — Docker, CI/CD, cloud deployment (AWS o GCP)
**Entregables:** Proyectos 9 y 10 · defensa oral · paper técnico de 8 páginas · sistema deployado en producción

---

#### 6.UAR — Undergraduate Advanced Research
**Instructor:** Investigador asignado
**Unidades:** 6
**Descripción:** UROP-style research. Reproducir un paper de embodied AI, extenderlo con una contribución propia, escribir el reporte técnico.

---

**Prerrequisitos:** Semestres 1–7
**Al completar:** Nivel 4–5 del sistema de evaluación · portafolio completo · producto funcional

---

## Curriculum Transversal
*Corre en paralelo durante todo el programa*

| Actividad | Inicio | Frecuencia |
|-----------|--------|------------|
| Research Notebook (research-log.md) | Mes 1 | Diario |
| Comunidad técnica (Twitter/X, Discord, Papers with Code) | Mes 1 | 15 min/día |
| Business Track (customer discovery → producto) | Mes 1 | 5h/semana |
| Kaggle competitions (solo Semestres 3–4) | Mes 9 | 1 competencia/semestre |
| Reading papers (arXiv, Papers With Code) | Mes 10 | 1/semana |
| Cloud computing + GPU (Google Colab → Vast.ai → AWS/GCP) | Mes 10 | Según necesidad |
| Paper reading intensivo | Mes 16 | 2/semana |
| C++ para sistemas de alto rendimiento | Mes 16 | 3h/semana |
| Paper reproduction | Mes 18 | 1/mes |

---

## Adiciones Estratégicas al Plan

### 1. Cloud Computing & GPU Access — Mes 10
Cuando arranque deep learning, el hardware local (Mac sin GPU NVIDIA) es insuficiente para entrenar modelos reales.

**Progresión de infraestructura:**
| Etapa | Herramienta | Costo | Cuándo |
|-------|-------------|-------|--------|
| Exploración | Google Colab (gratis) | $0 | Mes 10–11 |
| Experimentos reales | Vast.ai / Lambda Labs | $0.30–1.50/hr GPU | Mes 11–15 |
| Producción | AWS / GCP créditos estudiantiles | Variable | Mes 15+ |

**Acción antes del Mes 10:** Crear cuenta en Google Colab Pro, Vast.ai y solicitar créditos de AWS Activate o GCP for Startups.

---

### 2. Kaggle — Structured Competition Track
Kaggle es verificación pública de habilidades reales. Un leaderboard position es más convincente que cualquier certificado.

**Calendario de competencias:**
| Semestre | Tipo de competencia | Objetivo |
|----------|---------------------|----------|
| 3 (Mes 9) | Tabular data (Getting Started) | Familiarización, top 50% |
| 4 (Mes 12) | Computer Vision (clasificación) | Top 30% |
| 5 (Mes 15) | NLP / LLMs | Top 25% |
| 6–8 | Featured competitions | Top 20% o medalla |

**Recursos:** kaggle.com · Kaggle Learn (gratuito) · Notebooks públicos

---

### 3. Comunidad Técnica — Desde Ahora
El equivalente al network de un MIT student, construido intencionalmente.

**Twitter/X — Seguir desde hoy:**
- @karpathy (Andrej Karpathy — ex Stanford/Tesla/OpenAI)
- @ylecun (Yann LeCun — Meta AI, Turing Award)
- @RusstedrakeRob (Russ Tedrake — MIT)
- @svlevine (Sergey Levine — Berkeley)
- @pieterabbeel (Pieter Abbeel — Berkeley)
- @GaryMarcus (crítico de AI — perspectiva balanceada)
- @paperswithcode (estado del arte en papers)

**Discord/Comunidades:**
- Hugging Face Community Discord
- fast.ai Forums
- ROS Discourse (foros oficiales ROS 2)
- r/MachineLearning · r/robotics

**Hábito diario (15 min):**
Leer 3–5 tweets técnicos o un abstract de paper en Papers with Code. No es estudio — es exposición constante al ecosistema. Esto te mantiene actualizado sobre qué está pasando en el campo sin interrumpir el estudio profundo.

---

## Exámenes y Evaluaciones

| Evaluación | Frecuencia | Formato |
|------------|------------|---------|
| Problem sets | Semanal | Código + matemáticas |
| Lab checkpoints | Quincenal | Code review |
| Midterm | Por semestre | Teórico + implementación |
| Final exam | Por semestre | Problema abierto + defensa |
| Examen trimestral | Cada 3 meses | Teórico + código + mini-proyecto + defensa oral grabada |

**Sistema de niveles de evaluación:**

| Nivel | Criterio |
|-------|----------|
| 1 | Entiende conceptos, hace notebooks |
| 2 | Implementa proyectos sin tutorial completo |
| 3 | Lee docs oficiales, corrige y optimiza |
| **4** | Reproduce papers, diseña sistemas propios |
| **5** | Construye productos, research repos, arquitectura propia |

**Meta: Nivel 4–5 al graduarse**

---

## Portafolio — 11 Proyectos Estratégicos

| # | Proyecto | Semestre | Conexión empresa |
|---|---------|----------|-----------------|
| 1 | machine-learning-from-scratch | 3 | — |
| 2 | deep-learning-training-pipeline | 4 | — |
| 3 | computer-vision-lab | 4–5 | — |
| 4 | rag-systems-lab | 5 | — |
| 5 | multi-agent-systems | 5 | — |
| 6 | ai-automation-engine | 5 | **MVP ventas** |
| 7 | robotics-simulation-lab | 6 | — |
| 8 | autonomous-robot-system | 7 | — |
| 9 | embodied-ai-agent | 8 | — |
| 10 | ai-operating-system | 8 | **Producto central** |
| 11 | paper-reproduction-repo *(opcional)* | 6–8 | — |

**Proyecto 11 — paper-reproduction-repo:**
Repo público donde implementas los papers más importantes del campo desde cero:
- Transformer (Vaswani et al., 2017) — la arquitectura que cambió todo
- DQN (Mnih et al., 2015) — deep RL jugando Atari
- RT-1 (Brohan et al., 2022) — el primer robot transformer
Este repo es el que más impresiona a investigadores y equipos técnicos de alto nivel.

---

## Estado Actual

```
Semestre:    1 de 8
Mes:         1 de 24
Semana:      1 de 4
Día:         1
Curso activo: 6.100A — Introduction to Programming in Python
Ejercicio:   05/40 completados
Commit:      c0a39b3 ✅
```

---

*Programa diseñado sobre los currículos de MIT EECS, Stanford AI Lab y UC Berkeley BAIR.*
*Todos los cursos referenciados son reales y accesibles públicamente.*
