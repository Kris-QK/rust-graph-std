# Predicate Dictionary & Data Manifest

This document provides a semantic definition of the predicates used in the Knowledge Graph and reports their distribution statistics.

## 📊 Predicate Statistics (Audit Report)

| Count | Predicate (Relation) | Semantic Meaning |
| :--- | :--- | :--- |
| **380,003** | `rdf:type` | Defines the item kind (Struct, Enum, Function, Trait). |
| **318,716** | `owl:sameAs` | **Re-exports**: Links items in `std` to their definition in `core` or `alloc`. |
| **219,236** | `rdfs:label` | The human-readable name of the item. |
| **161,263** | `prop:isDefinedOn` | **Hierarchy**: Parent linkage (e.g., Method belongs to Struct). |
| **143,004** | `prop:hasSourceLink` | **Deep Link**: URL to the specific line in the GitHub source code. |
| **143,004** | `prop:hasOnlineUrl` | Link to the official `doc.rust-lang.org` page. |
| **143,004** | `prop:hasLocalPath` | Relative file path to the HTML documentation (for offline tools). |
| **119,141** | `prop:hasInput` | Function argument types. |
| **119,141** | `prop:hasOutput` | Function return types. |
| **73,521** | `prop:docIsEmpty` | Boolean flag (`true`) if the item has no documentation text. |
| **16,798** | `prop:implDisambiguator` | **Advanced**: A unique signature string to distinguish multiple `impl` blocks. |
| **9,574** | `prop:hasTraitBound` | **Logic**: `where` clause constraints (e.g., `where T: Send + Sync`). |

## 🛡️ Clean Room Policy

To ensure compliance with copyright laws, the following predicates have been **removed** from the public release:
* `prop:fullDoc` (The bulk documentation text)
* `prop:hasExampleCode` (Code snippets in documentation)
