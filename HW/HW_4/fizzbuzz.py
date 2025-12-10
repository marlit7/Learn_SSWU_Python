
# --------------------------- Homework_4  ------------------------------------

def fizzbuss(n: int) -> None:

    '''
    Виводить числа від 1 до n згідно з правилами FizzBuzz.

    Правила:
    - Якщо число кратне 3 і 5 — вивести "FizzBuzz".
    - Якщо число кратне лише 5 — вивести "Buzz".
    - Якщо число кратне лише 3 — вивести "Fizz".
    - В інших випадках вивести саме число.

    :param n: межа діапазону (включно), повинна бути додатним числом

    :return: None
    '''

    for i in range(1,n+1):

        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)

if __name__ == "__main__":
    n = int(input('число: '))
    fizzbuss(n)
