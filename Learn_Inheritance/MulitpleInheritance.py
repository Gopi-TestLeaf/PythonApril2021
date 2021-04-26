class GA:

    def ga(self):
        print("I'm from class GA")


class GB:

    def gb(self):
        print("I'm from class GB")

class GC:

    def gc(self):
        print("I'm from class GC")


class A(GA, GB):

    def a(self):
        print("I'm from Class A")

    def b(self):
        print("its me 'b', I'm from Class A")


class B(GC):

    def b(self):
        print("I'm from Class B")


class C(B, A):

    def c(self):
        print("I'm from Class C")


ccc = C()
ccc.gb()

print(C.__mro__) # MRO: Method Resolution Order

