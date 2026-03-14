# Sistema de Estudio de Alto Rendimiento
## MIT-Style Deep Work — Carlos Castro

---

## Principio Central

El aprendizaje técnico profundo no se mide en horas vistas ni en cursos completados.
Se mide en **problemas resueltos, código escrito y conceptos que puedes explicar sin notas**.

---

## Estructura del Día

4 bloques de deep work. Sin multitasking. Sin interrupciones dentro de cada bloque.

```
08:00 – 10:00   Bloque 1 — Matemáticas / Teoría dura
10:30 – 12:30   Bloque 2 — Programación
13:30 – 16:00   Bloque 3 — Proyecto
16:30 – 18:00   Bloque 4 — Lectura técnica / Debugging
```

**Total efectivo: 8–9 horas reales.**

---

### Bloque 1 — Matemáticas o Teoría Dura (2h)
Álgebra lineal · cálculo · probabilidad · algoritmos · papers teóricos.

**Regla:** Resolver problemas a mano, no solo leer. Leer sin resolver es pasivo y no consolida.
La comprensión se prueba cuando puedes derivar el resultado desde cero en papel.

---

### Bloque 2 — Programación (2h)
Python · estructuras de datos · implementaciones desde cero.

**Regla:** 20% leer, 80% programar. Nunca más teoría que código en este bloque.
Si llevas 30 minutos sin escribir código, algo está mal.

---

### Bloque 3 — Proyecto (2–3h)
Aquí ocurre el aprendizaje real. Proyectos del portafolio, mini-proyectos del curso, problem sets.

**Regla:** El proyecto tiene que estar roto al inicio del bloque y funcionando al final.
Si nunca se rompe, no estás trabajando en el límite de tu capacidad.

---

### Bloque 4 — Lectura Técnica / Debugging (1.5–2h)
Documentación oficial · papers · debugging de lo que se rompió en el Bloque 3 · optimización.

Este bloque es mentalmente más ligero. Úsalo para consolidar, no para aprender cosas nuevas.

---

## Estructura Semanal

| Día | Foco |
|-----|------|
| Lunes | Teoría nueva — primer contacto con el concepto |
| Martes | Problemas matemáticos — formalizar lo del lunes |
| Miércoles | Implementación — código del concepto |
| Jueves | Proyecto — aplicar en contexto real |
| Viernes | Debugging y optimización |
| Sábado | Paper reading + revisión semanal |
| Domingo | Descanso o revisión ligera |

---

## Secuencia de Aprendizaje por Concepto

Para cada concepto nuevo, sigue este orden sin saltarte pasos:

```
1. Intuición      → ¿Qué está pasando a nivel conceptual?
2. Matemáticas    → ¿Cómo se formaliza?
3. Implementación → ¿Cómo se convierte en código?
4. Aplicación     → ¿Dónde se usa en un sistema real?
```

**Ejemplo — Gradient Descent:**

```
Intuición:
  Moverse en la dirección donde la función disminuye más rápido.
  Como bajar una montaña siguiendo siempre la pendiente más pronunciada.

Matemáticas:
  θ = θ − α · ∇J(θ)
  donde α es el learning rate y ∇J(θ) es el gradiente de la función de pérdida.

Implementación:
  def gradient_descent(X, y, lr=0.01, epochs=1000):
      theta = np.zeros(X.shape[1])
      for _ in range(epochs):
          gradient = X.T @ (X @ theta - y) / len(y)
          theta -= lr * gradient
      return theta

Aplicación:
  Entrenar cualquier modelo de ML/DL — regresión, redes neuronales, todo.
```

Si falta alguna de las cuatro capas, el conocimiento no está consolidado.

---

## Sistema de Notas

Estructura para cada concepto en tus notas:

```markdown
## [Nombre del concepto]

**Intuición:**
...

**Matemáticas:**
...

**Código:**
```python
...
```

**Aplicación:**
...

**Errores comunes:**
...

**Conexión con otros conceptos:**
...
```

Notas así se convierten en referencia real, no en transcripción pasiva.

---

## Sistema de Papers (desde Mes 10)

**Frecuencia:** 1 paper/semana → 2/semana desde Mes 16

**Estructura de lectura para cada paper:**

```
1. Abstract + Conclusion primero  → ¿Cuál es la idea central?
2. Introduction                   → ¿Qué problema resuelve?
3. Method                         → ¿Cómo lo resuelve?
4. Key idea                       → ¿Qué es lo genuinamente nuevo?
5. Results                        → ¿Funciona? ¿Métricas?
6. Limitations                    → ¿Qué no resuelve?
```

**Paper Reproduction Ladder:**

| Nivel | Actividad |
|-------|-----------|
| 1 | Implementar el método en notebook propio |
| 2 | Reproducir los resultados del paper |
| 3 | Modificar la arquitectura y ver qué pasa |
| 4 | Proponer una mejora propia |
| 5 | Publicar el repo o escribir el paper |

Desde Mes 18: al menos 1 reproducción al mes.

---

## Sistema de Proyectos

Cada proyecto del portafolio sigue esta estructura:

```
1. Idea           → ¿Qué problema resuelve?
2. Architecture   → Diagrama de componentes antes de escribir código
3. Implementation → Código modular, funciones pequeñas, tests
4. Debugging      → Parte del proceso, no señal de fallo
5. Documentation  → README profesional, instrucciones de instalación y uso
```

**Regla del README:** Un buen README es casi tan importante como el código.
Si alguien no puede entender tu proyecto en 5 minutos leyendo el README, el proyecto no está terminado.

---

## Revisión Semanal

Cada sábado, antes del paper reading, abres `weekly-review.md` y respondes:

```markdown
## Semana [N] — [fecha]

**Aprendí:**
-
-

**Me confundió:**
-

**Implementé:**
-

**Queda pendiente:**
-

**Nivel de energía de la semana (1-10):**

**¿Qué haría diferente?**
```

Esto no es opcional. Sin revisión semanal no hay ajuste de estrategia.

---

## Indicadores de Progreso Real

**Señales de que estás avanzando:**
- Lees documentación oficial sin miedo
- Implementas cosas sin tutorial paso a paso
- Entiendes papers parcialmente (y cada semana un poco más)
- El debugging te resulta natural, no frustrante
- Puedes explicar un concepto a alguien que no lo conoce

**Señales de alerta — cambia de estrategia si:**
- Solo consumes videos sin escribir código
- Copias código sin entender cada línea
- No tienes proyectos propios en GitHub
- Nunca te sientes confundido (significa que no estás en el límite)

---

## Regla Mental Fundamental

```
Confusión   → normal, significa que estás aprendiendo algo nuevo
Errores     → normales, son información sobre qué no entiendes aún
Debugging   → parte del proceso de ingeniería, no señal de fallo
Frustración → normal al inicio de cada tema difícil
```

Los estudiantes de ingeniería de alto rendimiento no sienten menos confusión que los demás.
La diferencia es que la confusión no los detiene — la usan como señal de dónde trabajar más.

---

## Proporción Fundamental

```
30% teoría
70% práctica
```

Si inviertes eso, el conocimiento nunca se convierte en habilidad.

---

*Documento parte del programa B.S. in AI & Autonomous Robotics — Carlos Castro*
