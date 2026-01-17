#generator expression
nterms = 10

if nterms <= 0:
    print("Будь-ласка, задайте позитивне ціле число")
else:
    print("Ряд чисел Фібоначчі через генераторний вираз:")

    fib_seq = [0, 1]
    gen_expr = (fib_seq.append(fib_seq[-1] + fib_seq[-2]) or fib_seq[-1] for _ in range(2, nterms))

    print(fib_seq[0])
    print(fib_seq[1])

    for num in gen_expr:
        print(num)