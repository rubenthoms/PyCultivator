from components.Component import Component, GPIOPin
from enum import Enum

## Class describing a virtual pump object driving a pump with a L298N motor driver.
class LedLamp(Component):
    minPwmDutyCycle = 80

    class Status(Enum):
        Off = 0
        On = 1

    def __init__(self, in1: int, in2 : int, en: int):
        Component.__init__(self)
        ## GPIO pin connected to input 1 of the led driver
        self.in1 = self.registerPin(in1, GPIOPin.Mode.Out)
        ## GPIO pin connected to EN input of the led driver
        self.en = self.registerPin(en, GPIOPin.Mode.PWM, 1000.0)
        self.en.start(100)
        ## The current speed of the pump [0-100%]
        self.speed = 100.0
        ## The current status of the pump
        self.status = LedLamp.Status.Off

    def switchOn(self):
        self.in1.turnOn()

        self.status = LedLamp.Status.On

    def switchOff(self):
        self.in1.turnOff()
        self.in2.turnOff()
        self.status = LedLamp.Status.Off

    def changeBrightness(self, brightness: int):
        self.speed = max(0, min(100, brightness))
        en.changeDutyCycle(80 + 20 * self.brightness / 100.0)






