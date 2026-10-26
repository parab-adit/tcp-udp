import matplotlib.pyplot as plt

bands = ['VLF', 'LF', 'MF', 'HF', 'VHF', 'UHF', 'SHF', 'EHF']
freq = ['3–30 kHz', '30–300 kHz', '300 kHz–3 MHz', '3–30 MHz',
        '30–300 MHz', '300 MHz–3 GHz', '3–30 GHz', '30–300 GHz']
uses = ['Submarine', 'Navigation', 'AM Radio', 'Shortwave',
        'FM, TV', 'Mobile, Wi-Fi', '5G, Satellite', 'Radar, mmWave']
plt.figure(figsize=(12, 4))
for i in range(len(bands)):
    plt.axvspan(i, i + 1, color=plt.cm.rainbow(i / len(bands)))
    plt.text(i + 0.5, 0.5, bands[i], ha='center', fontsize=11)
    plt.text(i + 0.5, -0.4, freq[i] + '\n' + uses[i],
             ha='center', fontsize=8)
plt.xlim(0, 8)
plt.ylim(-1, 1)
plt.xticks([])
plt.yticks([])
plt.title('Wireless Frequency Spectrum')
plt.xlabel('Frequency Bands (Equal-Width Representation)')
plt.tight_layout()
plt.show()