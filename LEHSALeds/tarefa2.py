#import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import time

#SETAR MODO E PINO DE SAÍDA
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setwarnings(False)

#ESTRUTURA DE REPETIÇÃO. ACENDER A CADA 250 MILISEGUNDOS, 10000 VEZES
#TRY -> TENTE [COMANDOS] EXCETO QUANDO [FUNÇÃO]
cont = 0
try:
    while cont < 10000:
        GPIO.output(16, True)
        time.sleep(0.25)

        cont = cont + 1

        GPIO.output(16, False)
        time.sleep(0.25)
except KeyboardInterrupt:
    print('Encerrando programa...')
    GPIO.cleanup()
#CLEANUP -> RESETAR OS PINOS QUE ESTÁ USANDO