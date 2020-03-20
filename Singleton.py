class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.instance


# Monostate
class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        state = super(Monostate, cls).__new__(cls, *args, **kwargs)
        state.__dict__ = cls.__shared_state

        return state

    def state(self):
        return id(self.__shared_state)


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    # Singleton
    s = Singleton()
    s1 = Singleton()
    print(f"{s} | {s1}")

    # Monostate
    b = Monostate()
    b1 = Monostate()
    print(f"{b} | {b1}")
    print(f"{b.state()} | {b1.state()}")

    # Meta
    l = Logger()
    l1 = Logger()
    print(l, l1)
