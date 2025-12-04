# Rust Standard Library Knowledge Graph (Open Source Edition)

<div align="center">

[![License: CC-BY-4.0](https://img.shields.io/badge/Data_License-CC--BY--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Tools License: MIT](https://img.shields.io/badge/Tools_License-MIT-blue.svg)](LICENSE)
[![Data Size](https://img.shields.io/badge/Data_Size-12MB_(Compressed)-green)]()
[![Powered By](https://img.shields.io/badge/Powered_By-RustMind_Labs-orange)]()

**The first complete, structural Knowledge Graph of the Rust Standard Library (v1.89.0).**

[ **Live Demo** ](https://rustkg.one) | [ **Download Data** ](data/dist/rust-std-1.89.0.nt.gz) | [ **Enterprise Services** ](#-enterprise--ecosystem-services)

</div>

---

## 🚀 Overview

Documentation is for humans; **Graphs are for AI and Machines.**

This project transforms the flat, textual documentation of the Rust Standard Library (`std`, `core`, `alloc`) into a **high-fidelity Semantic Knowledge Graph**. It captures the intricate web of Types, Traits, Implementations, and Source Code Indices that traditional tools miss.

**Why use this Graph?**
* 🤖 **For AI Fine-tuning**: Eliminate hallucinations by feeding your LLM with "Ground Truth" logic (e.g., "Does `Arc<T>` implement `Send`? Only if `T: Send + Sync`").
* 🔍 **For Code Audit**: Perform deep dependency analysis and "unsafe" propagation checks without parsing source code.
* 📚 **For Advanced Navigation**: Jump directly to the exact source code line for any item or trait implementation.

## 📦 Data Artifacts

The dataset is surgically sliced to ensure **Zero Copyright Risk** while retaining 100% of the logical structure.

- **File**: [`data/dist/rust-std-1.89.0.nt.gz`](data/dist/rust-std-1.89.0.nt.gz)
- **Format**: N-Triples (RDF), Gzipped.
- **Content**: `std`, `core`, `alloc`, `proc_macro`, `test`.
- **Logic Nodes**: **2.5 Million+** Triples.

> **Note**: Bulk documentation text (`fullDoc`) has been removed to comply with copyright policies. Structure and Links are fully preserved.

## 📊 Data Manifest (Transparency Report)

We believe in strict data auditing. Here is a summary of what you get:

| Count | Predicate | Description |
| :--- | :--- | :--- |
| **380,003** | `rdf:type` | Item definitions (Struct, Enum, Fn). |
| **318,716** | `owl:sameAs` | Re-export resolution (Essential for Rust!). |
| **161,263** | `prop:isDefinedOn` | Hierarchy (Method -> Struct). |
| **143,004** | `prop:hasSourceLink` | **Deep links to GitHub source code lines.** |
| **143,004** | `prop:hasLocalPath` | Relative path to HTML docs. |
| **16,798** | `prop:implDisambiguator` | Unique signatures for complex Trait impls. |
| **9,574** | `prop:hasTraitBound` | `where` clause constraints (The "Logic"). |

*(See [`docs/PREDICATES.md`](docs/PREDICATES.md) for full details)*

## 🛠️ Quick Start

### Python
We provide ready-to-use scripts in the `examples/` folder.

```bash
# 1. No extra dependencies required (Standard lib only)
# 2. Run the demo
python3 examples/2_find_traits.py
````

### Graph Database

You can import the `.nt.gz` file directly into **Oxigraph**, **Neo4j** (via n10s), or **Apache Jena**.

---

## 💼 Enterprise & Ecosystem Services

Need more than just `std`? **RustMind Labs** offers professional services for the full Rust ecosystem.

### 1. Full Ecosystem Graph ($$)

Access knowledge graphs for top crates like **Tokio, Axum, Serde, Bevy**, etc.

- **Feature**: Cross-crate dependency resolution.
    
- **Feature**: Version diffing (e.g., v1 vs v2 breaking changes).
    

### 2. High-Quality LLM Fine-tuning Datasets

We generate **Chain-of-Thought (CoT)** Q&A pairs based on this graph logic.

- **Perfect for**: Training "Code Copilot" models to understand Rust lifetimes and ownership.
    
- **Sample**: [Download 100 sample pairs here](https://www.google.com/search?q=%23) _(Coming Soon)_.
    

### 3. Private Codebase Analysis (On-Premise)

Deploy our **Extraction Engine** as a Docker container in your internal network.

- Analyze your private crates.
    
- Generate architecture diagrams automatically.
    
- **Zero Data Leakage**: Your code never leaves your server.
    

👉 **Contact us for pricing**: `leoxiang252@gmail.com`

---

## 📜 License

- **Data**: [CC-BY 4.0](https://www.google.com/search?q=DATA_LICENSE) - You can use it commercially, but you must attribute **RustMind Labs**.
    
- **Tools**: [MIT](https://www.google.com/search?q=LICENSE) - Code in `tools/` is open source.

