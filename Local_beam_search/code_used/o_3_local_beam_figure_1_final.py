# This is the third file

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from o_2_local_beam_code_final import LocalBeamSearch

#  parameters
n_values = [8, 12, 16, 20]
k_values = [1, 3, 5, 7]

# I got lazy, and decide to google if there is a way to select
# differnt values for n and k, without copying and pasting them myself
# And I got the following.
# the problem being, that, there is a possibility of getting 
# two different plot
results = []

for n in n_values:
    for k in k_values:
        lbs = LocalBeamSearch(n, k)
        best_state, attacks, runtime = lbs.run()
        results.append({"n": n, "k": k, "attacks": attacks, "runtime": runtime})

# Convert results to DataFrame
df_results = pd.DataFrame(results)


# Plot the effect of k on finding solutions for the different n queens
plt.figure(figsize=(10, 6))


for n in n_values:
    subset = df_results[df_results["n"] == n]
    # reference for learnig how to use subset[13]. * 
    # reference for learnig how to use marker[14]. *
    # reference for knowing how to do the following[15]. * 
    plt.plot(subset["k"], subset["attacks"], marker="o", label=f"n={n}")

plt.xlabel("k (Number of states)")
plt.ylabel("Number of Attacking Pairs (Lower is better)")
plt.title("Effect of k on Attacking Pairs")
plt.legend()
plt.grid(True)
plt.show()
