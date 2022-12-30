from sense_hat import SenseHat
from gpiozero import MotionSensor
from threading import Thread
from time import sleep, time
import csv
import led_presets

pir = MotionSensor(12)
sense = SenseHat()


class SenseData:
    def __init__(self):
        self.temp = sense.get_temperature()
        self.hum = sense.get_humidity()
        self.pres = sense.get_pressure()
        self.gyro = sense.get_gyroscope()
        self.comp = sense.get_compass()
        self.pir = get_pir_state()


def get_sense_data():
    dataObj = SenseData()
    return dataObj


def get_pir_state():
    if pir.is_active:
        return True
    else:
        return False


def log_data():
    with open('sense-data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ['temperatur', 'pressure', 'humidity', 'pir', 'gyro', 'compass', 'timestamp'])
        while True:
            obj = get_sense_data()
            csv_writer.writerow(
                [obj.temp, obj.pres, obj.hum, obj.pir, obj.gyro, obj.comp, time()])
            sleep(float(5))


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


def flash_heart():
    while True:
        for event in sense.stick.get_events():
            # print(event.direction, event.action)
            switchJoystick(event.direction, event.action)
        while pir.is_active:
            sense.set_pixels(led_presets.heart)
        else:
            sense.clear()


def main():
    m = Thread(target=flash_heart)
    t = Thread(target=log_data)
    m.deamon = True
    t.daemon = True
    m.start()
    t.start()
    snooziness = int(10800)
    sleep(snooziness)


main()
