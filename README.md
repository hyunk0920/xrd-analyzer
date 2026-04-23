# XRD Analyzer

A small Python tool for analyzing X-ray diffraction (XRD) patterns.
Given a CSV of 2θ vs intensity, it detects peaks, computes
d-spacings via Bragg's law, and produces an annotated plot.

## Motivation

Built as a way to practice the XRD analysis pipeline from MSE 201
in a reproducible, automated form. It's modest in scope — the
goal was to translate characterization coursework into a small,
working tool.

## Status

🚧 In progress — targeting v1.0.

- [x] CSV parsing
- [x] Peak detection
- [ ] d-spacing calculation
- [ ] Annotated plots
- [ ] CLI interface

## Installation
