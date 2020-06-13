from core.Exceptions import PyCultivatorComponentGpioInUseException
import platform
from enum import Enum

if platform.system() == "Linux":
    import RPi.GPIO as GPIO
else:
    from modules.RPiSim.GPIO import *


class GPIOPin(object):
    class Mode(Enum):
        In = 0
        Out = 1
        PWM = 2

    def __init__(self, pinNumber: int, Mode: Mode, frequencyInHz: float = 100.0):
        self.pinNumber = pinNumber
        self.Mode = Mode
        self.p = None
        if Mode == GPIOPin.Mode.In:
            GPIO.setup(pinNumber, GPIO.IN)
        elif Mode == GPIOPin.Mode.Out:
            GPIO.setup(pinNumber, GPIO.OUT)
            GPIO.output(self.pinNumber, GPIO.LOW)
        elif Mode == GPIOPin.Mode.PWM:
            GPIO.setup(pinNumber, GPIO.OUT)
            self.p = GPIO.PWM(pinNumber, frequencyInHz)

    def turnOn(self) -> bool:
        if self.Mode == GPIOPin.Mode.Out:
            GPIO.output(self.pinNumber, GPIO.HIGH)
            return True
        return False

    def turnOff(self) -> bool:
        if self.Mode == GPIOPin.Mode.Out:
            GPIO.output(self.pinNumber, GPIO.LOW)
            return True
        return False

    def start(self, dutyCycle: float) -> bool:
        if self.Mode == GPIOPin.Mode.PWM and self.p:
            self.p.start(dutyCycle)
            return True
        return False

    def changeDutyCycle(self, dutyCycle: float) -> bool:
        if self.Mode == GPIOPin.Mode.PWM and self.p:
            self.p.ChangeDutyCycle(dutyCycle)
            return True
        return False

## A base class for all electronical components
class Component(object):
    ## List storing all pins used by all component derivatives
    gpioPinsUsed = []
    def __init__(self):
        self.gpioPins = []
        if len(self.gpioPinsUsed) == 0:
            GPIO.setmode(GPIO.BCM)

    def __del__(self):
        for pin in self.gpioPins:
            self.gpioPinsUsed.remove(pin)

        if len(self.gpioPinsUsed) == 0:
            GPIO.cleanup()

    def registerPin(self, gpioPin: int, Mode: GPIOPin.Mode, frequencyInHz: float = 100.0) -> GPIOPin:
        if gpioPin in self.gpioPinsUsed:
            raise PyCultivatorComponentGpioInUseException()
            return False

        self.gpioPins.append(gpioPin)
        self.gpioPinsUsed.append(gpioPin)
        return GPIOPin(gpioPin, Mode, frequencyInHz)




