#!/usr/bin/python

import time
import ConfigParser

from tornado.web import RequestHandler
from tornado.escape import json_encode

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855


config = ConfigParser.ConfigParser()
config.read('/etc/kilnapi/kilnapi.conf')
logdir = config.get('defaults', 'logdir')
port = config.get('defaults', 'port')
public_port = config.get('defaults', 'public_port')
apikeyfile = config.get('defaults', 'apikeyfile')

# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

class Help(RequestHandler):
    def get(self):
        """Print available functions"""
        result = { 'Help' : 'Print available functions' }
        self.write(result)

class PubHelp(RequestHandler):
    def get(self):
       """Print available public functions"""
       result = { 'Help' : 'Print available public functions' }
       self.write(result)

def kiln_tempf():
    # Define a function to convert celsius to fahrenheit.
    def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

    temp = sensor.readTempC()
    output = '{1:0.2F}'.format(temp, c_to_f(temp))
    return output

class KilnTempF(RequestHandler):
    def get(self):
        """Get temperature of kiln in fahrenheit"""
        result = { 'tempf' : kiln_tempf() }
        callback = self.get_argument('callback')
        jsonp = "{jsfunc}({json});".format(jsfunc=callback,json=json_encode(result))
        self.set_header('Content-Type', 'application/javascript')
        self.write(jsonp)

