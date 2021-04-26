# Encapsulation:
        # Data Hiding
        # Implementation Hiding

class TestLeaf:

    tl_ph_num = 123456789
    g_office_num = 420420
    _gpersonalnum = 54321

    def python(self):
        print('Python')


    def data_science(self):
        print('DS')


    def _arrangeInterviews(self):
        print('Related to Interviews')


    def get_data(self):
        return TestLeaf._gpersonalnum


    def set_data(self, new_ph_num):
        TestLeaf._gpersonalnum = new_ph_num

    def access_private_method(self):
        TestLeaf._arrangeInterviews(self)



per1 = TestLeaf()
print(per1.get_data())
per1.set_data('+443223108')
print(per1.get_data())
per1.access_private_method()