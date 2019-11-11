from functools import wraps
from time import time

class validators:
    _validators = ['Str','UInt64','Float64','ASCII','isString']

    # include Error definitions

    def __init__(self,*args):
        self.rules = [*args]

    def __call__(self,func, *fargs,**fkwargs):
        @wraps(func)
        def wrapper(*fargs, **fkwargs):
            # how do we capture the result of the wrapped function?
            # this is where we manipulate the args and kwargs
            self.checker(value='test')
            wrapped = func(*fargs,**fkwargs)
            return wrapped
        return wrapper  

    def checker(self,value):
        for rules in self.rules:
            if hasattr(self,rules.lower()):
                print("Instance has the '{}' function, with args: {}".format(rules, value))
                try:
                    eval("self.{}('{}')".format(rules.lower(), value))
                except:
                    pass
                
    @staticmethod
    def isstring(value: str):
        if isinstance(value, list):
            print('Value provided is of list type')
        elif isinstance(value, str):
            return True

    @staticmethod
    def uint64(value: int):
        if isinstance(value, int):
            print('Value is an instance of unsigned integer.')

    @staticmethod
    def utf8(value):
        if isinstance(value,int):
            print('Value is an instance of signed integer.')


@validators('isString','UInt64','UTF8')
def remember(*args):
    print(' '.join(i for i in [*args]) )
    return [*args]

remember('lester', 'cajegas', 'data','scientist')
# print(inspect.getsource(remember))
