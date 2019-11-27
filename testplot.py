import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename

file = pd.read_csv(askopenfilename(), sep=',', index_col=1)

df = pd.DataFrame(file)
times = df['0']
temps = df['2']

plt.plot(times, temps)

plt.suptitle('Testing')

plt.show()
