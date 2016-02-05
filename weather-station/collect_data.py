#!/usr/bin/python

import _mysql
from bme280_lib2 import *

sensor = BME280(mode=BME280_OSAMPLE_16)

db = _mysql.connect(host='localhost', port=3306, user='root', passwd='Eing9Cah&', db='weather')

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

sql_command = "INSERT INTO base_obs VALUES(NOW(), {0:0.3f}, {1:0.3f}, {2:0.3f});".format(degrees, humidity, hectopascals)

db.query(sql_command)

db.close()
