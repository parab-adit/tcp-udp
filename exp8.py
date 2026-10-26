import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N = 200000
bits = np.random.randint(0, 2, N)
s = 2 * bits - 1
def ber(snr_db, sir_db=None):
    noise = np.random.randn(N) / np.sqrt(2 * 10**(snr_db / 10))
    r = s + noise
    if sir_db is not None:
        r += 10**(-sir_db / 20) * np.sign(np.random.randn(N))
    return np.mean((r > 0) != bits)
snr = np.arange(0, 11)
plt.figure(figsize=(7, 4.5))
plt.semilogy(snr, [ber(x) + 1e-6 for x in snr], 'o-', label='AWGN only')
plt.semilogy(snr, [ber(x, 6) + 1e-6 for x in snr], 's-', label='SIR = 6 dB')
plt.semilogy(snr, [ber(x, 3) + 1e-6 for x in snr], '^-', label='SIR = 3 dB')

plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('Effect of Noise and Interference on BER')
plt.grid(True, which='both', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()