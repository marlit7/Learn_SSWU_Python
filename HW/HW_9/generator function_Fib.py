#generator function
def fibonacci_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


nterms = 10
if nterms <= 0:
    print("Будь-ласка, задайте позитивне ціле число")
else:
    print("Ряд чисел Фібоначчі через генераторну функцію:")
    for num in fibonacci_gen(nterms):
        print(num)