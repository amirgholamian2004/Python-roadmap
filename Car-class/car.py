from heater import Heater
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        self.heater = Heater()
    def brake(self):
        print(f"car with model--> {self.model} just braked.")
    def turn_heater_on(self, temp= 25):
        self.heater.turn_on()
        self.heater.reach_requested_temp(temp)
car1 = Car("BMW", "black", 2020)
car1.turn_heater_on()




