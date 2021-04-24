def fibonacci(count):
    cur = 1
    new = 1
    for i in range(count):
        yield cur
        tmp = cur + new
        cur = new
        new = tmp

def solve(n: int = 10):
    print("First " + str(n) + " Fibonacci numbers:")
    print([i for i in fibonacci(n)])

#solve()