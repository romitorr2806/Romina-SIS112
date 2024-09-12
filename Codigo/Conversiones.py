import Codigo.Funciones as Funciones
while True:
    opcion = Funciones.opciones()
    if opcion == 1:
         N = int(input("""Si quieres de metros a km apreta 1
        Si quieres de km a metros apreta 2
        :"""))
    if N == 1:
        m = int(input("Ingresa cuantos metros convertir: "))
        print("Tienes {} km".format(Funciones.m_km(m))) 
    elif N == 2:
        km = int(input("Ingresa cuantos km convertir: "))
        print("Tines {} metros".format(Funciones.km_m(km)))
    elif opcion == 2:
        N = int(input("""Si quieres de g a kg apreta 1
        Si quieres de kg a g apreta 2 
        :"""))
        if N ==  1:
            g = int(input("Ingrese cuantos g convertir: "))
            print("Tienes {} kg".format(Funciones.g_kg(g)))
        elif N== 2:
            kg = int(input("Ingrese cuantos kg convertir: "))
            print("Tienes {} g".format(Funciones.kg_g(kg)))
    elif opcion == 3:
        N = int(input("""Si quieres de centigrado a farenheit
        Si quieres de farenheit a centrigrado
        :"""))
        if N == 1:
            C = int(input("Ingrese cuantos centigrados convertir: "))
            print("Tienes {} k°".format(Funciones.C_F(C)))
        elif F == 2:
            F = int(input("Ingrese cuantos ferenheit convertir: "))
            print("Tienes {} C°".format(Funciones.F_C(F)))
    elif opcion == 4:
        break 
    