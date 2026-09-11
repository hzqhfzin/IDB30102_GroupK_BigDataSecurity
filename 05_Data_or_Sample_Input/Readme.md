# 📁 05_Data_or_Sample_Input

This directory contains the foundational datasets, configuration scripts, and access control profiles required to replicate the experimental testbed for the **Privacy-Preserving Big Data Security Framework**.

## 📂 Directory Contents

### 1. Synthetic Datasets (`/datasets`)
Contains the benchmark enterprise workloads used for ingestion testing and encryption benchmarking.
* **`structured_logs_sample.csv`** - A 100MB sample of the structured transaction logs.
* **`generate_synthetic_data.py`** - Python script to generate the full 10GB to 100GB datasets locally (bypassing GitHub file size limits).

### 2. Configuration Scripts (`/config`)
Contains the provisioning scripts used to set up the multi-node distributed cluster.
* **`hadoop_cluster_setup.yaml`** - Configuration for the Apache Hadoop (HDFS) master and worker nodes.
* **`spark_env_config.json`** - Apache Spark environment settings for distributed in-memory processing.

### 3. RBAC Profiles (`/rbac_policies`)
Contains the mock identities and matrices used to evaluate the Role-Based Access Control (RBAC) enforcement.
* **`user_identities.json`** - Mock user roles (e.g., Admin, Data Scientist, Guest, Malicious_Actor).
* **`access_matrix.xml`** - The fine-grained policy rules mapped to specific HDFS data blocks to test privilege escalation.

---

## 📊 Data Schema
The structured logs follow a standard enterprise telemetry format to simulate realistic Big Data ingestion:
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `timestamp` | DATETIME | The exact time of the transaction/log entry. |
| `user_id` | STRING | The unique identifier of the user or edge device. |
| `node_id` | STRING | The worker node handling the data block. |
| `payload` | STRING | The raw, unencrypted sensitive payload to be secured. |
| `clearance_level` | INTEGER | The RBAC clearance level required to access the record. |
