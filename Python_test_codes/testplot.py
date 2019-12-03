import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename

file = pd.read_csv(askopenfilename(), sep=',', index_col=1)
#file = pd.read_csv("/home/pi/2019-11-27_results.csv", sep=',', index_col=1)

df = pd.DataFrame(file)
times = df.index

othert = df[' S3Temp']
s1t = df[' S1Temp']
s2t = df[' S2Temp']
twot = othert.append(s1t, ignore_index=True)
allt = twot.append(s2t, ignore_index=True)

otherh = df[' S3Hum ']
s1h = df[' S1Hum']
s2h = df[' S2Hum']
twoh = otherh.append(s1h, ignore_index=True)
allh = twoh.append(s2h, ignore_index=True)

atemps = df[' AvgTemp']
ahums = df[' AvgHum']

plt.figure()


plt.subplot(211)
plt.plot(times, atemps)
plt.xlim(min(times), max(times))
plt.ylim(min(allt), max(allt))
plt.xticks([])
plt.xlabel('Time between' + str(min(times)) + 'and' + str(max(times)))
plt.ylabel('Temperature (*C)')

plt.subplot(212)
plt.plot(times, ahums)
plt.xlim(min(times), max(times))
plt.ylim(min(allh), max(allh))
plt.xticks([])
plt.xlabel('Time between' + str(min(times)) + 'and' + str(max(times)))
plt.ylabel('Humidity (%)')



plt.suptitle("Temperature and Humidity for " + df.iloc[1]['Date'])

plt.show()
