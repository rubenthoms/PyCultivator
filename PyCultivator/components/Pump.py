from components.Component import Component, GPIOPin
from enum import Enum

## Class describing a virtual pump object driving a pump with a L298N motor driver.
class Pump(Component):
    minPwmDutyCycle = 80
    class Direction(Enum):
        Forwards = 0
        Backwards = 1

    class Status(Enum):
        Idling = 0
        Running = 1

    def __init__(self, in1: int, in2 : int, en: int):
        Component.__init__(self)
        ## GPIO pin connected to input 1 of the motor driver
        self.in1 = self.registerPin(in1, GPIOPin.Mode.Out)
        ## GPIO pin connected to input 2 of the motor driver
        self.in2 = self.registerPin(in2, GPIOPin.Mode.Out)
        ## GPIO pin connected to EN input of the motor driver
        self.en = self.registerPin(en, GPIOPin.Mode.PWM, 1000.0)
        ## The current speed of the pump [0-100%]
        self.speed = 100.0
        ## The direction the pump shall pump
        self.direction = Pump.Direction.Forwards
        ## The current status of the pump
        self.status = Pump.Status.Idling

    def start(self):
        if self.direction == Pump.Direction.Forwards:
            self.in1.turnOn()
            self.in2.turnOff()
        else:
            self.in1.turnOff()
            self.in2.turnOn()

        self.status = Pump.Status.Running

    def changeDirection(self, direction: Direction):
        if self.direction == Pump.Direction.Forwards:
            self.in1.turnOff()
            self.in2.turnOn()
            self.direction = Pump.Direction.Backwards
        else:
            self.in1.turnOn()
            self.in2.turnOff()
            self.direction = Pump.Direction.Forwards

    def stop(self):
        self.in1.turnOff()
        self.in2.turnOff()
        self.status = Pump.Status.Idling

    def changeSpeed(self, speed: int):
        self.speed = max(0, min(100, speed))
        en.changeDutyCycle(80 + 20 * self.speed / 100.0)






