# sparkfun_motobit_microbit_python
A micro:bit Python implementation of the Sparkfun Moto:bit driver.

The [Sparkfun moto:bit](https://www.sparkfun.com/products/15713) is a carrier board for the [BBC micro:bit](https://microbit.org) that provides a set of motor and servo drivers, sensor inputs, and an I2C interface for simple robotics.

Sparkfun created a PXT driver for use with the MakeCode development environment, which provides a simple set of controls for the motor driver interface. However, there is no library module for use the [micro:bit MicroPython implementation](https://python.microbit.org/v/3/api) -- until now.

This driver is a simple reimplementation of the API from the PXT module, with a couple of small changes:

- The enable() method has been split into discrete enable and disable functions
- The speed setting method has some default parameters
- The module includes a basic implementation of `interp`, since the micro:bit doesn't include MicroPython's _ulab_

## Usage

```
from motobit import *

# turn on the motors; and don't forget that there's a hardware switch on the moto:bit!
motobit_enable()

# speed represents present of motor power from 0-100%
motobit_set_speed(MOTOBIT_RIGHT_MOTOR, speed=100, direction=MOTOBIT_FORWARD)
motobit_set_speed(MOTOBIT_RIGHT_MOTOR, speed=100) # default direction is forward

motobit_invert(MOTOBIT_RIGHT_MOTOR, True) # reverse the right motor
motobit_invert(MOTOBIT_RIGHT_MOTOR) # flip it back using the default of False

motobit_disable() # disable the motor driver (the current speed is still set and will resume if the motor driver is enabled again)
```

## References

[Sparkfun moto:bit](https://www.sparkfun.com/products/15713)
[moto:bit MakeCode PXT driver](https://github.com/sparkfun/pxt-moto-bit)
