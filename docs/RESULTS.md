# Results

## Numerical fidelity

The research reports **bit-exact agreement across 120 multi-length RTL/reference regression cases**.

At 35 dB input SNR:

| Scaling policy | Mean FFT SQNR |
|---|---:|
| Adaptive BFP | 60.17 dB |
| Fixed per-stage scaling | 35.86 dB |

Difference: **+24.31 dB** in favor of adaptive BFP.

## FPGA synthesis

Target: **Intel Cyclone V 5CGXFC9A6U19A7**

| Metric | Fixed scaling | Adaptive BFP |
|---|---:|---:|
| ALMs | 382 | 456 |
| Registers | 189 | 209 |
| Fmax | 50.69 MHz | 51.73 MHz |
| Block memory | 49,152 bits | 49,152 bits |
| DSP blocks | 2 | 2 |
| Estimated core dynamic power | 9.55 mW | 9.14 mW |

The adaptive design therefore trades a measured **+19.4% ALM overhead** for substantially improved high-SNR SQNR, while keeping identical memory and DSP footprints in the reported synthesis.

## Range behavior

For a 30 m target, the high-SNR peak-bin estimate shows a deterministic error floor of approximately **2.93 cm**, attributed to the nearest-bin offset of the zero-padded FFT grid rather than BFP scaling itself.
