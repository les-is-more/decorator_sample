class User:
    def __init__(self, **kwargs):
        """This part abstracts the parameter/argument initialization.
        Basically, **kwargs is a dict that lists out the keys as parameters, and values as values.
        """
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def initiate_name(self):
        if hasattr(self,'name'):
            print("Hello, {}.".format(self.name))

    def is_registered(self):
        pass
