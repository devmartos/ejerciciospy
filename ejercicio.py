print("A continuación completaremos su perfil, rellene los siguientes datos: ")

while True:
    name = input("Nombre: ").title()
    age = int(input("Edad: "))
    site = input("Localidad: ").upper()
    state = input("Provincia: ").upper()
    salary = input("Salario: ")
    dni = input("DNI: ")

    cadena = name, age, site, state, salary, dni
    print("Estos son sus datos")
    print(cadena)
    validate = input("Son correctos? -- y/n: ")

    if validate == "y":
        f = open("empleados.csv", "a")
        f.write(f"{cadena}\n")
        break