from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.legacy import  show_message

# Configuración del dispositivo
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0)

try:

    while True:

        msg = 'ARGO'

        # Mostrar el mensaje en el dispositivo
        show_message(device, msg, fill="white", scroll_delay=0.1)

except KeyboardInterrupt:
    # Manejando la interrupción del teclado (Ctrl+C) para salir limpiamente
    pass

finally:
    # Limpiando los pines utilizados por el módulo
    device.cleanup()
