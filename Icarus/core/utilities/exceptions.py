
class NotConnectedError(Exception):
    def __init__(self, *args):
        super().__init__("Internet Connection not established.", *args) 

    
