#Mochila Fraccional - Algotirmo Voraz - Quiz 10-30-25

items = [
    {"name":"A", "peso":10, "valor":60},
    {"name":"B", "peso":20, "valor":100},
    {"name":"C", "peso":30, "valor":120},
]
capacidad = 50

# Añadimos la razón y ordenamos por ella (mayor a menor)
for it in items:
    it["ratio"] = it["valor"] / it["peso"]
items_sorted = sorted(items, key=lambda x: x["ratio"], reverse=True)

seleccion = []
valor_total = 0.0
peso_restante = capacidad

for it in items_sorted:
    if peso_restante <= 0:
        break
    if it["peso"] <= peso_restante:
        # tomar entero
        seleccion.append((it["name"], 1.0))  # 1.0 = fracción completa
        valor_total += it["valor"]
        peso_restante -= it["peso"]
    else:
        # tomar fracción
        fraccion = peso_restante / it["peso"]
        seleccion.append((it["name"], fraccion))
        valor_total += it["valor"] * fraccion
        peso_restante = 0

print("Selección (objeto, fracción tomada):", seleccion)
print("Valor total:", valor_total)
