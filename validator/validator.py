from functools import wraps
from time import time

class validators:
    # create a checker that will validate against the list below
    _validators = ['Str','UInt64','Float64','ASCII','isString']

    # include Error definitions

    def __init__(self,*args):
        self.rules = [*args]

    def __call__(self,func, *fargs,**fkwargs):
        @wraps(func)
        def wrapper(*fargs, **fkwargs):
            self.checker([*fargs])
            wrapped = func(*fargs,**fkwargs)
            return wrapped
        return wrapper  

    def checker(self,value):
        for rules in self.rules:
            if hasattr(self,rules.lower()):
                print("Instance requires the '{}' function, with args: {}".format(rules, value))
            else:
                raise AttributeError("Validator '{}' is not a valid one".format(rules))

            for v in value:
                try:
                    eval("self.{}('{}')".format(rules.lower(), v))
                except:
                    pass
    #checkers below will raise an Exception or Error whenever the values do not conform the set rules     
    @staticmethod
    def isstring(value: str):
        if isinstance(value, list):
            print('Value provided is of list type')
        elif isinstance(value, str):
             print("Value '{}' is of string type".format(value))

    @staticmethod
    def uint64(value: int):
        if isinstance(value, int):
            print('Value is an instance of unsigned integer.')

    @staticmethod
    def utf8(value):
        if isinstance(value,int):
            print('Value is an instance of signed integer.')


@validators('isString','UInt64','UTF9')
def remember(*args):
    print(' '.join(i for i in [*args]) )
    return [*args]

remember('lester', 'cajegas', 'data','scientist')
remember()
# print(inspect.getsource(remember))
