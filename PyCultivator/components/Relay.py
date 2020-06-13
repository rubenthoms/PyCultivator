from components.Component import Component

## Class describing a virtual relay object operating a physical relay.
class Pump(Component):
    def __init__(self, controlPin: int):
        Component.__init__(self)
        ## The GPIO pin for controlling the relay
        self.controlPin = controlPin

        self.registerPin(controlPin)