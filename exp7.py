import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
f = 900e6
c = 3e8
lam = c / f
d = np.linspace(0, 5, 1000)
P = 20
amp = np.random.rand(P)
phase = 2 * np.pi * np.random.rand(P)
angle = 2 * np.pi * np.random.rand(P)
h = sum(amp[k] * np.exp(1j * (phase[k] +2 * np.pi * d / lam * np.cos(angle[k]))) for k in range(P))
rssi = 20 * np.log10(np.abs(h) / np.abs(h).mean())
plt.figure(figsize=(9, 4))
plt.plot(d, rssi)
plt.axhline(-10, color='red', linestyle='--', label='Deep fade (-10 dB)')
plt.xlabel('Distance moved (m)')
plt.ylabel('Signal level (dB)')
plt.title('Multipath Fading at 900 MHz')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
print("Maximum fade depth: %.1f dB" % rssi.min())
print("Signal below -10 dB: %.1f%%" % (100 * (rssi < -10).mean()))