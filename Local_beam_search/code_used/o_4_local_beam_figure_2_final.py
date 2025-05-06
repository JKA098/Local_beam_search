# This is the fourth file

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from o_2_local_beam_code_final import LocalBeamSearch

# Experiment parameters
n_values = [8, 12, 16, 20]
k_values = [1, 3, 5, 7]

# I got lazy, and decide to google if there is a way to select
# differnt values for n and k, without copying and pasting them myself
# And I got the following.
# the problem being, that, there is a possibility of getting 
# two different plot
# the references are the same as with: 3_local_beam_figure_1_final.py

results = []

for n in n_values:
    for k in k_values:
        lbs = LocalBeamSearch(n, k)
        best_state, attacks, runtime = lbs.run()
        results.append({"n": n, "k": k, "attacks": attacks, "runtime": runtime})

# Convert results to DataFrame
df_results = pd.DataFrame(results)

# Plot the effect of k on runtime for different n-queens
plt.figure(figsize=(10, 6))

for n in n_values:
    subset = df_results[df_results["n"] == n]
    plt.plot(subset["k"], subset["runtime"], label=f"n={n}", marker="*")

plt.xlabel("k (Number of states)")
plt.ylabel("Runtime (seconds)")
plt.title("Effect of k on Runtime for Different n(Board Sizes)")
plt.legend()
plt.grid(True)
plt.show()
