# ==========================================
# SISTEMA DE BUSQUEDA POLICIAL Y SERENAZGO
# ==========================================

# ==========================================
# SISTEMA DE BUSQUEDA POLICIAL Y SERENAZGO
# ==========================================


# ==========================================
# BASE DE DATOS DE EFECTIVOS POLICIALES
# ==========================================

policias = [

    {
        "nombre": "ALIAGA VELASQUEZ JOHAN",
        "dni": "76454404",
        "cip": "NO REGISTRADO",
        "rango": "SO3"
    },

    {
        "nombre": "ALVARADO SALES DAVID CRISTOBAL",
        "dni": "74228301",
        "cip": "NO REGISTRADO",
        "rango": "SO2"
    },

    {
        "nombre": "ALVAREZ LOPEZ BRYAN OSCAR",
        "dni": "48205314",
        "cip": "32140332",
        "rango": "SO3"
    },

    {
        "nombre": "ANCHAY HUAMAN ELMER SHAUL",
        "dni": "77048486",
        "cip": "42142301",
        "rango": "SO2"
    },

    {
        "nombre": "ARANIBAR POMA DAVID ANTONY",
        "dni": "71454831",
        "cip": "NO REGISTRADO",
        "rango": "SO2"
    },

    {
        "nombre": "ASENJO CLAVO ANTHONY NELSON",
        "dni": "48593865",
        "cip": "32168708",
        "rango": "SO2"
    },

    {
        "nombre": "BELLO CRUZ RONALD EDGAR",
        "dni": "79429029",
        "cip": "NO REGISTRADO",
        "rango": "SO2"
    },

    {
        "nombre": "CHAPARRO GALVEZ RICARDO JORGE",
        "dni": "71792586",
        "cip": "32491890",
        "rango": "SO3"
    },

    {
        "nombre": "DAVILA NEIRA LUIS FERNANDO",
        "dni": "75195166",
        "cip": "32169097",
        "rango": "SO2"
    },

    {
        "nombre": "FLORES GONZALES JESUS",
        "dni": "74983477",
        "cip": "32492035",
        "rango": "SO3"
    }

]


# ==========================================
# BASE DE DATOS DE SERENAZGO
# ==========================================

serenos = [

    {
        "nombre": "ZAPATA SILVA CARMEN NAYDU",
        "dni": "46689019"
    },

    {
        "nombre": "ZAPATA SILVA CECILIA",
        "dni": "40458530"
    },

    {
        "nombre": "ALVAREZ MATSUSAKA NICANOR",
        "dni": "15751086"
    },

    {
        "nombre": "BUITRON LAZO JUAN EDICSON",
        "dni": "48269608"
    },

    {
        "nombre": "CORDOVA ESPINOZA JORGE STEVE",
        "dni": "74920777"
    },

    {
        "nombre": "DEL AGUILA FLORES FREDY ROLANDO",
        "dni": "70166037"
    },

    {
        "nombre": "GALVAN GOMEZ ANDY",
        "dni": "71885137"
    },

    {
        "nombre": "GUZMAN ASCASIBAR SERGIO ANTONIO",
        "dni": "47123406"
    },

    {
        "nombre": "JORGE MELGAREJO LUIS ALBERTO",
        "dni": "41372517"
    },

    {
        "nombre": "POMAR ACOSTA JOSE ANDRES",
        "dni": "75239849"
    }

]

# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n======================================")
    print(" SISTEMA DE BUSQUEDA POLICIAL")
    print("======================================")

    print("1. Buscar Efectivo Policial")
    print("2. Buscar Agente de Serenazgo")
    print("3. Registrar Efectivo Policial")
    print("4. Registrar Agente de Serenazgo")
    print("5. Mostrar Efectivos Policiales")
    print("6. Mostrar Agentes de Serenazgo")
    print("7. Salir")
    print("8. Editar Efectivo Policial")
    print("9. Editar Agente de Serenazgo")

    opcion = input("\nSeleccione una opcion: ")

# ==========================================
    # BUSCAR POLICIA
    # ==========================================

    if opcion == "1":

        buscar = input("\nIngrese nombre o apellido: ").lower()
        encontrado = False

        for policia in policias:
            if buscar in policia["nombre"].lower():

                print("\n========== EFECTIVO ENCONTRADO ==========")
                print("Nombre :", policia["nombre"])
                print("DNI    :", policia["dni"])
                print("CIP    :", policia["cip"])
                print("Rango  :", policia["rango"])

                encontrado = True

        if not encontrado:
            print("\nNo se encontraron resultados.")


    # ==========================================
    # BUSCAR SERENO
    # ==========================================

    elif opcion == "2":

        buscar = input("\nIngrese nombre o apellido: ").lower()
        encontrado = False

        for sereno in serenos:
            if buscar in sereno["nombre"].lower():

                print("\n========== AGENTE ENCONTRADO ==========")
                print("Nombre :", sereno["nombre"])
                print("DNI    :", sereno["dni"])

                encontrado = True

        if not encontrado:
            print("\nNo se encontraron resultados.")

# ==========================================
    # REGISTRAR POLICIA
    # ==========================================

    elif opcion == "3":

        print("\n===== REGISTRAR EFECTIVO =====")

        nombre = input("Ingrese nombre completo: ")

        while True:
            dni = input("Ingrese DNI (8 digitos): ")
            if len(dni) == 8 and dni.isdigit():
                break
            print("DNI invalido.")

        cip = input("Ingrese CIP: ")
        rango = input("Ingrese rango: ")

        policias.append({
            "nombre": nombre,
            "dni": dni,
            "cip": cip,
            "rango": rango
        })

        print("\nEfectivo registrado correctamente.")


    # ==========================================
    # REGISTRAR SERENO
    # ==========================================

    elif opcion == "4":

        print("\n===== REGISTRAR AGENTE =====")

        nombre = input("Ingrese nombre completo: ")

        while True:
            dni = input("Ingrese DNI (8 digitos): ")
            if len(dni) == 8 and dni.isdigit():
                break
            print("DNI invalido.")

        serenos.append({
            "nombre": nombre,
            "dni": dni
        })

        print("\nAgente registrado correctamente.")

 # ==========================================
    # MOSTRAR POLICIAS
    # ==========================================

    elif opcion == "5":

        print("\n===== LISTA DE EFECTIVOS =====")

        for policia in policias:
            print("\nNombre :", policia["nombre"])
            print("DNI    :", policia["dni"])
            print("CIP    :", policia["cip"])
            print("Rango  :", policia["rango"])


    # ==========================================
    # MOSTRAR SERENOS
    # ==========================================

    elif opcion == "6":

        print("\n===== LISTA DE AGENTES =====")

        for sereno in serenos:
            print("\nNombre :", sereno["nombre"])
            print("DNI    :", sereno["dni"])


    # ==========================================
    # SALIR
    # ==========================================

    elif opcion == "7":

        print("\nSaliendo del sistema...")
        break

