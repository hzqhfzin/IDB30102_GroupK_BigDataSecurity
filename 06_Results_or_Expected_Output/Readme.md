# 📁 06_Results_or_Expected_Output

This directory contains the empirical evidence, performance telemetry, and visual benchmarks generated during the evaluation of the **Privacy-Preserving Big Data Security Framework**. 

The results demonstrate the system's ability to enforce data-at-rest encryption and fine-grained Role-Based Access Control (RBAC) across distributed nodes without causing severe computational bottlenecks[cite: 1].

## 📂 Directory Contents

### 1. Raw Execution Logs (`/execution_logs`)
Contains terminal output transcripts captured during the cluster testing phases.
* **`encryption_processing_run.log`** - Console output detailing the time taken to encrypt and distribute data blocks across the Hadoop worker nodes.
* **`rbac_security_audit.log`** - Logs demonstrating the system successfully blocking simulated unauthorized access and privilege escalation attempts[cite: 1].

### 2. Telemetry Data (`/telemetry_data`)
Contains the raw quantitative data collected by monitoring agents during the 10GB and 100GB workload injections.
* **`throughput_metrics.csv`** - Tracks the Read/Write speeds (in MB/s) of the encrypted framework versus a baseline native (unencrypted) HDFS setup.
* **`resource_utilization.json`** - Time-series data tracking CPU and memory consumption across the cluster during cryptographic operations.

### 3. Visualizations (`/visualizations`)
Contains graphical representations of the benchmark data for inclusion in the final report.
* **`throughput_comparison_chart.png`** - Bar chart comparing data retrieval throughput.
* **`latency_distribution.svg`** - Line graph mapping encryption latency (in milliseconds) against increasing file sizes.
* **`cpu_overhead_heatmap.png`** - Visualizes the resource footprint on the worker nodes during peak processing.

---

## 📊 Key Evaluation Metrics Summary

The data in this folder directly answers the core research objectives by evaluating the following metrics[cite: 1]:

| Metric | Target Benchmark | Actual Result (Expected) |
| :--- | :--- | :--- |
| **Encryption Latency** | Sub-second delay for standard blocks | *See `/telemetry_data/throughput_metrics.csv`* |
| **Read/Write Throughput** | Minimal degradation (<15% loss) | *See `/visualizations/throughput_comparison_chart.png`* |
| **RBAC Enforcement** | 100% block rate for unauthorized roles | **100%** (Verified in `rbac_security_audit.log`) |
| **Resource Overhead** | < 20% CPU spike during encryption | *See `/telemetry_data/resource_utilization.json`* |

---

## 🔬 How to Replicate Visualizations

If you wish to regenerate the charts from the raw telemetry data, a Python plotting script is included in this directory.

**Prerequisites:**
* Python 3.8+
* `matplotlib` and `pandas` libraries installed

**Run the generator:**
```bash
cd 06_Results_or_Expected_Output
python generate_charts.py --input telemetry_data/throughput_metrics.csv --output visualizations/
