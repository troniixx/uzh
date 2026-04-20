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

print(f"{'freq':>6} {'amp':>4} {'phase':>6} {'sr':>8} {'meas. freq (Hz)':>16} {'intensity (dB SPL)':>18}")
print("-" * 68)

measured_freqs = []

for sr in sample_rates:
    t = np.arange(0, duration, 1/sr)
    signal = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/sr)

    magnitudes = np.abs(spectrum)
    peak_idx = np.argmax(magnitudes)
    measured_freq = freqs[peak_idx]
    measured_freqs.append(measured_freq)
    peak_amplitude = magnitudes[peak_idx] / len(t) * 2

    if peak_amplitude > 0:
        rms = peak_amplitude / np.sqrt(2)
        intensity_db = 20 * np.log10(rms / p_ref)
        db_str = f"{intensity_db:.2f}"
    else:
        db_str = "-inf"

    print(f"{frequency:>6} {amplitude:>4} {phase:>6} {sr:>8} {measured_freq:>16.1f} {db_str:>18}")

# Plot with categorical x-axis
x = list(range(len(sample_rates)))
labels = [str(sr) for sr in sample_rates]

plt.figure(figsize=(14, 5))
plt.plot(x, measured_freqs, marker='o', color='black', linewidth=1)
plt.xticks(x, labels, fontsize=8)
plt.yticks([0, 50, 100, 150, 200])
plt.xlabel("sample rate", loc='right')
plt.ylabel("measured\nfrequency", loc='top', rotation=0, labelpad=-30)
plt.ylim(0, 220)
plt.xlim(-0.5, len(sample_rates) - 0.5)
plt.grid(False)
plt.tight_layout()
plt.savefig('measured_frequency_vs_sample_rate.png', dpi=150)
plt.show()