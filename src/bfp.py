"""Reference helpers for stage-wise block-floating-point scaling."""

def half_scale_guard(max_int: int) -> int:
    return max_int // 2

def needs_shift(samples, max_int: int) -> bool:
    guard = half_scale_guard(max_int)
    for value in samples:
        if isinstance(value, complex):
            if abs(value.real) >= guard or abs(value.imag) >= guard:
                return True
        elif abs(value) >= guard:
            return True
    return False

def arithmetic_shift_block(samples, bits: int = 1):
    if bits < 0:
        raise ValueError("bits must be non-negative")
    out = []
    for value in samples:
        if isinstance(value, complex):
            out.append(complex(int(value.real) >> bits, int(value.imag) >> bits))
        else:
            out.append(int(value) >> bits)
    return out

def adaptive_pre_stage_scale(samples, max_int: int, exponent: int = 0):
    if needs_shift(samples, max_int):
        return arithmetic_shift_block(samples, 1), exponent + 1, True
    return list(samples), exponent, False
