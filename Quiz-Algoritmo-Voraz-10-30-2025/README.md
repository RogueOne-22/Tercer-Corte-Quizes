# 🧠 Algoritmo Voraz

Un **algoritmo voraz** es una técnica de optimización que **toma decisiones locales óptimas**, esperando que esas decisiones lleven a una **solución global óptima**.

En lugar de analizar todas las combinaciones posibles, el algotimo voraz **elige siempre la opción más prometedora en el momento actual**, sin volver atrás.

Este principio se aplica ampliamente en problemas de optimización, búsqueda y selección.

---

## 🎒 Ejemplo del quiz: Problema de la Mochila Fraccional

Un aventurero tiene una mochila que soporta 50 kg. En su camino encuentra:

| Objeto | Peso (kg) | Valor (monedas) | Valor/Peso |
|:------:|:----------:|:----------------:|:-----------:|
| A | 10 | 60 | 6.0 |
| B | 20 | 100 | 5.0 |
| C | 30 | 120 | 4.0 |

**Objetivo:** maximizar el valor total sin exceder la capacidad de 50 kg.

**Estrategia voraz:** elegir primero los objetos con **mayor valor por unidad de peso**.

**Selección:**
- Tomar A completo (10 kg, valor 60)
- Tomar B completo (20 kg, valor 100)
- Tomar 2/3 de C (20 kg, valor 80)

✅ **Valor total máximo = 240 monedas de oro**

---

## ✅ Cuándo es apropiado usar un algoritmo voraz

Un algoritmo voraz es adecuado cuando:

1. **la solución óptima global puede construirse a partir de soluciones óptimas locales.**

2. **Cumple la propiedad de elección voraz**,  
   lo que significa que elegir la mejor opción local en cada paso **lleva a una solución global óptima**.

3. **El problema permite decisiones independientes**,  
   donde las decisiones tomadas no requieren corrección posterior.

4. **Se necesita eficiencia**,  
   ya que los algoritmos voraces suelen ser rápidos.

**Ejemplos comunes:**
- Problema de la mochila fraccional
- Árbol de expansión mínima (Kruskal, Prim)
- Codificación de Huffman
- Selección de actividades (interval scheduling)
- Dijkstra (en su versión con pesos positivos)

---

## ⚠️ Limitaciones del enfoque voraz

| Limitación | Descripción |
|:-----------|:-------------|
| ❌ **No garantiza solución óptima en todos los casos** | En problemas donde las decisiones afectan al futuro (como la mochila 0/1), puede quedarse en un óptimo local. |
| 🌀 **Sin retroceso (no backtracking)** | Una vez tomada una decisión, no hay vuelta atrás aunque luego se vea que fue incorrecta. |
| 💡 **Depende del criterio elegido** | Un criterio de selección mal definido puede producir resultados erróneos. |
| 🧮 **No aplicable a todos los problemas de optimización** | Algunos problemas requieren técnicas más completas como Programación Dinámica o Búsqueda Exhaustiva. |
---

## 🧾 Conclusiones

El **algoritmo voraz** es ideal cuando el problema cumple las propiedades de **subestructura óptima** y **elección voraz**,  
permitiendo obtener una solución eficiente sin necesidad de recorrer todo el espacio de búsqueda.

Sin embargo, su **simplicidad es también su limitación**, ya que **no considera consecuencias futuras** ni revisa decisiones pasadas.

Por eso, **antes de usarlo**, es fundamental analizar si el problema **cumple las condiciones que garantizan optimalidad**.

---
