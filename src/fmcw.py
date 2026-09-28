"""Small FMCW range-grid utilities."""

C = 299_792_458.0

def chirp_slope(bandwidth_hz: float, chirp_s: float) -> float:
    return bandwidth_hz / chirp_s

def beat_frequency(range_m: float, bandwidth_hz: float, chirp_s: float) -> float:
    return chirp_slope(bandwidth_hz, chirp_s) * (2.0 * range_m / C)

def range_from_beat(beat_hz: float, bandwidth_hz: float, chirp_s: float) -> float:
    return C * beat_hz / (2.0 * chirp_slope(bandwidth_hz, chirp_s))

def fft_bin_spacing(fs_hz: float, n_fft: int) -> float:
    return fs_hz / n_fft

def range_per_bin(fs_hz: float, n_fft: int, bandwidth_hz: float, chirp_s: float) -> float:
    return range_from_beat(fft_bin_spacing(fs_hz, n_fft), bandwidth_hz, chirp_s)
