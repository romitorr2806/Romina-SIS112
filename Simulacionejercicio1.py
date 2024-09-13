import random
intentos = 0 
numero_secreto = random.randint(1,100)
print(numero_secreto)
print('''¡Bienvenido al juego Adivina el Número!
      Estoy pensando en un número entre el 1 al 100. ¿Podrías adivinar cuál es? ''')
while True: 
    num = int(input('Introduce un número: '))
    intentos += 1
    if numero_secreto < num:
        print('El número es demasiado alto, inténtalo de nuevo.')
    if numero_secreto > num:
        print('El número es demasiado bajo, inténtalo de nuevo.')
    if numero_secreto == num:
        print('Felicidades ganó el juego despues de {} intentos'.format(intentos))
        break





