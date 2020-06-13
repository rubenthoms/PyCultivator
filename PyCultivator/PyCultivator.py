import subprocess
import sys

## A helper function for installing modules for this program if they are not existing.
#  
#  \param packageName Name of the package that shall be installed.
def maybeInstall(packageName):
    if importlib.util.find_spec(packageName) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", packageName])

if __name__ == "__main__":
    # Update pip.
    #subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade",  "pip"])
    # For file exchange with Git
    
    from PyQt5.QtWidgets import *
    from PyQt5 import QtCore
    app = QApplication(sys.argv)
    app.setApplicationVersion("1.0.0")

    from gui.MainWindow import MainWindow
    from core.Controller import Controller
    controller = Controller()
    window = MainWindow(controller)
    window.show()
    sys.exit(app.exec_())