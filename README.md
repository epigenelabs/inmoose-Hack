<div align="center">
  <img src="docs/source/inmoose.png" width="600" alt="InMoose Logo">
  
  <h1>InMoose</h1>
  <p><strong>In</strong>tegrated <strong>M</strong>ulti-<strong>O</strong>mic <strong>O</strong>pen <strong>S</strong>ource <strong>E</strong>nvironment</p>
  
  <p>
    <a href="https://pypi.org/project/inmoose"><img src="https://img.shields.io/pypi/v/inmoose" alt="PyPI version"></a>
    <a href="https://pepy.tech/project/inmoose"><img src="https://static.pepy.tech/badge/inmoose" alt="PyPI Downloads"></a>
    <a href="https://pepy.tech/projects/inmoose"><img src="https://static.pepy.tech/badge/inmoose/month" alt="Monthly Downloads"></a>
    <a href="https://coveralls.io/github/epigenelabs/inmoose"><img src="https://img.shields.io/coverallsCoverage/github/epigenelabs/inmoose.svg" alt="Coverage"></a>
    <a href="https://inmoose.readthedocs.io/en/latest/?badge=latest"><img src="https://readthedocs.org/projects/inmoose/badge/?version=latest" alt="Documentation Status"></a>
    <a href="LICENSE"><img src="https://img.shields.io/pypi/l/inmoose" alt="License"></a>
  </p>
  
  <p>A comprehensive collection of tools for the analysis of omic data</p>
  
  <p>Developed and maintained by <img src="docs/source/epigenelogo.png" width="20"> <a href="https://www.epigenelabs.com/">Epigene Labs</a></p>
</div>

---

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📖 Documentation](#-documentation)
- [🧬 Batch Effect Correction](#-batch-effect-correction)
- [🔍 Cohort Quality Control](#-cohort-quality-control)
- [📊 Differential Expression Analysis](#-differential-expression-analysis)
- [🎯 Consensus Clustering](#-consensus-clustering)
- [📚 Citation](#-citation)
- [🤝 Contributing](#-contributing)

---

## 🚀 Quick Start

### Installation

Install InMoose directly from PyPI:

```bash
pip install inmoose
```

### Basic Usage

```python
from inmoose.pycombat import pycombat_norm, pycombat_seq

# Batch effect correction
microarray_corrected = pycombat_norm(microarray_data, microarray_batches)
rnaseq_corrected = pycombat_seq(rnaseq_data, rnaseq_batches)
```

---

## ✨ Features

InMoose provides a comprehensive suite of tools for multi-omic data analysis:

| Feature | Description | Supported Data Types |
|---------|-------------|---------------------|
| **Batch Effect Correction** | Remove technical biases from your data | Microarray, RNA-seq |
| **Quality Control** | Comprehensive QC with HTML reports | All expression data |
| **Differential Expression** | Find differentially expressed genes | Microarray, RNA-seq |
| **Consensus Clustering** | Robust clustering with confidence metrics | Any numeric data |

---

## 📖 Documentation

Comprehensive documentation is available on [ReadTheDocs](https://inmoose.readthedocs.io/en/latest/).

---

## 🧬 Batch Effect Correction

InMoose provides state-of-the-art batch effect correction methods for transcriptomic data:

### 🔬 Microarray Data
- **ComBat**: Python3 implementation superseding [pyCombat](https://github.com/epigenelabs/pycombat/)
- **Method**: Empirical Bayes approach for batch effect removal
- **Reference**: [Johnson et al., 2007](https://doi.org/10.1093/biostatistics/kxj037)

### 🧬 RNA-seq Data  
- **ComBat-Seq**: Python3 port optimized for count data
- **Method**: Negative binomial regression for batch correction
- **Reference**: [Zhang et al., 2020](https://doi.org/10.1093/nargab/lqaa078)

### Usage Example

```python
from inmoose.pycombat import pycombat_norm, pycombat_seq

# Correct microarray data
microarray_corrected = pycombat_norm(
    data=microarray_data,      # Expression matrix (genes × samples)
    batch=microarray_batches   # Batch labels for each sample
)

# Correct RNA-seq data  
rnaseq_corrected = pycombat_seq(
    data=rnaseq_data,         # Count matrix (genes × samples)
    batch=rnaseq_batches      # Batch labels for each sample
)
```

### Parameters

- **`data`**: Expression/count matrix with genes as rows and samples as columns
- **`batch`**: List of batch identifiers (same length as number of samples)

---

## 🔍 Cohort Quality Control

Perform comprehensive quality control analysis on your cohort datasets with automated reporting.

### CohortMetric Class

The `CohortMetric` class provides methods for quality control analysis:

#### Features
- 📊 **Principal Component Analysis (PCA)** - Assess data variation patterns
- 📈 **Sample Distribution Comparison** - Compare distributions across batches
- 🎯 **Batch Correction Quantification** - Measure correction effectiveness  
- 📏 **Silhouette Score Analysis** - Evaluate batch separation
- 🔀 **Entropy Calculation** - Assess sample mixing quality

#### Usage Example

```python
from inmoose.cohort_qc.cohort_metric import CohortMetric

# Initialize quality control analysis
cohort_qc = CohortMetric(
    clinical_df=clinical_data,
    batch_column="batch",
    data_expression_df=gene_expression_after_correction,
    data_expression_df_before=gene_expression_before_correction,
    covariates=["biopsy_site", "sample_type"]
)
```

### QCReport Class

Generate comprehensive HTML reports with visualizations:

```python
from inmoose.cohort_qc.qc_report import QCReport

# Generate interactive HTML report
qc_report = QCReport(cohort_qc)
qc_report.save_html_report_local(output_path='reports')
```

The report includes:
- 📊 Interactive PCA plots
- 📈 Before/after batch correction comparisons  
- 📋 Summary statistics and metrics
- 🎨 Professional visualizations

---

## 📊 Differential Expression Analysis

Identify differentially expressed genes using gold-standard statistical methods.

### 🔬 Microarray Analysis
- **limma**: The *de facto* standard for microarray differential expression
- **Reference**: [Ritchie et al., 2015](https://doi.org/10.1093/nar/gkv007)

### 🧬 RNA-seq Analysis  

#### edgeR
- **Method**: Exact tests for negative binomial models
- **Best for**: Simple experimental designs, small sample sizes
- **Reference**: [Robinson et al., 2010](https://doi.org/10.12688/f1000research.8987.2)

#### DESeq2  
- **Method**: Wald tests with empirical Bayes shrinkage
- **Best for**: Complex designs, larger sample sizes
- **Reference**: [Love et al., 2014](https://doi.org/10.1186/s13059-014-0550-8)

### Getting Started

Detailed usage examples and tutorials are available in the [documentation](https://inmoose.readthedocs.io/en/latest/).

---

## 🎯 Consensus Clustering

Determine optimal cluster numbers with confidence using resampling-based consensus clustering.

### Features
- 🔄 **Resampling-based approach** for robust clustering
- 📊 **Automatic optimal cluster detection**
- 📈 **Confidence metrics and stability analysis**
- 🔧 **Compatible with any scikit-learn clustering algorithm**

### Requirements
Your clustering algorithm must:
- Be instantiated with `n_clusters` parameter
- Have a `fit_predict` method

### Usage Example

```python
from inmoose.consensus_clustering.consensus_clustering import consensusClustering
from sklearn.cluster import AgglomerativeClustering

# Initialize consensus clustering
cc = consensusClustering(
    cluster=AgglomerativeClustering,
    min_k=2,
    max_k=10,
    nb_resampling_iteration=50
)

# Perform analysis
cc.compute_consensus_clustering(data_matrix)

# Get optimal number of clusters
optimal_k = cc.bestK
print(f"Optimal number of clusters: {optimal_k}")
```

### Outputs
- **Consensus matrices** for each cluster number
- **Stability metrics** and confidence scores
- **Visualization plots** for cluster assessment
- **Optimal cluster recommendation**

---

## 📚 Citation

When using InMoose, please cite the appropriate papers based on the features you use:

### Batch Effect Correction
```bibtex
@article{behdenna2023pycombat,
  title={pyComBat, a Python tool for batch effects correction in high-throughput molecular data using empirical Bayes methods},
  author={Behdenna, A and Colange, M and Haziza, J and Gema, A and Appé, G and Azencot, CA and Nordor, A},
  journal={BMC Bioinformatics},
  volume={24},
  number={1},
  pages={459},
  year={2023},
  doi={10.1186/s12859-023-05578-5}
}
```

### Differential Expression Analysis  
```bibtex
@article{colange2024differential,
  title={Differential Expression Analysis with InMoose, the Integrated Multi-Omic Open-Source Environment in Python},
  author={Colange, M and Appé, G and Meunier, L and Weill, S and Nordor, A and Behdenna, A},
  journal={BioRxiv},
  year={2024},
  doi={10.1101/XXX}
}
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/epigenelabs/inmoose/blob/master/CONTRIBUTING.md) for details on:

- 🐛 **Bug Reports** - Help us improve by reporting issues
- ✨ **Feature Requests** - Suggest new functionality  
- 🔧 **Code Contributions** - Submit pull requests
- 📖 **Documentation** - Improve our docs and examples

### Development Setup

```bash
# Clone the repository
git clone https://github.com/epigenelabs/inmoose-Hack.git
cd inmoose-Hack

# Install in development mode
pip install -e .
```

---

<div align="center">
  <p>Made with ❤️ by <a href="https://www.epigenelabs.com/">Epigene Labs</a></p>
  <p>
    <a href="https://github.com/epigenelabs/inmoose-Hack">🌟 Star us on GitHub</a> |
    <a href="https://inmoose.readthedocs.io/en/latest/">📖 Documentation</a> |
    <a href="https://pypi.org/project/inmoose/">📦 PyPI Package</a>
  </p>
</div>