from components import Component, Pump
from time import sleep

class Controller(object):
    """description of class"""
    def __init__(self):
        self.components = {}
        self.components["PeristalticPump1"] = Pump.Pump(24, 23, 25)

    def getComponent(self, name: str) -> Component.Component:
        if name in self.components:
            return self.components[name]
        return None

