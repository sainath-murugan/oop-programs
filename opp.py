class vehicle():

    def __init__(self,name, mileage, wheels_quality, tank_capacity, colour):
        self.name = name
        self.mileage = mileage
        self.wheels_quality = wheels_quality
        self.tank_capacity = tank_capacity
        self.colour = colour
    def enginee(self,enginee):
        self.enginee = enginee
        return f"{self.name} has {enginee} enginee"

option = int(input("looking for which vechile in YAMAHA?\n1.Yamaha FZ S FI\n2.Yamaha YZF R15 V3\n3.Yamaha FZ25\n"))

constructor_1 = vehicle("Yamaha FZ S FI", "45km", "finite-grip", "12 liters", "red")
constructor_2 = vehicle("Yamaha YZF R15 V3", "40km", "super-finite grip", "12.5 liters", "teal-blue")
constructor_3 = vehicle("Yamaha FZ25", "35km", "solid-grip", "10liters", "Black")

if option == 1:
 print(constructor_1.name)
 print(constructor_1.mileage)
 print(constructor_1.wheels_quality)
 print(constructor_1.tank_capacity)
 print(constructor_1.colour)
 print(constructor_1.enginee("200cc"))

elif option == 2:

    print(constructor_2.name)
    print(constructor_2.mileage)
    print(constructor_2.wheels_quality)
    print(constructor_2.tank_capacity)
    print(constructor_2.colour)
    print(constructor_2.enginee("250cc"))

elif option == 3:

    print(constructor_3.name)
    print(constructor_3.mileage)
    print(constructor_3.wheels_quality)
    print(constructor_3.tank_capacity)
    print(constructor_3.colour)
    print(constructor_3.enginee("300cc"))


