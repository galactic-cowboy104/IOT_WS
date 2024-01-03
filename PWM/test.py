import RPi.GPIO as GPIO

# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declarando los pines GPIO
pin = 4

# Configurando los pines como salidas
GPIO.setup(pin, GPIO.OUT)

# Configurando el PWM a 100 Hz de frecuencia
pwm = GPIO.PWM(pin, 100)

try:

    # Inicializando la señal PWM a 0
    pwm.start(0)
    
    # Ajustando la señal PWM a 60
    pwm.ChangeDutyCycle(60)

    while True:
        pass
    
except KeyboardInterrupt:
    pass

finally: 

    # Deteniendo las señales PWM
    pwm.stop()

    # Limpiando los pines GPIO
    GPIO.cleanup()
    