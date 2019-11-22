#!/user/bin/env python

import io
import fcntl
import datetime
import time
import string
from atlas_i2c import atlas_i2c

def main():
	device = atlas_i2c()  

	# creates the I2C port object,specify the address or bus if necessary
	print(">> Continuously polls the board every xx.x seconds,")
	print(" where xx.x is longer than the {} second timeout.".format(atlas_i2c.long_timeout))
	print(" Pressing ctrl-c will stop the polling")

	# main loop
	while True:
		polltime = float(input("Enter poll time: "))
		if(polltime < atlas_i2c.long_timeout):
			print("Polling time is shorter than timeout, setting polling time to {}".format(atlas_i2c.long_timeout))
			polltime = atlas_i2c.long_timeout

		try:
			while True:
				timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
				value = device.query("R")
				print(timestamp + "\t pH: " + value)
				time.sleep(polltime - atlas_i2c.long_timeout)
		except KeyboardInterrupt():
			# catches the ctrl-c command, which breaks the loop above
			print("Continuous polling stopped.")

	# if not a special keyword, pass commands straight to board
	else:
		try:
			print(device.query(polltime))
		except IOError:
			print("Query failed.")


if __name__ == '__main__':
	main()
