__author__ = 'rgarofal'


class Prova:

    def __init__(self, max_value):
        self.init_value = max_value

    @property
    def print_max(self):
        return self.init_value

    def check_max(self, value):
        if value > self.init_value:
            print "Value e' piu' grande"

    def reset_max(self, value):
        self.init_value = value

def add(self, addendum):
    self.init_value += addendum

if __name__ == "__main__":
    ggg = Prova(30)
    print ggg.print_max
    ggg.check_max(40)
    ggg.reset_max(20)
    Prova.add = add

    ggg.add(3)
    print ggg.print_max
