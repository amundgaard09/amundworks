
class NotConnectedError(Exception):
    def __init__(self, *args):
        super().__init__("Internet connection could not be established.", (str(arg) + "\n" for arg in args))

class UnknownOSError(Exception):
    def __init__(self, *args):
        super().__init__("Unknown OS Error.", (str(arg) + "\n" for arg in args))

class UnknownEmotionError(Exception):
    def __init__(self, *args):
        super().__init__("Unknown Emotion Error.", (str(arg) + "\n" for arg in args))

class MissingFileError(Exception):
    def __init__(self, *args):
        super().__init__("Missing file:", (str(arg) + "\n" for arg in args))

class SkillLoadError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
