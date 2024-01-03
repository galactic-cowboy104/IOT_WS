import RPi.GPIO as GPIO
import time

# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declarando los pines GPIO
led1 = 22
led2 = 27

# Configurando los pines como salidas
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)  

# Configurando el PWM a 100 Hz de frecuencia
led_pwm1 = GPIO.PWM(led1, 100)
led_pwm2 = GPIO.PWM(led2, 100)

try:

    while True:

        # Inicializando la señal PWM a 0
        led_pwm1.start(0)
        led_pwm2.start(0)

        # Incrementando la señal PWM del LED 1
        for duty_cycle in range(0, 101, 1):
            led_pwm1.ChangeDutyCycle(duty_cycle)
            print(f"Valor del ciclo de trabajo (pin 1): {duty_cycle}")
            time.sleep(0.05)
        
        # Decrementando la señal PWM del LED 1
        for duty_cycle in range(100, -1, -1):
            led_pwm1.ChangeDutyCycle(duty_cycle)
            print(f"Valor del ciclo de trabajo (pin 1): {duty_cycle}")
            time.sleep(0.05)
        
        # Incrementando la señal PWM del LED 2
        for duty_cycle in range(0, 101, 1):
            led_pwm2.ChangeDutyCycle(duty_cycle)
            print(f"Valor del ciclo de trabajo (pin 2): {duty_cycle}")
            time.sleep(0.05)
        
        # Decrementando la señal PWM del LED 2
        for duty_cycle in range(100, -1, -1):
            led_pwm2.ChangeDutyCycle(duty_cycle)
            print(f"Valor del ciclo de trabajo (pin 2): {duty_cycle}")
            time.sleep(0.05)
    
except KeyboardInterrupt:
    pass

finally: 

    # Deteniendo las señales PWM
    led_pwm1.stop()
    led_pwm2.stop()

    # Limpiando los pines GPIO
    GPIO.cleanup()
