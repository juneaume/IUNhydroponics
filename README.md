# IUNhydroponics
Hydroponic system code

atlas_i2c.py contains the class used within the pHcode.py file

pHcode.py

  This will request a poll time and then return a time-stamped result. Any errors returned will be listed as "Error" instead of values. Currently it is unknown how to have the program retry the reading and only report once there is a value instead of listing every error. 
