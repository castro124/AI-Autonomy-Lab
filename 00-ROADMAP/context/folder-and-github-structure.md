# Estructura de Carpetas y GitHub — AI-Autonomy-Lab

---

## Carpeta raíz local: AI-Autonomy-Lab

Dividida en 3 niveles conceptuales:
- **Universidad personal** → teoría y estudio
- **Laboratorio** → experimentos y práctica
- **Portafolio público** → repositorios limpios en GitHub

```
AI-Autonomy-Lab/
│
├── 00-ROADMAP/
├── 01-FOUNDATIONS/
├── 02-MACHINE-LEARNING/
├── 03-DEEP-LEARNING/
├── 04-COMPUTER-VISION/
├── 05-LLMS-AGENTS/
├── 06-ROBOTICS/
├── 07-REINFORCEMENT-LEARNING/
├── 08-EMBODIED-AI/
├── 09-PAPERS/
├── 10-PROJECTS/
├── 11-CAPSTONE/
├── 12-NOTES/
├── 13-DATASETS/
└── 14-TOOLS/
```

---

## Detalle de cada carpeta

### 00-ROADMAP
```
00-ROADMAP/
├── master-roadmap.md       ← visión 5-10 años + áreas a dominar
├── 24-month-plan.md
├── weekly-plan.md
├── learning-goals.md
└── progress-tracker.md     ← estado de cada mes (✔/□)
```

**progress-tracker.md formato:**
```markdown
Month 1
✔ Python basics
✔ Git
✔ Linux

Month 2
✔ Data structures
□ Algorithms
```

---

### 01-FOUNDATIONS
```
01-FOUNDATIONS/
├── python/
│   ├── notes.md
│   ├── exercises/
│   ├── mini-projects/
│   └── resources.md
├── algorithms/
├── linear-algebra/
├── calculus/
└── probability/
```

---

### 02-MACHINE-LEARNING
```
02-MACHINE-LEARNING/
├── theory/
│   ├── regression.md
│   ├── classification.md
│   ├── clustering.md
│   └── model-evaluation.md
├── notebooks/
├── exercises/
└── projects/
```

---

### 03-DEEP-LEARNING
```
03-DEEP-LEARNING/
├── theory/
├── pytorch/
├── architectures/
│   ├── mlp.md
│   ├── cnn.md
│   ├── rnn.md
│   └── transformers.md
├── experiments/
└── notebooks/
```

---

### 04-COMPUTER-VISION
```
04-COMPUTER-VISION/
├── theory/
├── opencv/
├── cnn-vision/
├── detection/
└── projects/
```

---

### 05-LLMS-AGENTS
```
05-LLMS-AGENTS/
├── theory/
├── transformers/
├── rag/
├── agents/
├── langgraph/
└── experiments/
```

---

### 06-ROBOTICS
```
06-ROBOTICS/
├── robotics-math/
├── kinematics/
├── dynamics/
├── control/
├── ros2/
│   ├── notes.md
│   ├── tutorials/
│   ├── experiments/
│   └── projects/
└── simulation/
```

---

### 07-REINFORCEMENT-LEARNING
```
07-REINFORCEMENT-LEARNING/
├── theory/
├── q-learning/
├── policy-gradient/
├── ppo/
└── experiments/
```

---

### 08-EMBODIED-AI
```
08-EMBODIED-AI/
├── research/
├── architectures/
├── multimodal-agents/
└── experiments/
```

---

### 09-PAPERS
```
09-PAPERS/
├── ai/
├── robotics/
├── agents/
├── rl/
└── summaries/
```

**Estructura por paper:**
```
paper-name/
├── paper.pdf
├── notes.md
└── reproduction/
```

---

### 10-PROJECTS (proyectos pequeños / medios)
```
10-PROJECTS/
├── ml-projects/
├── vision-projects/
├── llm-projects/
├── robotics-projects/
└── experiments/
```

---

### 11-CAPSTONE (proyectos grandes)
```
11-CAPSTONE/
├── project-1/
├── project-2/
└── final-system/       ← "autonomous-agent-system"
```

---

### 12-NOTES (base de conocimiento personal)
```
12-NOTES/
├── concepts/
│   ├── backpropagation.md
│   ├── attention.md
│   ├── transformers.md
│   └── reinforcement-learning.md
├── cheatsheets/
├── summaries/
└── diagrams/
```

---

### 13-DATASETS
```
13-DATASETS/
├── raw/
├── processed/
└── experiments/
```

---

### 14-TOOLS
```
14-TOOLS/
├── docker/
├── scripts/
├── environments/
└── setup-guides/
```

---

## Daily Log

Archivo `daily-log.md` para acelerar el aprendizaje:

```markdown
2026-03-13

Estudié:
- NumPy broadcasting
- Regresión lineal

Hice:
- Notebook regression
- Ejercicios

Problemas:
- Entender gradiente

Mañana:
- Repasar cálculo
```

---

## GitHub — Estructura de Repos

### Filosofía
GitHub = portafolio profesional + laboratorio de ingeniería.
Si alguien (inversionista, socio, ingeniero senior) entra al perfil, debe ver inmediatamente un constructor serio de sistemas de IA y autonomía.

### 3 capas de repositorios

**Capa 1 — Foundations (bases técnicas)**
```
python-foundations         ← estructuras, algoritmos, patrones
math-for-ai                ← álgebra lineal, cálculo, prob, optimización (con notebooks)
machine-learning-from-scratch ← ML sin librerías (solo NumPy)
```

**Capa 2 — Systems (sistemas reales)**
```
deep-learning-pytorch      ← training pipelines, architectures, experiment tracking
computer-vision-lab        ← clasificación, detección, segmentación, tracking
llm-agents-lab             ← RAG, tool use, multi-agent, planning agents
ai-automation-systems      ← lead qualification, sales agents, workflow automation
```

**Capa 3 — Robotics**
```
robotics-foundations       ← cinemática, dinámica, control, motion planning (simulaciones)
ros2-lab                   ← nodes, navigation, sensors, simulation
robot-vision               ← perception, camera calibration, SLAM, visual servoing
reinforcement-learning-lab ← Q-learning, DQN, policy gradient, PPO
embodied-ai-systems        ← perception, planning, control, experiments
```

**Capa 4 — Flagship Projects**
```
autonomous-agent-platform  ← sistema multiagente (agent-core, planning, memory, tools)
ai-operating-system        ← PRODUCTO REAL (agents, workflows, integrations, dashboard)
embodied-autonomy-system   ← sistema grande (perception, planning, navigation, control)
```

---

## Perfil GitHub ideal (pinned repos)
```
autonomous-agent-platform
ai-operating-system
computer-vision-lab
deep-learning-pytorch
robotics-foundations
embodied-ai-systems
```

## README del perfil
```markdown
AI Systems Builder

Focus:
- AI agents
- Autonomy systems
- Computer vision
- Robotics
- Embodied AI

Projects:
- autonomous-agent-platform
- ai-operating-system
- computer-vision-lab
```

---

## Workflow de estudio → publicación

```
1. APRENDER     → notas en NOTES/
2. PRACTICAR    → ejercicios en EXERCISES/
3. EXPERIMENTAR → experimentos en EXPERIMENTS/
4. CREAR        → proyecto en PROJECTS/
5. PUBLICAR     → repo limpio en GitHub
```

**Qué hace un repo impresionante:**
1. Código limpio
2. Buenos READMEs
3. Demos
4. Diagramas de arquitectura
5. Explicaciones claras

---

## Calendario de creación de repos (alineado al plan de 24 meses)

| Meses | Repo a crear |
|-------|-------------|
| 1–2 | python-foundations |
| 3–6 | math-for-ai |
| 7–9 | machine-learning-from-scratch |
| 10–12 | deep-learning-pytorch + computer-vision-lab |
| 13–15 | llm-agents-lab |
| 16–18 | robotics-foundations |
| 19–20 | ros2-lab |
| 21–22 | robot-vision + reinforcement-learning-lab |
| 23–24 | embodied-ai-systems + ai-operating-system (capstone) |
