import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename

file = pd.read_csv(askopenfilename(), sep=',', index_col=1)

df = pd.DataFrame(file)
times = df.index
temps = df[' AvgTemp']
hums = df[' AvgHum']

plt.figure()

plt.xlabel('Time')

plt.subplot(211)
plt.plot(times, temps)
plt.ylabel('Temperature (*C)')

plt.subplot(212)
plt.plot(times, hums)
plt.ylabel('Humidity (%)')


plt.suptitle('Testing')

plt.show()
