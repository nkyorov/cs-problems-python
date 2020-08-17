class Stack:
    def __init__(self):
        self._container = []
    
    def push(self, item):
        self._container.append(item)
    
    def pop(self):
        return self._container.pop()
    
    def __repr__(self):
        return repr(self._container)

def hanoi_solver(start, end, temp, disks):
    if disks == 1:
        end.push(start.pop())
    else:
        hanoi_solver(start = start, end = temp, temp = end, disks = disks - 1)
        hanoi_solver(start = start, end = end, temp = temp, disks = 1)
        hanoi_solver(start = temp, end = end, temp = start, disks = disks - 1)

if __name__ == "__main__":
    num_discs = 5
    tower_a, tower_b, tower_c = Stack(), Stack(), Stack()

    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi_solver(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)