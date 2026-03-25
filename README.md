# GreenPoll

GreenPoll is an open-source research software project for greenhouse pollination robotics.

Version 1 focuses on a software-only pipeline:
- flower detection
- target prioritization
- path planning
- simulation and evaluation

## Status
Early scaffold.

## Planned modules
- `greenpoll.data`: dataset loading and validation
- `greenpoll.detect`: flower detection baselines
- `greenpoll.prioritize`: target ranking
- `greenpoll.plan`: route planning
- `greenpoll.sim`: greenhouse-row simulation
- `greenpoll.eval`: metrics
- `greenpoll.viz`: visual outputs
- `greenpoll.cli`: command-line tools

## Install
```bash
pip install -e .[dev]
```

## Run tests
```bash
pytest
```

## Research rules
- No fabricated results
- No fake citations
- No claims beyond implemented and validated functionality
