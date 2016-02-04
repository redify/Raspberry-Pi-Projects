#!/usr/bin/python

from bme280_lib2 import *
# import bme280_lib2

sensor = BME280(mode=BME280_OSAMPLE_16)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

print ('Timestamp = {0:0.3f}'.format(sensor.t_fine))
print ('Temp      = {0:0.3f} deg F'.format(degrees))
print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
print ('Humidity  = {0:0.2f} %'.format(humidity))
