# Architecture

The documented system couples the physical FMCW sampling chain to fixed-point FFT hardware rather than optimizing the FFT in isolation.

```text
target range
   ↓
FMCW beat generation
   ↓
ADC quantization
   ↓
1000 samples / chirp
   ↓ zero padding
1024-point radix-2 FFT
   ↓
stage magnitude monitor
   ↓
adaptive shift decision
   ↓
shared exponent update
   ↓
range spectrum / peak estimate
```

At each stage, the block magnitude is monitored before butterfly growth. A half-full-scale guard is used because a radix-2 stage can approximately double worst-case magnitude. When the guard is crossed, the block is shifted right and the shared exponent is incremented.

Documented research blocks include radix-2 butterflies, memory banking, overflow / magnitude detection, stage-wise BFP control, pipelined datapaths, and shared-exponent tracking.

This public repository exposes the architecture and numerical contract without claiming that the original internal RTL hierarchy is available here.
