# in main.py
from . import ar

class TextHandler:
    def __init__(self, lang='ar'):
      self.lang = lang.lower()

    def __getattr__(self, name):
        # get the module that matches the lang attribute
        module = globals()[self.lang]
        # get the nested class from the module
        subclass = getattr(module, self.lang)
        # create an instance of the nested class
        obj = subclass()
        # get the function that matches the name argument
        func = getattr(obj, name)
        # return the function
        return func
