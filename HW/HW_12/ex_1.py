import random
import time

def random_int_list(n):
    return [random.randint(0, 1000) for _ in range(n)]


# Бульбашкове сортування
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":

    size = 1000
    data = random_int_list(size)

    start = time.time()
    sorted_data = bubble_sort(data)
    end = time.time()

    print("Розмір вибірки:", size)
    print("Час сортування:", end - start, "секунд")