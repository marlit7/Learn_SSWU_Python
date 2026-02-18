from collections import deque

def create_stack():
    return deque()

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def hanoi(n, source, helper, target):
    if n == 1:
        disk = pop(source)
        push(target, disk)
        print("Перемістити диск", disk)
    else:
        hanoi(n - 1, source, target, helper)
        hanoi(1, source, helper, target)
        hanoi(n - 1, helper, source, target)


n = 3

A = create_stack()
B = create_stack()
C = create_stack()

for i in range(n, 0, -1):
    push(A, i)

print("Ходи:")
hanoi(n, A, B, C)

print("Результат:")
print("A:", list(A))
print("B:", list(B))
print("C:", list(C))