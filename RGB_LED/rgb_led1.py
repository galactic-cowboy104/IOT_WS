import RPi.GPIO as GPIO
import time

# Configurando el modo de los pines (BCM o BOARD)
GPIO.setmode(GPIO.BCM)

# Defininiendo el número de los pines GPIO que se utilizarán
red = 4
green = 27
blue = 22

# Configurando los pines como salidas
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:

    while True:

        # Encendiendo color rojo por 2 segundos
        GPIO.output(red, GPIO.HIGH)
        print('  Color rojo encendido.')
        time.sleep(2)  
        
        # Apagando color rojo
        GPIO.output(red, GPIO.LOW)

        # Encendiendo color verde por 2 segundos
        GPIO.output(green, GPIO.HIGH)
        print('  Color verde encendido.')
        time.sleep(2) 

        # Apagando color verde
        GPIO.output(green, GPIO.LOW)

        # Encendiendo color azul por 2 segundos
        GPIO.output(blue, GPIO.HIGH)
        print('  Color azul encendido.')
        time.sleep(2) 

        # Apagando color azul
        GPIO.output(blue, GPIO.LOW)

# Manejando la interrupción del teclado (Ctrl+C)
except KeyboardInterrupt:
    pass

finally:
    # Limpiando y liberando los recursos GPIO
    print('\n  Fin del programa.')
    GPIO.cleanup()