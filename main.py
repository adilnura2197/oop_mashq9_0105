class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("Transport harakatda")


class Bus(Transport):
    def __init__(self, brand, speed, seats, route):
        super().__init__(brand, speed)
        self.seats = seats
        self.route = route

    def move(self):
        super().move()
        print(f"Brend: {self.brand}")
        print(f"Marshrut: {self.route}")

    def passengers(self):
        print(f"O‘rindiqlar: {self.seats}")


b1 = Bus("Isuzu", 80, 40, "Toshkent - Samarqand")

b1.move()
b1.passengers()
