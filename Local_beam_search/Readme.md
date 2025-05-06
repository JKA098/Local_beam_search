# ♟️ Local Beam Search for Solving the n-Queens Problem

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Focus](https://img.shields.io/badge/focus-Heuristic%20Search-blueviolet)
![Theme](https://img.shields.io/badge/theme-n--Queens%20Problem-brightgreen)
![Data](https://img.shields.io/badge/data%20analysis-Pandas-lightgrey)
![Statistics](https://img.shields.io/badge/statistical%20tests-Runtime%20%7C%20Accuracy-blue)
![ML](https://img.shields.io/badge/algorithm-Local%20Beam%20Search-orange)
![Framework](https://img.shields.io/badge/framework-Custom%20Implementation-informational)
![Editor](https://img.shields.io/badge/editor-Jupyter%20%7C%20PyCharm-orange)

---

## 📌 Overview

This project applies the **Local Beam Search (LBS)** algorithm to solve the **n-Queens problem**, with the goal of minimizing the number of attacking queen pairs on an `n x n` chessboard.

Using various configurations of `n` (board size) and `k` (number of beam states), the project explores how these parameters impact the ability to find optimal solutions and the associated runtime performance.


---

## 🎯 Objectives

1. Implement Local Beam Search for the n-Queens problem.
2. Visualize and compare how `k` (number of states) affects the ability to find solutions.
3. Analyze runtime trends and solution quality using graphs.
4. Report observations and trade-offs as `n` and `k` vary.

---

## 🚧 Deliverables

* [x] `o_1_other_fn_local_beam_code_final.py`: Core functions for state generation, heuristic evaluation, and successor generation.
* [x] `o_2_local_beam_code_final.py`: Full class-based implementation of the Local Beam Search algorithm.
* [x] `3_local_beam_figure_1_final.py`: Visualization of attacking pairs vs. `k`.
* [x] `4_local_beam_figure_2_final.py`: Visualization of runtime vs. `k`.


---

## 🧠 Algorithm Summary

### 🔹 State Representation

* A 1D NumPy array where the index represents the column and the value represents the row of a queen.

### 🔹 Heuristic

* Number of attacking queen pairs based on row and diagonal conflicts.

### 🔹 Local Beam Search Logic

1. Initialize `k` random states.
2. At each iteration:

   * Generate all successors from current `k` states.
   * Compute heuristic scores for all.
   * Select the `k` best states.
3. Stop if:

   * A solution (0 attacks) is found.
   * All states have the same score (local minima).
   * Maximum iterations are reached.

---

## 🧪 Sample Execution

```python
n_values = [......] # replace dots by numbers
k_values = [[......]] # replace dots by numbers

for n in n_values:
    for k in k_values:
        print(f"\n🚀 Running Local Beam Search for n={n}, k={k}...")
        lbs = LocalBeamSearch(n, k)
        lbs.run()
```

Output includes:

* Final board configuration
* Number of attacking pairs
* Runtime
* Whether it found a solution or got stuck in a local minimum

---

## 📊 Visualization Examples

### 🔸 Attacking Pairs vs k

* Shows how increasing `k` affects the solution quality.

### 🔸 Runtime vs k

* Plots how computation time changes as `k` increases.

Both figures highlight the **trade-off** between **solution accuracy** and **execution time**.

---

## 🤔 Key Insights

1. **Higher `k`** improves the chances of finding optimal solutions.
2. **Runtime increases** with `k`, revealing a performance trade-off.
3. Local minima are more likely with small `k` and large `n`.
4. For very large `n`, LBS becomes computationally expensive and may stagnate.

---

## 📄 License

Licensed under the **Apache 2.0 License**. Open for use, reuse, and modification with attribution.





---

📘 *References used within code are cited in-line with numbered annotations, aiding transparency and traceability for debugging logic and function behavior.*
