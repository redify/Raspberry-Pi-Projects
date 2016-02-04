#!/usr/bin/python

import pymysql
from bme280_lib2 import *


sensor = BME280(mode=BME280_OSAMPLE_16)

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Eing9Cah&', db='weather')
cur = db.cursor()

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

sql_command = "INSERT INTO base_obs VALUES(NOW(), {0:0.2f}, {1:0.2f}, {2:0.2f});".format(degrees, humidity, hectopascals)
#print (sql_command)
#exit()

cur.execute(sql_command)

cur.close()
db.close()
