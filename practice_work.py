class TownCar:
    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print("TownCar go")
    
    def stop(self):
        print("TownCar go")

    def turn(self,direction):
        print("TownCar turn {}".format(direction))

class SportCar:
    def __init__(self,speed, color, name, is_police):
        TownCar.__init__(self, color, name, is_police)
        self.speed = 200
    def go():
        print("SportCar go")
    
    def stop():
        print("SportCar stop")

    def turn(direction):
        print("SportCar turn {}".format(direction))

class WorkCar:
    def __init__(self,speed, color, name, is_police):
        TownCar.__init__(self,speed, color, name, is_police)

    def go():
        print("WorkCar go")
    
    def stop():
        print("WorkCar stop")

    def turn(direction):
        print("WorkCar turn {}".format(direction))

class PoliceCar:
    def __init__(self,speed, color, name, is_police):
        TownCar.__init__(self,speed, color, name)
        self.is_police = True
    def go():
        print("PoliceCar go")
    
    def stop():
        print("PoliceCar stop")

    def turn(direction):
        print("PoliceCar turn {}".format(direction))

TownCar = TownCar("10","red","BMW",False)
TownCar.go()
TownCar.stop()
TownCar.turn("left")

SportCar.go()
SportCar.stop()
SportCar.turn("left")

WorkCar.go()
WorkCar.stop()
WorkCar.turn("left")

PoliceCar.go()
PoliceCar.stop()
PoliceCar.turn("left")
