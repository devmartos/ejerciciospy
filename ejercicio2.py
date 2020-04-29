filename = "empleados.csv"
iteration = 0

with open(filename) as empleados_reverso:
    for person in empleados_reverso.readlines():

        name, age, site, state, salary, dni = person.split(",")


        cadena = dni, salary, state, site, age, name
        print(cadena)

        f = open("empleados_reverso.csv", "a")
        f.write(f"{cadena}\n")
        break

