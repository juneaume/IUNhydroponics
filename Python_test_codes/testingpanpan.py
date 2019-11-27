import pandas as pd
from tkinter.filedialog import askopenfilename

file = pd.read_csv(askopenfilename(), sep=',', index_col=1)

data = pd.DataFrame(file)


print(data[[' AvgTemp', ' AvgHum']])


