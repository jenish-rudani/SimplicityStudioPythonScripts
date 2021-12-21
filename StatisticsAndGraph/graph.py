import os
import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import figure
figure(figsize=(12, 8), dpi=300)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
print(ROOT_DIR)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

headers = ["#Device ID", "Time (us)", "Current (mA)", "Voltage (V)",
           "PC", "Function Name", "File Name", "Line number"]

df = pd.read_csv('{}\EnergyProfile_12-21.csv'.format(ROOT_DIR), names=headers, sep=';')
# print(df)

x = df[headers[1]][1:]
y = df[headers[2]]
x = pd.to_numeric(x, downcast="float")
y = pd.to_numeric(y[1:], downcast="float")

totalTimeInUs = x[len(x)]
totalTimeInSeconds = totalTimeInUs / 1000000
print("Total Time in Seconds : {}".format(totalTimeInSeconds))

meanCurrentValue = y.mean()
print("Average Current for this duration : {} uA/s".format(meanCurrentValue*1000))

print("Peak Value for this duaration : {} mA".format(y.max()))

x = [x[i+1]/1000000 for i in range(len(x))]

plt.plot(x, y,linewidth=1)


plt.title("OTA FW Update Power Consumption Profile",loc = 'left')
plt.xlabel("Time Index (s)")
plt.ylabel("Current (mA)")
plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)
plt.savefig('plot.png')
plt.show()

