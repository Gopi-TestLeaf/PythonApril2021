class A:

    def a(self):
        print("I'm from class A")


class B(A):
    
    def b(self):
        print("I'm from class B")

bbb = B()
bbb.a()
bbb.b()