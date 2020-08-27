import sys

sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import CosSignal

#modulo para mostrar graficas
import matplotlib.pyplot as plt

#Crear señal senoidal

seno = SinSignal(freq=200, amp=1.0, offset=0)

#Crear señal cosenoidal

coseno = CosSignal(freq=200, amp=1.0, offset=0)

#Crear grafica en memoria y asignamos propiedades
seno.plot()
coseno.plot()
decorate(xlabel='Tiempo(s)')
decorate(ylabel='Amplitud')

plt.show()