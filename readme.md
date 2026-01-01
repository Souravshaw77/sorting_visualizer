# Sorting Algorithm Comparison Visualizer

A full-stack, Python-driven web application that visualizes and compares sorting algorithms side by side.  
The project bridges **theoretical time complexity (Big-O)** with **empirical execution behavior** using step-level analysis and real-time animations.

This tool is designed for **learning, analysis, and interview-ready demonstration** of algorithmic tradeoffs.

---

## Features

### Core
- Visualizes sorting algorithms step by step
- Python-based algorithm execution (Flask backend)
- Vanilla JavaScript frontend (no frameworks)

### Algorithm Comparison
- Side-by-side visualization on identical input
- Independent animation and metrics for each algorithm
- Fair comparison using cloned arrays

### Analysis & Metrics
- Real-time counts of:
  - Comparisons
  - Swaps
  - Total steps
- Time & space complexity display per algorithm
- Stability and in-place behavior indicators

### Big-O Overlay (Theory vs Practice)
- Actual observed steps vs theoretical growth trend
- Visual overlay comparing empirical work against expected Big-O
- Correctly models average-case behavior where applicable

---

##  Algorithms Implemented

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Each algorithm records **step-level operations** instead of directly sorting, enabling accurate visualization and analysis.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Architecture:** REST APIs + step-based execution model

---

## 📊 How Big-O Is Used (Important)

This project does **not** attempt to compute Big-O dynamically.

Instead:
- Big-O is treated as a **theoretical growth model**
- Observed steps are compared against expected growth trends
- This preserves academic correctness and avoids misleading claims

---