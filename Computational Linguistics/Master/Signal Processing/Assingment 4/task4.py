import numpy as np

frequency = 200
phase = 0
duration = 1
sr = 22050
phase_rad = phase * 2 * np.pi / 360
p_ref = 2e-5

bits_list = [1, 2, 4, 8, 12, 16]
amplitudes = [1e-3, 0.5e-3]  # 1 mV and 1/2 mV

def quantise(signal, bits):
    """Replicates Praat's quantisation formula exactly."""
    q = 2 ** bits
    c = (2 / q) / 2
    quantised = (np.floor(signal * (q / 2)) / (q / 2)) + c
    return quantised

def analyse(signal, sr, frequency):
    """Returns quantisation levels visible, fundamental dB SPL, and harmonic distortion in dB."""
    N = len(signal)
    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(N, d=1/sr)
    magnitudes = np.abs(spectrum) / N * 2

    # Fundamental
    fund_idx = np.argmin(np.abs(freqs - frequency))
    fund_amp = magnitudes[fund_idx]
    fund_db = 20 * np.log10(fund_amp / np.sqrt(2) / p_ref) if fund_amp > 0 else -np.inf

    # Find harmonics (multiples of fundamental, skip fundamental itself)
    harmonic_amps = []
    harmonic_num = 2
    while harmonic_num * frequency <= sr / 2:
        h_idx = np.argmin(np.abs(freqs - harmonic_num * frequency))
        harmonic_amps.append(magnitudes[h_idx])
        harmonic_num += 1

    if harmonic_amps and max(harmonic_amps) > 0:
        max_harmonic_amp = max(harmonic_amps)
        # Harmonic distortion = difference between fundamental and strongest harmonic
        distortion_db = 20 * np.log10(fund_amp) - 20 * np.log10(max_harmonic_amp)
    else:
        distortion_db = np.inf  # no distortion detectable

    return distortion_db

print(f"{'bits':>6} | {'q levels':>10} | {'HD 1mV (dB)':>12} | {'q levels':>10} | {'HD 0.5mV (dB)':>14}")
print("-" * 62)

for bits in bits_list:
    q_levels = 2 ** bits
    row = f"{bits:>6} | {q_levels:>10} |"

    for amp in amplitudes:
        t = np.arange(0, duration, 1/sr)
        signal = amp * np.sin(2 * np.pi * frequency * t + phase_rad)
        q_signal = quantise(signal, bits)
        hd = analyse(q_signal, sr, frequency)
        hd_str = f"{hd:.2f}" if np.isfinite(hd) else "inf"
        row += f" {hd_str:>12} |"

    print(row)