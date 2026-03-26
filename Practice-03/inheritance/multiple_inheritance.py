#1
class Phone:
    def call(self):
        print("Making a voice call...")
class Camera:
    def take_photo(self):
        print("Capturing a high-res photo...")
# Inherits from BOTH Phone and Camera
class SmartPhone(Phone, Camera):
    def browse_internet(self):
        print("Surfing the web...")
# Usage:
iphone = SmartPhone()
iphone.call()        # From Phone
iphone.take_photo()  # From Camera
iphone.browse_internet()

#2
class LandVehicle:
    def drive(self):
        print("Driving on the road...")
class WaterVehicle:
    def swim(self):
        print("Sailing on the water...")
# Combines land and water capabilities
class AmphibiousCar(LandVehicle, WaterVehicle):
    def transform(self):
        print("Switching modes!")
# Usage:
hovercraft = AmphibiousCar()
hovercraft.drive()
hovercraft.swim()

#3
class TechSkills:
    def write_code(self):
        print("Writing Python logic...")
class ManagementSkills:
    def plan_budget(self):
        print("Planning the team budget...")
# The Lead Developer has both sets of skills
class LeadDeveloper(TechSkills, ManagementSkills):
    def mentor_team(self):
        print("Mentoring junior devs...")
# Usage:
dias = LeadDeveloper()
dias.write_code()    # From Tech
dias.plan_budget()   # From Management

#4
class ElectronicDevice:
    def power_on(self):
        print("Device is now ON.")
class NetworkDevice:
    def connect_to_wifi(self):
        print("Connecting to local WiFi...")
class SmartLight(ElectronicDevice, NetworkDevice):
    def set_brightness(self, level):
        print(f"Brightness set to {level}%")
# Usage:
bulb = SmartLight()
bulb.power_on()
bulb.connect_to_wifi()