class A:

    def a(self):
        print("I'm from class A")


class B(A):

    def b(self):
        print("I'm from class B")



class C(B):

    def d(self):
        print("I'm from class C")

ccc = C()
ccc.d()
ccc.b()
ccc.a()
