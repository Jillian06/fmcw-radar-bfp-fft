# ADC-Aware Adaptive BFP FFT for FMCW Radar

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SystemVerilog](https://img.shields.io/badge/SystemVerilog-RTL-6B4FBB)](#)
[![Tests](https://github.com/Jillian06/fmcw-radar-bfp-fft/actions/workflows/test.yml/badge.svg)](https://github.com/Jillian06/fmcw-radar-bfp-fft/actions/workflows/test.yml)

A research portfolio repository for an **ADC-aware, stage-wise adaptive block-floating-point (BFP) FFT** architecture for FMCW radar range processing.

> **Provenance:** the paper and measured results are the research record. This public repository contains a clean reference model, documentation, and reproducible checks derived from the documented design. It is not presented as a verbatim copy of the original internal research source tree.

## Research question

How can a fixed-point FFT preserve spectral fidelity and avoid overflow without paying the cost of uniformly wide internal precision?

The project studies this at the **ADC-to-FFT boundary** by combining:

- finite-resolution ADC modeling
- a 1024-point radix-2 FFT
- stage-wise magnitude monitoring
- shared-exponent BFP scaling
- bit-accurate Python ↔ RTL verification
- FPGA synthesis and numerical-quality evaluation

## Signal chain

```text
FMCW beat signal
      |
      v
finite-resolution ADC
      |  1000 samples @ 10 MHz
      v
zero pad to 1024
      |
      v
radix-2 fixed-point FFT
      |
      +--> stage magnitude monitor
      |          |
      |          v
      |    adaptive shift / shared exponent
      v
range spectrum -> peak bin -> range estimate
```

## Key measured results

| Metric | Reported result |
|---|---:|
| FFT length | 1024 points |
| Sampling rate | 10 MHz |
| Chirp duration | 100 µs |
| Physical ADC samples / chirp | 1000 |
| RTL/reference regressions | 120 multi-length cases |
| Bit-exact agreement | Yes |
| Adaptive BFP SQNR @ 35 dB input SNR | 60.17 dB |
| Fixed per-stage scaling SQNR @ 35 dB | 35.86 dB |
| SQNR improvement | **+24.31 dB** |
| Cyclone V Fmax | 51.73 MHz |
| Adaptive BFP ALMs | 456 |
| Registers | 209 |
| DSP blocks | 2 |
| Block memory | 49,152 bits |
| High-SNR 30 m grid-offset floor | ~2.93 cm |

## Repository structure

```text
.
├── src/
│   ├── bfp.py              # BFP scaling helpers
│   └── fmcw.py             # FMCW range / bin utilities
├── tests/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── RESULTS.md
│   └── VERIFICATION.md
└── .github/workflows/
```

## Quick start

```bash
python -m pip install pytest numpy
PYTHONPATH=src pytest -q
```

## Design idea

For a radix-2 butterfly, worst-case magnitude can grow by approximately a factor of two in one stage. The design therefore uses a **pre-stage guard threshold of one-half full scale** as a deterministic overflow-safe condition: if a monitored block approaches that threshold, the block is shifted before the next stage and the shared exponent is incremented.

## Why BFP?

Fixed per-stage scaling is safe but can introduce unnecessary quantization loss. Adaptive BFP only shifts when the observed dynamic range requires it, preserving more useful signal amplitude while still managing overflow risk.

## Verification philosophy

The original research used a bit-accurate Python reference model and SystemVerilog RTL regression flow. This public version keeps the numerical contract explicit and testable, while avoiding claims that unmeasured behavior or unavailable internal source files are reproduced exactly.

See [Verification](docs/VERIFICATION.md) and [Results](docs/RESULTS.md).

## Scope

**Documented research:** adaptive BFP policy, Python–RTL bit-exact verification, FMCW end-to-end evaluation, Cyclone V synthesis, SQNR/resource trade-offs.

**Public reference code here:** numerical helpers and reproducible sanity checks for BFP scaling and FMCW range-grid calculations.

## License

MIT for code in this repository. Research manuscripts and publication content remain under their respective copyright terms.
