
def clasificar(numero):
    if numero % 2 == 0:
        return f"{numero} es par"
    else:
        return f"{numero} es impar"


for i in range(1,11):
    print(clasificar(i))