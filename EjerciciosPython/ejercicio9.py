"""
1.
Crea una lista con 5 precios de productos
2.
Con un for, imprime cada precio
3.
Calcula e imprime el total sumando todos los precios
4.
Extra: imprime solo los precios mayores a $10.000
"""

precios = [25000, 5000, 15000, 50000, 12000]
total = 0
for p in precios:
    print(f"precios {p}")
    total += p

for p in precios:
    if p > 10000:
        print(f"precios mayores de $10.000 {p}")

print(f"Total sumado de los precios {total}")