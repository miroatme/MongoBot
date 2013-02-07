import inspect

# TODO: decorator to support command aliases

class Dendrite(object):
    def __init__(self, cortex):
        self.cx = cortex
    
    def chat(self, what):
        self.cx.chat(what)

    def snag(self):
        self.values = self.cx.values
        self.lastsender = self.cx.lastsender
        self.context = self.cx.context


def serotonin(cortex, expansion):
    methods = inspect.getmembers(expansion)
    letter = expansion.category[:1]
    word = expansion.category[1:]

    helps = []

    for name, method in methods:
        if not hasattr(method, "create_command"):
            continue

        if hasattr(method, "help"):
            helps.append("~" + name + " " + method.help)

        if name in cortex.commands:
            print "Warning: overwriting " + name

        cortex.commands[name] = method

    if len(helps):
        if letter in cortex.helpmenu:
            print "Warning: overwriting category " + letter + " in help menu"

        cortex.helpmenu[letter] = helps
        cortex.helpcategories.append("(" + letter + ")" + word)
        
def category(text):
    def add(cls):
        cls.category = text
        return cls
    return add 

def axon(fn):
    fn.create_command = True 
    return fn

def help(text):
    def add(fn):
        fn.help = text
        return fn
    return add 

# TODO: make implicit?
def snag(expansion, cortex):
    expansion.values = cortex.values
    expansion.lastsender = cortex.lastsender
