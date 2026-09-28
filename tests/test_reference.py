from bfp import adaptive_pre_stage_scale, half_scale_guard, needs_shift
from fmcw import fft_bin_spacing, range_from_beat

def test_half_scale_guard():
    assert half_scale_guard(511) == 255

def test_shift_triggers_at_guard():
    assert needs_shift([254, -254], 511) is False
    assert needs_shift([255], 511) is True

def test_adaptive_scaling_updates_exponent():
    scaled, exp, shifted = adaptive_pre_stage_scale([300, -100], 511, exponent=2)
    assert shifted is True
    assert exp == 3
    assert scaled == [150, -50]

def test_fft_bin_spacing_for_documented_setup():
    assert fft_bin_spacing(10_000_000.0, 1024) == 9765.625

def test_range_mapping_is_positive():
    assert range_from_beat(2.0e6, 1.0e8, 1.0e-4) > 0
