# create car methods and classes. commit



class car:
    print("Start of car class")
    def start(self):
        print ("Start the car")

    def stop(self):
        print ("Stop the car")

    print("End of car class")


class sportscar():
    print("Start of sportscar class")

    def Aerodynamics(self):
        print ("Start the Aerodynamics")

    def top_Speed(self):
        print ("This is top speed")

    print("End of sportscar class")

class bmw(car,sportscar):
    print("Start of bmw class")
    def parkingassistance(self):
        print ("This is parking assistance")

    print("End of bmw class")



c1 = car()
c1.start()
c1.stop()


c2 = sportscar()
c2.Aerodynamics()
c2.top_Speed()

c3=bmw()
c3.top_Speed()
c3.stop()
c3.start()
c3.Aerodynamics()
c3.parkingassistance()