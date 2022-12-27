from sense_hat import SenseHat
from gpiozero import MotionSensor
import math
import time
pir = MotionSensor(12)
sense = SenseHat()
n = (0, 0, 0)  # closed
rsin = ((math.sin(time.time()) + 1) / 2)
rsin *= 255.0
rsin = int(rsin)
r = (rsin, 0, 0)  # colou
heart = [
    n, n, n, n, n, n, n, n,
    n, r, r, n, n, r, r, n,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    n, r, r, r, r, r, r, n,
    n, n, r, r, r, r, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
]


class SenseData:
    def __init__(self):
        self.temp = sense.get_temperature()
        self.hum = sense.get_humidity()
        self.pres = sense.get_pressure()
        self.gyro = sense.get_gyroscope()
        self.comp = sense.get_compass()


def get_sense_data():
    dataObj = SenseData()
    return dataObj


def switch(direction):
    if direction == "":
        return "You can become a web developer."
    elif direction == "PHP":
        return "You can become a backend developer."
    elif direction == "Python":
        return "You can become a Data Scientist"
    elif direction == "Solidity":
        return "You can become a Blockchain developer."
    elif direction == "Java":
        return "You can become a mobile app developer"


obj = get_sense_data()
print(str(obj.temp), str(obj.hum), str(obj.pres))
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        # switch(event.direction)
    while pir.is_active:
        sense.set_pixels(heart)
    else:
        sense.clear()
