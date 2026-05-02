

numeros = [4, 17, 8, 33, 22, 5, 14, 91, 6, 50]

pares, impares, con_par, con_imp = [],[],0,0

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
        con_par += 1
    else:
        impares.append(i)
        con_imp += 1

print(pares)
print(impares)
print(f"Total de pares {con_par}")
print(f"Total de impares {con_imp}")