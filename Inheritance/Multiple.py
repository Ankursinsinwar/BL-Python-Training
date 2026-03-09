'''
Multiple Inheritence
'''


class Camera:
    def take_photo(self):
        print("Taking photo")

class Phone:
    def make_call(self):
        print("Making call")

class SmartPhone(Camera, Phone):
    def play_music(self):
        print("Playing music")

s = SmartPhone()

s.take_photo()
s.make_call()
s.play_music()