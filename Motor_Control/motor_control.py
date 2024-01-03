from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Configuración de pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declaración de pines GPIO
motor_pin1 = 4
motor_pin2 = 24

# Configurando pines como salidas
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

# Enviando estado "LOW" al pin 2 del motor
GPIO.output(motor_pin2, GPIO.LOW)

# Configuración señal PWM a 100 Hz
pwm_motor = GPIO.PWM(motor_pin1, 100)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para manejar las solicitudes del deslizador
@app.route("/control_motor", methods=["POST"])
def control_motor():

    try:

        # Inicializando el ciclo de trabajo a 0
        pwm_motor.start(0)

        # Obteniendo el valor del deslizador
        value = int(request.form.get("value"))

        # Ajustando el ciclo de trabajo PWM
        duty_cycle = value
        pwm_motor.ChangeDutyCycle(duty_cycle)

        return "Ok"

    except Exception as e:
        return str(e)

# Ruta para manejar la terminación del programa
@app.route("/shutdown", methods=["POST"])
def shutdown():

    # Apagando los actuadores
    pwm_motor.ChangeDutyCycle(0)

    # Deteniendo la señal PWM
    pwm_motor.stop()

    # Limpiando los pines GPIO
    GPIO.cleanup()

    return "Shutting down..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)