import numpy as np

frequency = 200
amplitude = 1
duration = 1
sr = 400
p_ref = 2e-5

phases_deg = [0, 45, 90, 135, 180]

print(f"{'freq':>6} {'amp':>4} {'phase':>7} {'sr':>6} {'meas. freq (Hz)':>16} {'intensity (dB SPL)':>18}")
print("-" * 68)

for phase in phases_deg:
    phase_rad = phase * 2 * np.pi / 360
    t = np.arange(0, duration, 1/sr)
    signal = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/sr)

    magnitudes = np.abs(spectrum)
    peak_idx = np.argmax(magnitudes)
    measured_freq = freqs[peak_idx]
    peak_amplitude = magnitudes[peak_idx] / len(t) * 2

    if peak_amplitude > 0:
        rms = peak_amplitude / np.sqrt(2)
        intensity_db = 20 * np.log10(rms / p_ref)
        db_str = f"{intensity_db:.2f}"
    else:
        db_str = "-inf"

    print(f"{frequency:>6} {amplitude:>4} {phase:>6}° {sr:>6} {measured_freq:>16.1f} {db_str:>18}")