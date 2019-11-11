class Keymap:
    def __init__(self):
        pass

    def __call__(self):
        pass

    @classmethod
    def static(cls,*args, **kwargs):
        kMap = {"q": "quit",
        "F1": "help"
        }
        return kMap

    def keyMapper(stroke,keymap):
        assert stroke is str, "Provided stroke is missing or is not a string value"
        assert keymap is dict, "No keymap has been initialized."

        if not stroke in keymap.keys():
            print('Keyword provided is not allowed')
            break

        return getattr(self.static[stroke],Keymap())

    def quit(self):
        return 'quit()'
