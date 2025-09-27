import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# configuracion estetica de las graficas
plt.style.use('seaborn-v0_8')
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Tipos de Señales', fontsize=16, fontweight='bold')

# parametros comunes
t_continuo = np.linspace(0, 2, 1000)  # Tiempo continuo
t_discreto = np.linspace(0, 2, 20)      # Tiempo discreto 
f = 2  # Frecuencia de 2 Hz

# Grafica 1 Señal Periódica Continua 
senal_periodica_continua = np.sin(2 * np.pi * f * t_continuo)
axs[0, 0].plot(t_continuo, senal_periodica_continua, 'b-', linewidth=2)
axs[0, 0].set_title('Señal Periódica Continua\n(Onda Senoidal)')
axs[0, 0].set_xlabel('Tiempo')
axs[0, 0].set_ylabel('Amplitud')
axs[0, 0].grid(True, alpha=0.3)

# Grafica 2 Señal Periódica Discreta 
senal_periodica_discreta = np.sin(2 * np.pi * f * t_discreto)
axs[0, 1].stem(t_discreto, senal_periodica_discreta, 'r-', basefmt=" ")
axs[0, 1].plot(t_discreto, senal_periodica_discreta, 'r--', alpha=0.5)
axs[0, 1].set_title('Señal Periódica Discreta\n(Sinusoidal Muestreada)')
axs[0, 1].set_xlabel('Tiempo')
axs[0, 1].set_ylabel('Amplitud')
axs[0, 1].grid(True, alpha=0.3)

# Grafica 3 Señal Aperiódica Continua
senal_aperiodica_continua = np.exp(-3 * t_continuo) * np.sin(10 * np.pi * t_continuo)
axs[1, 0].plot(t_continuo, senal_aperiodica_continua, 'g-', linewidth=2)
axs[1, 0].set_title('Señal Aperiódica Continua\n(Exponencial Decreciente)')
axs[1, 0].set_xlabel('Tiempo')
axs[1, 0].set_ylabel('Amplitud')
axs[1, 0].grid(True, alpha=0.3)

# Grafica 4 Señal Aperiódica Discreta
n = np.arange(0, 20)  # Índices discretos
senal_aperiodica_discreta = signal.unit_impulse(20, 7)  # Pulso en n=5
axs[1, 1].stem(n, senal_aperiodica_discreta, 'm-', basefmt=" ")
axs[1, 1].set_title('Señal Aperiódica Discreta\n(Pulso Unitario)')
axs[1, 1].set_xlabel('Muestras')
axs[1, 1].set_ylabel('Amplitud')
axs[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


