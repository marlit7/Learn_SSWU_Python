# open/closed
#
# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
#
#     def give_discount(self) -> float:
#         if self.customer == 'silver':
#             return self.price * 0.2
#         elif self.customer == 'gold':
#             return self.price * 0.3
#         elif self.customer == 'vip':
#             return self.price * 0.4

from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__(self, price: float):
        self.price = price

    @abstractmethod
    def give_discount(self) -> float:
        pass

class SilverDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.2

class GoldDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.3

class VipDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.4