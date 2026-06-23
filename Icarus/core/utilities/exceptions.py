
class NotConnectedError(Exception):
    def __init__(self, *args):
        super().__init__("Internet connection could not be established.", (arg + "\n" for arg in args)) 

class UnknownOSError(Exception):
    def __init__(self, *args):
        super().__init__("Unknown OS Error.", (arg + "\n" for arg in args)) 

class UnknownEmotionError(Exception):
    def __init__(self, *args):
        super().__init__("Unknown Emotion Error.", (arg + "\n" for arg in args)) 


    
    
