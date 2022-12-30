from sense_hat import SenseHat
from gpiozero import MotionSensor
from threading import Thread
from time import sleep, time
from csv import writer
import led_presets
import sys
from logzero import logger
import _thread
import os

pir = MotionSensor(12)
sense = SenseHat()

if sys.version_info[0:3] != (3, 9, 2):
    raise Exception('Requires python 3.9.2')


class SenseData:
    def __init__(self):
        self.temp = sense.get_temperature()
        self.hum = sense.get_humidity()
        self.pres = sense.get_pressure()
        self.gyro = sense.get_gyroscope()
        self.comp = sense.get_compass()
        self.pir = get_pir_state()


def exit_program():
    os._exit(0)


def get_sense_data():
    dataObj = SenseData()
    if dataObj:
        return dataObj
    else:
        logger.error("could not get sensor data!")
        return 0


def get_pir_state():
    if pir.is_active:
        return True
    else:
        return False


def log_data():
    with open('sense-data.csv', 'w', newline='') as csvfile:
        logger.info("created 'sense-data.csv'.")
        csv_writer = writer(csvfile)
        csv_writer.writerow(
            ['temperatur', 'pressure', 'humidity', 'pir', 'gyro', 'compass', 'timestamp'])
        logger.info("successfully written inital line into 'sense-data.csv'.")
        while True:
            obj = get_sense_data()
            logger.info(
                "successfully written line into 'sense-data.csv'.")
            csv_writer.writerow(
                [obj.temp, obj.pres, obj.hum, obj.pir, obj.gyro, obj.comp, time()])
            sleep(float(5))


def switchJoystick(direction):

    if direction == "left pressed":
        logger.info("left pressed")
        return
    elif direction == "left released":
        logger.info("left released")
        return
    elif direction == "right pressed":
        logger.info("right pressed")
        return
    elif direction == "right released":
        logger.info("right released")
        return
    elif direction == "up pressed":
        logger.info("up pressed")
        return
    elif direction == "up released":
        logger.info("up released")
        return
    elif direction == "down pressed":
        logger.info("down pressed")
        return
    elif direction == "down released":
        logger.info("down released")
        return
    elif direction == "middle pressed":
        logger.info("middle pressed")
        return
    elif direction == "middle released":
        logger.info("middle released. will exit now!")
        sense.clear()
        t = Thread(target=exit_program)
        t.start()


def flash_heart():
    while True:
        for event in sense.stick.get_events():
            # print(event.direction, event.action)
            switchJoystick(event.direction + " " + event.action)
        while pir.is_active:
            sense.set_pixels(led_presets.heart)
        else:
            sense.clear()


f = Thread(target=flash_heart)
l = Thread(target=log_data)
f.deamon = True
l.daemon = True
f.start()
l.start()

snooziness = int(10800)
sleep(snooziness)
