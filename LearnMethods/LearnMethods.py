class Hospital:

    def adm(self):                          # instance method
        print('Admin')

    def doctor(self):
        print("Doctor Name: ")

    @classmethod
    def police_info(cls):                   # class method
        print('police: enq')

    @staticmethod
    def yoga_details():                     # static Method
        print("some info related to yoga")
        
d1 = Hospital()
d1.doctor()
d1.police_info()
d1.yoga_details()

Hospital.police_info()
Hospital.yoga_details()