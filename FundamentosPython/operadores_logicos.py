edad = 20
time_id = True

# and: ambas condiciones deben ser True
if edad >=18 and time_id:
    print("Puede entrar.")

#or: basta con que uno de los dos sea True
es_estudiante = False
es_profesor = True
if es_estudiante or es_profesor:
    print("Tiene acceso al campus")

#not: invierte el valor
if not time_id:
    print("No tiene identificacion")
        