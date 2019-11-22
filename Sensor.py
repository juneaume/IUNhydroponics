## Brittany Armstrong
import RPi.GPIO as GPIO
import Adafruit_DHT

class Sensor:
    __hum1, __temp1 = Adafruit_DHT.read_retry(22, 23)
    __hum2, __temp2 = Adafruit_DHT.read_retry(22, 24)
    __hum3, __temp3 = Adafruit_DHT.read_retry(22, 25)

    __hums = [__hum1, __hum2, __hum3]
    __temps = [__temp1, __temp2, __temp3]

    def getReadH(self):
        return self.__hums

    def getReadT(self):
        return self.__temps