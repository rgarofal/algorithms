__author__ = 'rgarofal'


class Mediated:

    def __init__(self):
        self.mediator = None;

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)
        print "Chiamo on_change ereditata"

# Decoratore di classe
def mediated(Class):
    setattr(Class, "mediator", None)
    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)
        print "Chiamo on_change decorata"
    setattr(Class, "on_change", on_change)
    return Class


#with inheriting
class InHer1(Mediated):
    in1 = None
    def __init__(self):
        Mediated.__init__(self)
        self.in1 = 'Ereditata'

#with decorator pattern
@mediated
class NotHer1:
    in1 = None
    def __init__(self):
        self.in1 = 'Decorated'

if __name__ == "__main__":

    ih = InHer1()
    dh = NotHer1()

    print ih.in1
    print dh.in1

    ih.on_change()
    dh.on_change()