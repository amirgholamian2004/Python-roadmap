from sensor import Sensor
import time
class Heater:
    def turn_on(self):
        print("HEATER ON")
    def turn_off(self):
        print("HEATER OFF")
    def reach_requested_temp(self, temp):
        measured_temp = Sensor().show()
        while measured_temp <= temp:
            print(f"temperature is-->{measured_temp}")
            measured_temp += 1
            time.sleep(1)

        self.turn_off()











