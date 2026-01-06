# Dependency Inversion
#
# class Reporter:
#
#     @staticmethod
#     def publish(news: str) -> None:
#         print(NewsPaper().publish(news=news))
#
# class NewsPaper:
#
#     @staticmethod
#     def publish(news: str) -> None:
#         print(f"{news} published today")
#
# reporter = Reporter()
# print(reporter.publish("News Paper"))

from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def publish(self, news: str) -> None:
        pass

class NewsPaper(Publisher):
    def publish(self, news: str) -> None:
        print(f"{news} published today")

class Reporter:
    def __init__(self, publisher: Publisher):
        self.publisher = publisher

    def publish(self, news: str) -> None:
        self.publisher.publish(news)


publisher = NewsPaper()
reporter = Reporter(publisher)
reporter.publish("News Paper")