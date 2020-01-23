import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import time, datetime, os
import tkinter as tk
from tkinter import filedialog


class liveGraph():

	def __init__(self):
		w = tk.Tk(screenName = None, baseName = None, className = " Testing Live Graphing Functionality", useTk = 1)
		w.title("Testing Live Graphing Functionality")

		self.lab1 = tk.Label(w, text = "Close the program.", wraplength = "150")
		self.lab1.grid(row = 2, column = 2, padx = "10")
		self.lab2 = tk.Label(w, text = "Choose a file in which to import temperature and humidity data.", wraplength = "150")
		self.lab2.grid(row = 2, column = 1, padx = "10")
		self.but1 = tk.Button(w, text = "Close Window", command = w.destroy)
		self.but1.grid(row = 1, column = 2, pady = "10", padx = "10")
		self.but2 = tk.Button(w, text = "Choose Data", command = self.plot)
		self.but2.grid(row = 1, column = 1, padx = "10")

		w.mainloop()

	def newfile(self):
		file = filedialog.askopenfilename(
			initialdir = (os.environ['HOME'] + "/TempHum_Results"),
				title = "Select file",
				filetypes = [("Spreadsheets", "*.csv")])
		#file = pd.read_csv("/home/pi/TempHum_Results/2019-12-19_results.csv", sep=',', index_col=1)
		return file




	def xtickval(self, value):
		toUse = []
		for i in range(len(value)):
			if len(value) < 25:
				toUse.append(value[i])
			elif len(value) < 300:
				if (i % 10 == 0) == True:
					toUse.append(value[i])
			elif len(value) > 300:
				if (i % 50 == 0) == True:
					toUse.append(value[i])
		return toUse




	def plot(self):

		fig = plt.figure()
		ax1 = fig.add_subplot(1,1,1)

		global file
		file = self.newfile()

		def animate(i):
			df = pd.DataFrame(pd.read_csv(file, sep=',', index_col=1))
			df.set_axis(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], axis = 'columns', inplace = True)

			xar = df.index
			y1ar = df['B']
			y2ar = df['C']

			ax1.clear()
			ax1.plot(xar, y1ar, label = "Average Temperature")
			ax1.plot(xar, y2ar, label = "Average Humidity")
			plt.xticks(self.xtickval(xar))
			plt.suptitle("Temperature and Humidity for " + df.iloc[1]['A'])
			plt.grid(True)
			plt.legend(loc = 'upper left', borderaxespad = 0)
			plt.setp(ax1.get_xticklabels(), rotation = -25, ha = "left")


		ani = animation.FuncAnimation(fig, animate, interval = 1000)

		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())

		plt.show()

liveGraph()
