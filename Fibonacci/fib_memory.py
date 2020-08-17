#Base case
memory = {0: 0, 1: 1} 

def fib(num: int) -> int:
    if num not in memory:
        memory[num] = fib(num - 1) + fib(num - 2)
    return memory[num]

if __name__ == "__main__":
    print(fib(5))
    print(fib(50))