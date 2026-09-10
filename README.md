# IDB30102: Distributed Big Data Security Framework

## Research Title
Design and Implementation of a Secure Storage and Privacy-Preserving Framework for Distributed Big Data Systems

## Group Details
* **Group Number:** Group K
* **Assigned Research Area:** Big Data Security and Distributed Systems
* **Course:** Bachelor of Cybersecurity Technology with Honours (UniKL)

### Group Members:
1. **Ikmal Hakimi Bin Muhaidi** (52215125391)
2. **Muhammad Anas Bin Mohd Ramlee** (52215125186)
3. **Muhammad Haziq Hafizin Bin Abd Rashid** (52215125933)
4. **Muhamad Azim Mustaqim Bin Azman** (52215125078)

---

## Research Overview

### Research Problem
1. **Unprotected Storage Nodes:** Many open-source and enterprise distributed storage platforms do not enforce mandatory data-at-rest encryption across individual worker nodes, exposing raw data if a node is compromised.
2. **High Latency From Traditional Encryption:** Heavy cryptographic operations across multi-terabyte datasets drastically degrade query throughput and system performance.

### Research Aim
To design, implement, and evaluate a secure storage framework that enforces data-at-rest encryption and privacy-preserving access controls for distributed Big Data platforms without degrading processing performance.

### Research Objectives
1. **RO1:** To evaluate existing security vulnerabilities and performance bottlenecks in distributed Big Data storage environments.
2. **RO2:** To develop a lightweight storage encryption module coupled with Role-Based Access Control (RBAC) designed specifically for multi-node data processing.
3. **RO3:** To measure the performance of the proposed framework in terms of encryption latency, data retrieval throughput, and unauthorized access prevention.

### Proposed Solution
A lightweight, privacy-preserving security framework integrated directly into distributed storage ingestion pipelines. It combines optimized AES encryption for data-at-rest with fine-grained Role-Based Access Control (RBAC) to secure worker nodes while maintaining high read/write throughput.

---

## Methodology & Evaluation

### Research Methodology & Development Model
* **Research Methodology:** Design Science Research (DSR) Framework.
* **Development Model:** Iterative Prototyping Model.

### Proposed Evaluation Plan
* **Baseline:** Standard unencrypted HDFS / distributed file system setup vs. traditional full-disk encryption methods.
* **Dataset / Test Environment:** Multi-node Linux cluster environment using synthetic multi-gigabyte log and CSV datasets.
* **Evaluation Metrics:**
  * **Encryption / Decryption Latency:** Measured in milliseconds (ms).
  * **System Throughput:** Measured in Megabytes per second (MB/s) during read/write operations.
  * **Access Policy Enforcement:** Verification rate (%) of unauthorized request blocking.

---

## Architecture & Technical Components

### Proposed System Architecture
The framework sits between the data ingestion layer and distributed storage worker nodes. Data streams are processed through an inline encryption engine managed by a Key Management Service (KMS), with access requests filtered by an RBAC policy engine before data access is granted across cluster nodes.

### Repository Structure & Technical Components
```text
.
├── 01_Research_Papers/           # Literature review source papers (PDFs)
├── 02_Literature_Review/          # Comparative tables & summary matrices
├── 03_Architecture_and_Flowchart/ # System architecture & workflow diagrams
├── 04_Source_Code/                # Encryption module & RBAC implementation code
├── 05_Data_or_Sample_Input/       # Benchmark test datasets & log samples
├── 06_Results_or_Expected_Output/ # Benchmark logs, charts, & performance data
├── 07_References/                 # BibTeX / APA citation files
└── README.md                      # Comprehensive project documentation
