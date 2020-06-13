from PyQt5.QtWidgets import QMainWindow
from core import Controller
from gui.ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """description of class"""
    def __init__(self, controller, parent = None):
        QMainWindow.__init__(self, parent)

        # Set up the user interface
        self.setupUi(self)


        self.controller = controller

        self.btn_startPump.toggled.connect(self.startStopPump)

    def startStopPump(self, checked: bool):
        if checked:
            self.controller.getComponent("PeristalticPump1").start()
        else:
            self.controller.getComponent("PeristalticPump1").stop()

