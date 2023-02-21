class s:
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def l(self):
        return 0.5 * self.a * self.t


p = s(10, 20)
print(p.l())