#iterator
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        if self.i == 0:
            self.i += 1
            return 0
        elif self.i == 1:
            self.i += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return self.b


nterms = 10
if nterms <= 0:
    print("Будь-ласка, задайте позитивне ціле число")
else:
    print("Ряд чисел Фібоначчі через ітератор:")
    for num in FibonacciIterator(nterms):
        print(num)