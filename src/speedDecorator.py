#comes from geeks for geeks with a few differences.
#was trying to wrapp the speed and mutiply it but i was having too many problems with that
#so i decided to return the values i wanted. This is the Decorator pattern
class MainSpeed:
    def __inti__(self):
        global speed
        speed = 4
    def setSpeed(self):
        return speed
class SpeedUp(MainSpeed):
    def __inti__(self, wrapped):
        self._wrapped = wrapped
    def setSpeed(self):
        return 8
class SlowDown(MainSpeed):
    def __inti__(self, wrapped):
        self.wrapped = wrapped
    def setSpeed(self):
        return 2
class normSpeed(MainSpeed):
    def __inti__(self, wrapped):
        self.wrapped = wrapped
    def setSpeed(self):
        return 4
    