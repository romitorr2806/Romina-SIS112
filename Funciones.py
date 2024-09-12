def opciones():
    op = int(input('''Elija la la conversión que quiera realizar: 
                   1. Conversión de longitud
                   2. Conversión de masa
                   3. Conversión de temperatura 
                   4. Apagar la conversión'''))
    op = int(input('Elija la opción:'))
    return op 
def m_km(m):
    distancia = m / 1000 
    return distancia
def km_m(km): 
    distancia = km * 1000
    return distancia
def kg_g(kg):
    masa = kg * 1000 
    return masa 
def g_kg(g):
    masa = g / 1000
    return masa 
def C_F(C):
    temperatura = (C*1.8)+32
    return temperatura
def F_C(F):
    temperatura = (F-32)/1.8
    return temperatura