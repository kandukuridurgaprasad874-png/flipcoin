# Camera class
class Camera:
    def take_photo(self):
        print("Photo captured")


# Music Player class
class MusicPlayer:
    def play_music(self):
        print("Playing music")


# GPS class
class GPS:
    def navigate(self):
        print("Navigating to destination")


# Smartphone class inherits all features
class Smartphone(Camera, MusicPlayer, GPS):
    def device_info(self):
        print("Smartphone with multiple features")


# Object
phone = Smartphone()

phone.device_info()
phone.take_photo()
phone.play_music()
phone.navigate()