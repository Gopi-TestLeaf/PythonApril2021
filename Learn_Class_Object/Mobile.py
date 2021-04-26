class Mobile:

    def __init__(self, **kwargs):
        self.dial_list = kwargs

    def __str__(self):
        return "hello all"

    def dial_num(self, ph_num):
        for name, num in self.dial_list.items():
            if ph_num == num:
                print('dailing.......', name)

    def send_sms(self, ph_num):
        for name, num in self.dial_list.items():
            if ph_num == num:
                print('sending.......', name)


# Execution
mani = Mobile(Mano=12345, Sang=54321)
mani.dial_num(54321)
print(mani)


