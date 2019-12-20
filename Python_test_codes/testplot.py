import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename

file = pd.read_csv(askopenfilename(), sep=',', index_col=1)
#file = pd.read_csv("/home/pi/TempHum_Results/2019-12-19_results.csv", sep=',', index_col=1)

df = pd.DataFrame(file)
df.set_axis(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], axis='columns', inplace=True)
times = df.index

othert = df['H']
s1t = df['D']
s2t = df['F']
twot = othert.append(s1t, ignore_index=True)
allt = twot.append(s2t, ignore_index=True)

otherh = df['I']
s1h = df['E']
s2h = df['G']
twoh = otherh.append(s1h, ignore_index=True)
allh = twoh.append(s2h, ignore_index=True)

atemps = df['B']
ahums = df['C']

def xtickval(value):
	toUse = []
	for i in range(len(value)):
		if len(value) < 300:
			if (i % 10 == 0) == True:
				toUse.append(df.index[i])
		elif len(value) > 300:
			if (i % 100 == 0) == True:
				toUse.append(df.index[i])
	return toUse

plt.figure()

ax1 = plt.subplot(211)
ax1.plot(times, atemps, color="green")
plt.xlim(min(times), max(times))
#plt.ylim(min(allt), max(allt))
plt.ylabel('Temperature (*C)')
plt.xticks(xtickval(df.index))
plt.setp(ax1.get_xticklabels(), rotation = -25, ha = "left")

offset = -72
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(arrowstyle = "->", connectionstyle = "angle,angleA=0,angleB=90,rad=10")

ax1.annotate((
	"Maximum " + str(atemps.max()) + '*C at' + str(atemps.idxmax())),
	xy=(atemps.idxmax(), atemps.max()),
	xytext=(offset, 2.5*offset), textcoords='offset points',
	bbox=bbox, arrowprops = arrowprops)

plt.grid(True)

ax2 = plt.subplot(212)
ax2.plot(times, ahums, color="purple")
plt.xlim(min(times), max(times))
#plt.ylim(min(allh), max(allh))
plt.xlabel('Time between' + str(min(times)) + 'and' + str(max(times)))
plt.ylabel('Humidity (%)')
plt.xticks(xtickval(df.index))
plt.setp(ax2.get_xticklabels(), rotation = -25, ha = "left")

ax2.annotate((
	"Maximum " + str(ahums.max()) + '% at' + str(ahums.idxmax())),
	xy=(ahums.idxmax(), ahums.max()),
	xytext=(offset, 2.5*offset), textcoords='offset points',
	bbox = bbox, arrowprops = arrowprops)

plt.grid(True)

plt.suptitle("Temperature and Humidity for " + df.iloc[1]['A'])

plt.show()
