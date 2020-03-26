from abc import ABCMeta, abstractmethod


class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f"{type(self).__name__} got {args} from {subject}")


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f"{type(self).__name__} got {args} from {subject}")


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(subscriber).__name__ for subscriber in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return self.__latest_news


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f"{type(self).__name__} {self.publisher.get_news()}")


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f"{type(self).__name__} {self.publisher.get_news()}")


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f"{type(self).__name__} {self.publisher.get_news()}")


if __name__ == "__main__":
    s = Subject()
    o1 = Observer1(s)
    o2 = Observer2(s)
    s.notify_all("ALERT!")

    news_publisher = NewsPublisher()

    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(news_publisher)
    print(f"Subscribers: {news_publisher.subscribers()}")

    news_publisher.add_news("Hello World!")
    news_publisher.notify_subscribers()

    print(f"Detached: {type(news_publisher.detach()).__name__}")
    print(f"Subscribers: {news_publisher.subscribers()}")

    news_publisher.add_news("My second news!")
    news_publisher.notify_subscribers()
