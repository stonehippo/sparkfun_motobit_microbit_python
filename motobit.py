# microbit-module: motobit@0.1.0
# 
# Copyright (c) 2023 George White
# released under the MIT License
# https://github.com/stonehippo/sparkfun_motobit_microbit_python/blob/f5c03ebc07b7894ce560504145ce968ba26ef40d/LICENSE

from microbit import i2c
from micropython import const

i2c.init()

MOTOBIT_ADDR= const(89)
MOTOBIT_ENABLE = const(28673)
MOTOBIT_DISABLE = const(28672)
MOTOBIT_RIGHT_MOTOR= const(8192)
MOTOBIT_LEFT_MOTOR= const(8448)
MOTOBIT_FORWARD = const(0)
MOTOBIT_REVERSE = const(1)

# helper implementation of interp (map a value from one range to another)
def interp(v, a, b, a_prime, b_prime):
  if v > b:
     return b_prime
  if v < a:
    return a_prime
  return int(((v - a) / (b - a)) * (b_prime - a_prime) + a_prime)

def motobit_write(value):
  i2c.write(MOTOBIT_ADDR, (value).to_bytes(2, 'big'))
  
def motobit_enable():
  motobit_write(MOTOBIT_ENABLE)
  
def motobit_disable():
  motobit_write(MOTOBIT_DISABLE)
 
def motobit_set_speed(motor, direction = MOTOBIT_FORWARD, speed = 0):
  power = 0
  if direction == MOTOBIT_FORWARD:
    power = interp(speed, 0, 100, 0, 127) + 128
  else:
    power = interp(speed, 0, 100, 127, 0)
  motobit_write(motor + power)  

def motobit_invert(motor, invert = False):
  mode = 1 if invert else 0
  value = 4608 if motor == MOTOBIT_RIGHT_MOTOR else 4864
  motobit_write(value + mode)
