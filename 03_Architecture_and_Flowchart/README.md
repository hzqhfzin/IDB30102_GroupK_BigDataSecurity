# 03 - Architecture and System Flow

This directory contains the core methodological framework and operational diagrams for the **Privacy-Preserving Big Data Analytics (PPBDA)** framework, supporting **Research Objective 2 (RO2)**.

---

## 1. Design Science Research (DSR) Iteration Cycle
- **File:** `system_architecture.png`
- **Description:** Illustrates the 5-phase Design Science Research methodology (Peffers et al., 2007) and Iterative Prototyping model. It demonstrates the feedback loop between Phase 4 (Demonstration & Evaluation) and Phase 3 (Artifact Design & Prototyping) to balance privacy budgets ($\epsilon$) against predictive utility.

---

## 2. System Operational Flowchart
- **File:** `system_flowchart.png`
- **Description:** Details the sequential execution pipeline:
  1. Data Ingestion & Preprocessing
  2. Sensitivity Calculation ($L_2$-norm: $\|g\|_2$)
  3. Dynamic Gradient Clipping ($g \leftarrow g \cdot \frac{C}{\|g\|_2}$)
  4. Adaptive Laplace Differential Privacy Noise Injection
  5. Cryptographic Policy & Token Verification (CP-ABE / Kerberos)
  6. Distributed Secure Aggregation & Privacy Ledger Update
