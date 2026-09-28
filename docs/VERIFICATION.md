# Verification

## Original research flow

```text
physical FMCW beat model
        ↓
finite ADC quantization
        ↓
bit-accurate Python integer reference
        ↓
SystemVerilog RTL
        ↓
regression comparison
```

Reported checks include:
- 120 multi-length FFT regression cases with bit-exact agreement
- dedicated overflow-guard tests
- end-to-end SNR sweeps
- FFT SQNR comparison between scaling policies
- FPGA synthesis under matched constraints

## Public reference checks

The tests in this repository validate:
- half-full-scale guard calculation
- adaptive pre-stage shift behavior
- shared exponent update
- documented FFT-bin spacing for 10 MHz / 1024-point processing
- basic FMCW beat-to-range mapping

These checks are intentionally small and transparent. They are not labeled as a replacement for the full internal RTL verification environment.
