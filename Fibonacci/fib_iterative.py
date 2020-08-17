def fib(num: int) -> int:
    if num == 0: return num
    last = 0
    next = 1

    for _ in range(1, num):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib(5))
    print(fib(50))