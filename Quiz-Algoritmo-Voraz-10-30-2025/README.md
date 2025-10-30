# 🧠 Algoritmos Voraces (Greedy Algorithms)

## 📘 Descripción General

Un **algoritmo voraz (greedy)** es una técnica de optimización que **toma decisiones locales óptimas en cada paso**, esperando que esas decisiones lleven a una **solución global óptima**.

En lugar de analizar todas las combinaciones posibles (como haría un algoritmo de fuerza bruta o programación dinámica), el método voraz **elige siempre la opción más prometedora en el momento actual**, sin volver atrás.

---

## ⚙️ Principio del Algoritmo Voraz

> “En cada paso, elige la opción que parece la mejor en ese instante,  
> sin preocuparte por el efecto futuro de esa decisión.”

Este principio se aplica ampliamente en problemas de optimización, búsqueda y selección.

---

## 🎒 Ejemplo: Problema de la Mochila Fraccional

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

1. **El problema tiene propiedad de subestructura óptima**,  
   es decir, la solución óptima global puede construirse a partir de soluciones óptimas locales.

2. **Cumple la propiedad de elección voraz**,  
   lo que significa que elegir la mejor opción local en cada paso **lleva a una solución global óptima**.

3. **El problema permite decisiones independientes**,  
   donde las decisiones tomadas no requieren corrección posterior.

4. **Se necesita eficiencia**,  
   ya que los algoritmos voraces suelen ser rápidos (tiempo lineal o logarítmico).

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

## 🧩 Diferencia entre mochila fraccional y 0/1

| Tipo de Mochila | ¿Se pueden tomar fracciones? | ¿Voraz es óptimo? |
|:-----------------|:-----------------------------:|:------------------:|
| Fraccional | ✅ Sí | ✅ Sí |
| 0/1 (entera) | ❌ No | ❌ No siempre |

**Ejemplo:**  
Si solo puedes tomar objetos completos (0 o 1), el algoritmo voraz puede no encontrar la mejor combinación.

---

## 🧮 Complejidad

- **Tiempo:** `O(n log n)` (por la ordenación inicial de objetos)  
- **Espacio:** `O(n)` (para almacenar la lista de objetos)

---

## 🧾 Conclusión

El **algoritmo voraz** es ideal cuando el problema cumple las propiedades de **subestructura óptima** y **elección voraz**,  
permitiendo obtener una solución eficiente sin necesidad de recorrer todo el espacio de búsqueda.

Sin embargo, su **simplicidad es también su limitación**, ya que **no considera consecuencias futuras** ni revisa decisiones pasadas.

Por eso, **antes de usarlo**, es fundamental analizar si el problema **cumple las condiciones que garantizan optimalidad**.

---

## 👩‍💻 Ejemplo de implementación (Python)

```python
def mochila_fraccional(objetos, capacidad):
    objetos_ordenados = sorted(objetos, key=lambda x: x[2] / x[1], reverse=True)
    valor_total = 0
    peso_total = 0
    seleccion = []

    for nombre, peso, valor in objetos_ordenados:
        if peso_total + peso <= capacidad:
            seleccion.append((nombre, 1.0))
            valor_total += valor
            peso_total += peso
        else:
            fraccion = (capacidad - peso_total) / peso
            seleccion.append((nombre, round(fraccion, 2)))
            valor_total += valor * fraccion
            break

    return valor_total, seleccion
