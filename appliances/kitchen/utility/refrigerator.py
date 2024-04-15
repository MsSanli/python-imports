from appliances import Appliance

class Refrigerator(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def make_ice(self):
        print("something's wrong")
