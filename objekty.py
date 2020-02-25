class Kruh:
    def __init__(self, _polomer):
        self.polomer = _polomer
        # self.farba=None

    def __str__(self):
        return "Kruh ma polomer {}".format(self.polomer)

    def __eq__(self, other):
        return self.polomer == other.polomer

    def __lt__(self, other):
        return self.polomer < other.polomer

    def __add__(self, other):
        if isinstance(other, Kruh):
            return Kruh(self.polomer+other.polomer)
        else:
            return Kruh(self.polomer+other)

    def __sub__(self, other):
        return Kruh(self.polomer-other.polomer)

    def __truediv__(self, other):
        return Kruh(self.polomer/other.polomer)

    def __mul__(self, other):
        return Kruh(self.polomer*other.polomer)

    def __iadd__(self, other):
        return Kruh(self.polomer+other)

    def __radd__(self, other):
        return Kruh(self.polomer+other)

    def obsah(self):
        return 3.14*self.polomer**2

    def obvod(self):
        return 2*3.14*self.polomer

    @property
    def polomer(self):
        return self.__polomer

    @polomer.setter
    def polomer(self, polomer):
        assert polomer > 0, "poloměř musí být nenulový a nezáporný"
        self.__polomer = polomer




Prvy = Kruh(-10)
Druhy = Kruh(5)
# print(Prvy.obsah())
# print(Prvy)
# if Prvy == Druhy:
    # print("rovnaju sa")
# else:
    # print("nerovnaju sa")
# Prvy += 5
# print(Prvy)
# print(Prvy+2)
# print(3+Prvy)
# print(Druhy+Prvy)
