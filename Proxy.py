from abc import ABCMeta, abstractmethod


class Actor:
    def __init__(self):
        self.busy = False

    def occupied(self):
        self.busy = True
        print(f"{type(self).__name__} is occupied with current movie")

    def available(self):
        self.busy = False
        print(f"{type(self).__name__} is free for movie")

    def status(self):
        return self.busy


class Agent:
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.status():
            self.actor.occupied()
        else:
            self.actor.available()


class Customer:
    def __init__(self):
        print("Customer: buy shirt")
        self.card = DebitCard()
        self.purchased = None

    def make_payment(self):
        self.purchased = self.card.do_pay()

    def __del__(self):
        if self.purchased:
            print("Customer: YAHOO!")
        else:
            print("Customer: DOOH!")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print(f"Bank: Has {self.__get_account()} enough funds?")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print("Bank: Enough funds")
            return True
        else:
            print("Bank: Not enough funds")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy: Card Number > ")
        self.bank.set_card(card)
        return self.bank.do_pay()


if __name__ == "__main__":
    a = Agent()
    a.work()

    c = Customer()
    c.make_payment()
