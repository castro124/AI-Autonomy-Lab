# Stack Tecnológico de Élite — AI/Robotics/Agents Engineer

El stack que usan ingenieros que trabajan en IA avanzada, agentes, visión y robótica.
Organizado en capas: fundamentos → producción → especialización.

---

## 1. Lenguajes de Programación

### Python (obligatorio — lenguaje principal)
Dominio en:
- Programación avanzada (async, tipado, optimización)
- Librerías científicas: numpy, pandas, matplotlib
- Ecosistemas: ML, DL, visión, agentes, ciencia de datos

### C++ (lenguaje secundario — crítico para robótica)
Necesario para:
- ROS 2 (nodos en C++ son la norma en producción)
- Sistemas de alto rendimiento
- Motores de simulación
- Control en tiempo real

Debes saber: memoria, punteros, compilación, CMake

### Rust (opcional — infraestructura)
Cada vez más usado para:
- Infraestructura de IA
- Sistemas seguros y de alto rendimiento
- Herramientas de bajo nivel

---

## 2. Matemáticas (base no negociable)

| Área | Para qué sirve |
|------|----------------|
| Álgebra lineal | Redes neuronales, visión, cinemática |
| Cálculo multivariable | Gradientes, optimización, entrenamiento |
| Probabilidad y estadística | ML, inferencia, evaluación de modelos |
| Optimización matemática | Entrenamiento, planificación, control |

---

## 3. Machine Learning Clásico

| Herramienta | Uso |
|-------------|-----|
| **NumPy** | Computación numérica |
| **pandas** | Manipulación y análisis de datos |
| **scikit-learn** | Modelos clásicos: regresión, clasificación, clustering |
| matplotlib / seaborn | Visualización |

---

## 4. Deep Learning

**Framework principal: PyTorch**

Estándar actual para investigación, visión, LLMs, robótica.

Dominar:
- Tensors y operaciones
- Autograd (diferenciación automática)
- Training loops modulares
- Optimización de entrenamiento
- `torch.compile` para acelerar

---

## 5. Computer Vision

| Herramienta | Uso |
|-------------|-----|
| **OpenCV** | Procesamiento de imágenes, detección, tracking clásico |
| **PyTorch + torchvision** | Modelos profundos de visión |
| Detectron2 / YOLO | Detección de objetos |
| Segment Anything (SAM) | Segmentación avanzada |

Pipeline típico: OpenCV (preprocesamiento) → PyTorch (modelo profundo) → postprocesamiento

---

## 6. LLMs y Agentes

| Herramienta | Uso |
|-------------|-----|
| **Transformers (Hugging Face)** | Modelos de lenguaje |
| **LangChain** | Framework para sistemas con LLMs |
| **LangGraph** | Orquestación de agentes con estado |
| **LlamaIndex** | Sistemas RAG |
| OpenAI API | Acceso a modelos de frontera |

---

## 7. Bases de Datos

### Vector Databases (para embeddings y RAG)
- **Chroma** — local, simple, ideal para desarrollo
- **Pinecone** — cloud, producción
- **Weaviate** — flexible, open-source
- **Qdrant** — alto rendimiento, open-source

### Bases relacionales
- **PostgreSQL** — estándar para SaaS y backend de IA

---

## 8. Backend y APIs

**FastAPI** — estándar para APIs de IA

Ideal para:
- APIs que sirven modelos de ML
- Microservicios de agentes
- Sistemas de autonomía operativa

Complementos: Pydantic (validación), SQLAlchemy (ORM)

---

## 9. DevOps e Infraestructura

| Herramienta | Necesidad |
|-------------|-----------|
| **Docker** | Contenedores, despliegue reproducible |
| **Git** | Control de versiones (obligatorio) |
| **Linux** | Sistema operativo dominante en IA y robótica |
| pytest | Testing |
| MLflow / W&B | Experiment tracking |
| GitHub Actions | CI/CD básico |

---

## 10. Robótica

**ROS 2** — sistema operativo robótico

Usado en:
- Robots industriales
- Investigación
- Drones y vehículos autónomos

Stack completo:
- ROS 2 Jazzy
- TF2 (transformaciones)
- URDF (descripción de robots)
- MoveIt 2 (manipulación)
- Nav2 (navegación)

---

## 11. Simulación

| Herramienta | Uso |
|-------------|-----|
| **Gazebo (Harmonic)** | Simulación robótica + ROS 2 |
| **MuJoCo** | Simulación física avanzada, RL |
| **PyBullet** | Simulación física, RL, fácil de usar |
| **Isaac Sim (NVIDIA)** | Simulación con GPU, foto-realista |

---

## 12. Reinforcement Learning

| Herramienta | Uso |
|-------------|-----|
| **Stable Baselines3** | Algoritmos clásicos de RL (PPO, SAC, TD3) |
| **RLlib** | RL a escala, distribuido |
| Gymnasium (OpenAI Gym) | Entornos estándar para RL |

Conceptos a dominar: policy gradient, Q-learning, PPO, SAC, model-based RL

---

## 13. Hardware (etapa avanzada)

- **NVIDIA Jetson** — edge AI con GPU
- **Raspberry Pi** — robótica educativa y prototipado
- Cámaras depth (Intel RealSense, DepthAI)
- IMU / LiDAR según especialización

---

## Stack Completo Resumido

```
LENGUAJES
Python (principal) · C++ (robótica) · Rust (opcional)

MATEMÁTICAS
Álgebra lineal · Cálculo · Probabilidad · Optimización

ML CLÁSICO
NumPy · pandas · scikit-learn

DEEP LEARNING
PyTorch

COMPUTER VISION
OpenCV · PyTorch Vision

LLMs / AGENTES
Transformers · LangChain · LangGraph · LlamaIndex

BASES DE DATOS
Chroma/Pinecone/Qdrant · PostgreSQL

BACKEND
FastAPI · Pydantic

INFRAESTRUCTURA
Docker · Git · Linux · pytest · MLflow/W&B

ROBÓTICA
ROS 2 · MoveIt · Nav2 · TF2 · URDF

SIMULACIÓN
Gazebo · MuJoCo · PyBullet

RL
Stable Baselines3 · RLlib · Gymnasium
```

---

## Sistemas que este stack permite construir

**Arquitectura 1 — Embodied AI:**
```
Vision (OpenCV/PyTorch) → LLM Planner (LangGraph) → Actions (ROS 2)
```

**Arquitectura 2 — Autonomía operativa:**
```
Perception → Planning → Control
```

**Arquitectura 3 — AI Operating System:**
```
Input → Multi-agent system (LangGraph) → Tools/APIs → Output
```

---

## Perfil que esto crea

Si dominas este stack y construyes proyectos reales:
- **AI Systems Architect**
- **Autonomy Systems Engineer**
- **Embodied AI Researcher/Engineer**

Perfiles extremadamente demandados y raros.

---

## Secuencia de aprendizaje (alineada al plan de 24 meses)

```
1. Python
2. Matemáticas
3. ML (NumPy, pandas, scikit-learn)
4. Deep Learning (PyTorch)
5. Computer Vision (OpenCV + PyTorch)
6. LLMs y agentes (Transformers, LangGraph)
7. Robótica (ROS 2, cinemática, control)
8. RL (Stable Baselines3, MuJoCo)
```

**Regla:** No aprender todo al mismo tiempo. Cada herramienta tiene su momento en el plan.
