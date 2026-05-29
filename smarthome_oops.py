# Light system
class Light:
    def turn_on(self):
        print("Lights are ON")

    def turn_off(self):
        print("Lights are OFF")


# Temperature system
class Temperature:
    def set_temperature(self, temp):
        print(f"Temperature set to {temp}°C")


# Security alarm system
class SecurityAlarm:
    def activate(self):
        print("Security Alarm Activated")

    def deactivate(self):
        print("Security Alarm Deactivated")


# Smart Home Controller
class SmartHome:
    def __init__(self):
        self.light = Light()
        self.temperature = Temperature()
        self.alarm = SecurityAlarm()

    def home_mode(self):
        self.light.turn_on()
        self.temperature.set_temperature(24)
        self.alarm.deactivate()

    def away_mode(self):
        self.light.turn_off()
        self.temperature.set_temperature(18)
        self.alarm.activate()


# Create object
home = SmartHome()

print("Home Mode:")
home.home_mode()

print("\nAway Mode:")
home.away_mode()