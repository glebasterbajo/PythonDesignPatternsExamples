from abc import ABCMeta, abstractmethod

# Pizzas
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class MeatPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class ChickenPizza(MeatPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "on", type(VegPizza).__name__)


class HamPizza(MeatPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "on", type(VegPizza).__name__)


# Factories
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_meat_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_meat_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_meat_pizza(self):
        return HamPizza()


# Store
class PizzaStore:
    def make_pizzas(self):
        for factory in (IndianPizzaFactory(), USPizzaFactory()):
            self.factory = factory
            self.meat_pizza = self.factory.create_meat_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.meat_pizza.serve(self.veg_pizza)


if __name__ == "__main__":
    store = PizzaStore()
    store.make_pizzas()
