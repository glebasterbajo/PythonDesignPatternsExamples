class EventManager:
    def __init__(self):
        print("Event Manager: Let's talk to the folks")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier:
    def bookHotel(self):
        print(f"{self.__class__} got the task!")


class Florist:
    def setFlowerRequirements(self):
        print(f"{self.__class__} got the task!")


class Caterer:
    def setCuisine(self):
        print(f"{self.__class__} got the task!")


class Musician:
    def setMusicType(self):
        print(f"{self.__class__} got the task!")


class Client:
    def askEventManager(self):
        em = EventManager()
        em.arrange()


if __name__ == "__main__":
    c = Client()
    c.askEventManager()
