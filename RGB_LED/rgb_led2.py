import RPi.GPIO as GPIO
import time

# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declarando los pines como variables
red_pin = 4
green_pin = 27
blue_pin = 22

# Configurando los pines como salidas
GPIO.setup(red_pin, GPIO.OUT)  
GPIO.setup(green_pin, GPIO.OUT) 
GPIO.setup(blue_pin, GPIO.OUT) 

# Configurando los objetos PWM a 1000 Hz de frecuencia
red_pwm = GPIO.PWM(red_pin, 1000)  
green_pwm = GPIO.PWM(green_pin, 1000) 
blue_pwm = GPIO.PWM(blue_pin, 1000) 

def changeColor(red_dc, green_dc, blue_dc):

    # Indicando que se están usando variables globales
    global red_pwm
    global green_pwm
    global blue_pwm

    # Cambiando los valores de las señales PWM
    red_pwm.ChangeDutyCycle(red_dc)
    green_pwm.ChangeDutyCycle(green_dc)
    blue_pwm.ChangeDutyCycle(blue_dc)

    # Imprimiendo los valores de las señales PWM
    print(f'R:{red_dc:03d}, G:{green_dc:03d}, B:{blue_dc:03d}', end='\r')

def mainTask():

    try:

        # Indicando que se están usando variables globales
        global red_pwm
        global green_pwm
        global blue_pwm

        # Inicializando las señales PWM con un ciclo de trabajo del 0%
        red_pwm.start(0)
        green_pwm.start(0)
        blue_pwm.start(0)

        # Bucle principal
        while True:

            # Inicializando las variables que almacenarán los valores PWM
            red_dc = 0
            green_dc = 0
            blue_dc = 0

            # Incrementa gradualmente el ciclo de trabajo de 0% a 100%
            for duty_cycle in range(0, 101, 1):
                red_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02)  # Espera 0.02 segundos para que sea perceptible
            
            # Incrementa gradualmente el ciclo de trabajo de 0% a 100%
            for duty_cycle in range(0, 101, 1):
                green_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02)  # Espera 0.02 segundos para que sea perceptible
            
            # Incrementa gradualmente el ciclo de trabajo de 0% a 100%
            for duty_cycle in range(0, 101, 1):
                blue_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02)  # Espera 0.02 segundos para que sea perceptible
            
            # Decrementa gradualmente el ciclo de trabajo de 100% a 0%
            for duty_cycle in range(100, -1, -1):
                red_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02) # Espera 0.02 segundos para que sea perceptible

            # Decrementa gradualmente el ciclo de trabajo de 100% a 0%
            for duty_cycle in range(100, -1, -1):
                green_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02) # Espera 0.02 segundos para que sea perceptible

            # Decrementa gradualmente el ciclo de trabajo de 100% a 0%
            for duty_cycle in range(100, -1, -1):
                blue_dc = duty_cycle
                changeColor(red_dc, green_dc, blue_dc)
                time.sleep(0.02) # Espera 0.02 segundos para que sea perceptible

    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para salir limpiamente
        pass

    finally:
        # Detiene las señales PWM y limpia la configuración de GPIO
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()

mainTask() # Mandando a llamar la función principal