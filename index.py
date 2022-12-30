from sense_hat import SenseHat
from gpiozero import MotionSensor
from threading import Thread
from time import sleep, time
import math
import csv

pir = MotionSensor(12)
sense = SenseHat()
n = (0, 0, 0)  # closed
rsin = ((math.sin(time()) + 1) / 2)
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
    sleep(float(5))
    dataObj = SenseData()
    # print
    return dataObj


def log_data():
    with open('sense-data.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)
        # Write the rows of data
        csv_writer.writerow(
            ['temperatur', 'pressure', 'humidity', 'gyro', 'compass', 'timestamp'])
        while True:
            obj = get_sense_data()
            csv_writer.writerow(
                [obj.temp, obj.pres, obj.hum, obj.gyro, obj.comp, time.time()])


def switchJoystick(direction, event):
    if direction == "left" & event == "pressed":
        return "left pressed"
    elif direction == "left" & event == "released":
        return "left released"
    elif direction == "right" & event == "pressed":
        return "right pressed"
    elif direction == "right" & event == "released":
        return "right released"
    elif direction == "up" & event == "pressed":
        return "up pressed"
    elif direction == "up" & event == "released":
        return "up released"
    elif direction == "down" & event == "pressed":
        return "down pressed"
    elif direction == "down" & event == "released":
        return "down pressed"
    elif direction == "middle" & event == "pressed":
        return "middle pressed"
    elif direction == "middle" & event == "released":
        sense.clear()
        exit(0)
        return "middle released"


# obj = get_sense_data()
# print(str(obj.temp), str(obj.hum), str(obj.pres))
def main():
    while True:
        for event in sense.stick.get_events():
            # print(event.direction, event.action)
            switchJoystick(event.direction, event.action)
        while pir.is_active:
            sense.set_pixels(heart)
        else:
            sense.clear()


m = Thread(target=main)
t = Thread(target=log_data)
m.deamon = True
t.daemon = True
m.start()
t.start()
snooziness = int(10800)
sleep(snooziness)
