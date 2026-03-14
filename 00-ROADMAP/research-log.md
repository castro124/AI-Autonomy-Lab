# Research Log — Carlos Castro
*Un investigador sin cuaderno de notas no es investigador.*

---

## Cómo usar este archivo

Cada día que estudies, abres este archivo y escribes.
No importa si es mucho o poco. Lo que importa es el hábito.

**Estructura de cada entrada:**
```
## YYYY-MM-DD

**Qué aprendí hoy:**
...

**Qué me confundió:**
...

**Ideas de sistemas:**
...

**Ideas de negocio / producto:**
...

**Preguntas abiertas para investigar:**
...
```

---

## Por qué importa

Los mejores investigadores del mundo llevan cuadernos de notas.
Feynman los llevaba. Turing los llevaba. Los investigadores de DeepMind los llevan.

No para recordar lo que aprendieron — para **pensar**.
Escribir fuerza la claridad. Si no puedes escribirlo, no lo entiendes todavía.

Con el tiempo este log se convierte en:
- Un mapa de tu evolución intelectual
- Una fuente de ideas para papers y proyectos
- Evidencia de pensamiento sistemático (impresiona en entrevistas)

---

## Entradas

---

## 2026-03-13

**Qué aprendí hoy:**
- Variables en Python: nombres que apuntan a objetos en memoria (no son el objeto)
- 4 tipos fundamentales: str, int, float, bool
- Operadores aritméticos: +, -, *, /, //, %, **
- La diferencia entre / (siempre float) y // (floor division, int)
- Strings: indexing base-cero, índices negativos, slicing [inicio:fin:paso]
- input() siempre devuelve string — type casting necesario para aritmética
- int(), float(), str() — conversión de tipos
- f-strings: la forma moderna de formatear texto en Python

**Qué me confundió:**
- Al principio no entendía por qué edad + 10 fallaba si edad venía de input()
  → Lo resolví probando el error intencionalmente. TypeError: can't concat str to int.

**Ideas de sistemas:**
- Un programa que recibe datos del usuario y hace cálculos podría ser la base
  de cualquier formulario de intake de cliente (clínica, despacho legal)

**Ideas de negocio / producto:**
- Las clínicas tienen formularios de admisión en papel o PDFs
  → Un sistema que digitaliza ese proceso con input validado podría ser
  el primer módulo del AI OS

**Preguntas abiertas:**
- ¿Cómo maneja Python strings en memoria? ¿Immutable significa que crea nuevo objeto cada vez?
- ¿Qué pasa si hago float("abc")? → ValueError (lo probaré mañana)

---
