import RPi.GPIO as GPIO
import time

# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declarando los pines GPIO
led_pin = 4
button_pin = 27

# Configurando el pin del LED como salidas
GPIO.setup(led_pin, GPIO.OUT)

# Configurando el pin del pulsador como entrada
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:

    # Enviando una estado alto al pin del LED
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.1)

    while True:
        
        # Detectando el estado del pulsador
        button_state = GPIO.input(button_pin)

        if button_state == GPIO.LOW:
            GPIO.output(led_pin, not GPIO.input(led_pin))
        else:
            GPIO.output(led_pin, GPIO.HIGH)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:

    # Limpiando los pines GPIO
    GPIO.cleanup()