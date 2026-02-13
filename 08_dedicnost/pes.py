class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno


class Pes(Zvire):
    def __init__(self, jmeno):
        super().__init__(jmeno)

    def zastekej(self):
        print("haf")


p = Pes("Azor")
p.zastekej()
