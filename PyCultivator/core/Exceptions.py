
class PyCultivatorException(Exception):
    """Base class for other exceptions"""
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class PyCultivatorComponentGpioInUseException(PyCultivatorException):
    """Raised when a GPIO pin is already in use by another component"""
    def __init__(self, expression="", message=""):
        self.expression = expression
        self.message = message