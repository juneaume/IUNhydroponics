# IUNhydroponics
Hydroponic system code


Sensor.py was an attempt to create a class that generated protected read values from the sensors. Implementation proved too tedious and this was abandoned.

Temphumsensors.py is the final product that takes readings from all 3 sensors and records those readings in a .csv file within the home directory. This file can be invoked on startup and runs in the background, sending data to the dated .csv file.
