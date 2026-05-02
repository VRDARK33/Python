def verificar_contraseña(contraseña):
    numeros = False
    mayusculas = False
    longitud = len(contraseña) >= 8
    minusculas = False


    for caracter in contraseña:
        if caracter.isupper():
            mayusculas = True
        if caracter.isdigit():
            numeros = True
        if caracter.islower():
            minusculas = True

    es_valida = numeros and mayusculas and longitud and minusculas

    if not numeros:
        print(f"No contiene numeros")
    if not mayusculas:
        print(f"No contiene mayusculas")
    if not minusculas:
        print(f"No contiene minusculas")
    if not longitud:
        print(f"contraseña muy corta (MINIMO 8 caracteres)")
    
    if es_valida:
        print("contraseña valida")
    else:
        print(f"contraseña invalida")


contraseña = input("ingrese una contraseña: ")

verificar_contraseña(contraseña)

