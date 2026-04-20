import numpy as np
import matplotlib.pyplot as plt

frequency = 200
amplitude = 1
phase = 0
duration = 1
phase_rad = phase * 2 * np.pi / 360
p_ref = 2e-5

sample_rates = [44100, 5000, 1000, 500, 410, 401, 400, 399,
                350, 310, 290, 250, 210, 200, 190, 150, 110, 100, 90, 50]

measured_freqs = []

for sr in sample_rates:
    t = np.arange(0, duration, 1/sr)
    signal = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)
    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/sr)
    magnitudes = np.abs(spectrum)
    peak_idx = np.argmax(magnitudes)
    measured_freqs.append(freqs[peak_idx])

x = list(range(len(sample_rates)))
labels = [str(sr) for sr in sample_rates]

# Nyquist is at sr=400, index 6
nyquist_idx = sample_rates.index(400)

# Aliased region: sr < 400, i.e. index 7 (sr=399) onwards
aliased_start = sample_rates.index(399)

plt.figure(figsize=(14, 5))

# Shade aliased region
plt.axvspan(aliased_start - 0.5, len(sample_rates) - 0.5,
            color='red', alpha=0.1, label='Aliased region (sr < 400 Hz)')

# Plot line
plt.plot(x, measured_freqs, marker='o', color='black', linewidth=1)

# Arrow pointing to Nyquist frequency (sr=400)
nyquist_y = measured_freqs[nyquist_idx]
plt.annotate(
    'Nyquist frequency\n(sr = 400 Hz)',
    xy=(nyquist_idx, nyquist_y),
    xytext=(nyquist_idx - 2, nyquist_y + 60),
    arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
    color='blue',
    fontsize=9,
    ha='center'
)

plt.xticks(x, labels, fontsize=8)
plt.yticks([0, 50, 100, 150, 200])
plt.xlabel("sample rate", loc='right')
plt.ylabel("measured\nfrequency", loc='top', rotation=0, labelpad=-30)
plt.ylim(0, 220)
plt.xlim(-0.5, len(sample_rates) - 0.5)
plt.legend(loc='upper right', fontsize=9)
plt.grid(False)
plt.tight_layout()
plt.savefig('measured_frequency_vs_sample_rate.png', dpi=150)
plt.show()