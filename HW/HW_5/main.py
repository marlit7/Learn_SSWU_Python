import module_2d
import module_cv
import module_fizzbuzz

if __name__ == "__main__":
    print('--------------------- звернення до module_2d---------------')
    module_2d.area_triangle()

    print('--------------------- звернення до module_cv---------------')
    module_cv.my_cv()

    print('--------------------- звернення до module_fizzbuzz---------------')
    n = int(input('число: '))
    module_fizzbuzz.fizzbuss(n)

