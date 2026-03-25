# CrossPoll — Efficient Project Guide
**Author**: Pankaj Kushwaha  
**Updated**: 25 March 2026  
**Status**: Ready to implement

---

## 1) Final Scope (Locked)

### Project in one line
Build **CrossPoll**: a multi-crop transfer-learning framework for **flower detection** in robotic pollination, optimized for fast adaptation to a new crop with few labels.

### What we are NOT doing
- No MAML / second-order meta-learning
- No hardware robot build
- No greenhouse deployment study
- No crop-only classification project

### Why this scope
This is the highest-probability path that is:
1. Technically feasible with your time (3–5 hrs/week)
2. Strong enough for publication
3. Directly aligned with robotic pollination requirements

---

## 2) Core Research Question

Can a detector jointly pretrained on flowers from multiple crops adapt to a new crop faster (with fewer labeled images) than standard baselines?

### Main hypothesis
CrossPoll reaches a target mAP on a new crop using significantly fewer labels than:
- training from scratch
- standard COCO-pretrained fine-tuning
- single-crop pretraining

---

## 3) Minimal Method (Most Efficient)

### Pipeline
1. Build unified flower datasets for 4 crops
2. Hold out one crop as “new crop”
3. Joint-train YOLOv8 on the other 3 crops
4. Fine-tune on held-out crop with N images, where N ∈ {25, 50, 100, 200, 500}
5. Compare against 3 baselines and plot sample-efficiency curves

### Why this is efficient
- Uses stable tooling (`ultralytics`)
- Avoids fragile meta-learning stacks
- Produces reviewer-friendly quantitative evidence quickly

---

## 4) Experimental Design (Fixed)

### Crop split template
- **Train crops**: Tomato + Strawberry + Apple
- **Held-out test crop**: Kiwi (or Pepper if dataset quality is better)

### Baselines (required)
1. **Scratch**: train on held-out crop only
2. **COCO Transfer**: `yolov8n.pt` → held-out crop
3. **Single-Crop Transfer**: pretrain on one source crop → held-out crop
4. **CrossPoll (ours)**: joint-pretrain on 3 crops → held-out crop

### Metrics
- Primary: mAP@50
- Secondary: Precision, Recall, F1
- Efficiency: training time, model size, inference latency

### Primary figures/tables
- Figure A: Sample-efficiency curve (mAP vs N labels)
- Table A: Method comparison at each N
- Table B: Efficiency metrics

---

## 5) Implementation Plan in This Repo

Use existing structure:

```
src/greenpoll/
  data/
  detect/
  eval/
  viz/
```

### New files to create
- `src/greenpoll/detect/train_joint.py` — joint pretraining script
- `src/greenpoll/detect/finetune.py` — fine-tune on held-out crop for each N
- `src/greenpoll/detect/baselines.py` — baseline runners
- `src/greenpoll/eval/metrics.py` — evaluation aggregation
- `src/greenpoll/viz/plots.py` — curve + comparison plots

### Config files
- `configs/datasets/*.yaml` (one per crop)
- `configs/experiments/crosspoll.yaml`

### Dependency additions
- `ultralytics`
- `torch`
- `torchvision`
- `matplotlib`
- `seaborn`

---

## 6) Week-by-Week Roadmap (Lean)

### Week 1
- Finalize datasets + held-out crop
- Convert all annotations to YOLO format
- Sanity-check train/val/test splits

### Week 2
- Implement and run baseline #1 and #2
- Save results in a single CSV schema

### Week 3
- Run baseline #3
- Implement joint training pipeline

### Week 4
- Run CrossPoll joint pretraining
- Start held-out fine-tuning for N={25, 50, 100}

### Week 5
- Complete N={200, 500}
- Generate plots/tables

### Week 6
- Draft Methods + Results sections
- Prepare reproducibility package (code/configs/README)

### Week 7
- Draft Introduction + Related Work + Discussion

### Week 8
- Final revisions
- arXiv upload
- COMPAG submission

---

## 7) Definition of Done

Project is complete when all are true:

- [ ] 4 methods executed (3 baselines + CrossPoll)
- [ ] Results for all N values captured in one results table
- [ ] Sample-efficiency curve produced
- [ ] Reproducible run command documented
- [ ] Paper draft complete (all major sections)
- [ ] Code publicly available
- [ ] arXiv + journal submission package ready

---

## 8) Risk Control (Practical)

| Risk | Mitigation |
|---|---|
| Dataset inconsistency | Standardize labels early; run format validator before training |
| Weak gains over baseline | Emphasize sample-efficiency and compute-efficiency; include confidence intervals |
| Time overrun | Freeze scope: no new models beyond YOLOv8n + defined baselines |
| Reviewer asks for stronger novelty | Frame contribution as first systematic cross-crop flower transfer benchmark for pollination context |

---

## 9) Publication Strategy

### Primary
Computers and Electronics in Agriculture (COMPAG)

### Submission framing
“Open, reproducible framework + benchmark for sample-efficient cross-crop flower detection for robotic pollination pipelines.”

### Preprint
Post arXiv (`cs.RO`, cross-list `cs.CV`) once main results are stable.

---

## 10) Immediate Next Actions (Start Here)

1. Install training stack and verify import of `ultralytics`.
2. Freeze held-out crop decision.
3. Build dataset manifests in `configs/datasets/`.
4. Run baseline #2 (COCO transfer) first to establish a strong reference.
5. Record every run in a single `results/summary.csv` file.

If you follow this guide exactly, you avoid unnecessary complexity and maximize probability of a publishable result in the shortest time.
