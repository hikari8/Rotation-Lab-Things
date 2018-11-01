#!/usr/bin/env python3

"""
./growth_curve.py
Growth curve plots for Hv with CRISPRi plasmid"""

import sys
import matplotlib.pyplot as plt
import numpy as np

raw_data = open(sys.argv[1])
name_of_strain = sys.argv[1].split(".")[0]

interval = []
time = []
absorbance = []

for line in raw_data:
    if line.startswith("Time"):
        continue
    else:
        interval.append(int(line.split()[0]))
        time.append(float(line.split()[1]))
        absorbance.append(float(line.split()[2]))

od600 = np.array(absorbance)
actual_time = np.array(time)

"""
Ideally, I'd have a script to generlize this process and have growth curves overlaying
"""

# fig, ax = plt.subplots()
# plt.plot(actual_time, od600, color = "salmon")
# ax.set_xlabel("Time (hrs)")
# ax.set_ylabel("OD600")
# ax.set_xlim(0, 20)
# ax.set_ylim(0, 1.0)
# ax.set_title("Growth Curve \n" + str(name_of_strain))
# ax.set_xticks(np.arange(min(interval), max(interval), 2))
# ax.set_xticklabels(interval)
# plt.tight_layout()
# plt.savefig(str(name_of_strain) + " Growth Curve")
# plt.close()

fig, ax = plt.subplots()
plt.scatter(actual_time, od600, s = 5.0, color = "salmon")
ax.set_xlabel("Time (hrs)")
ax.set_ylabel("OD600")
ax.set_xlim(0, 52)
ax.set_ylim(0, 1.0)
ax.set_title("Growth Curve \n" + str(name_of_strain))
ax.set_xticks(np.arange(min(interval), max(interval), 2))
ax.set_xticklabels(interval)
plt.tight_layout()
plt.savefig(str(name_of_strain) + " Growth Curve")
plt.close()
