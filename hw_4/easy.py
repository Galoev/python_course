from time import time
from threading import Thread
from multiprocessing import Process


def fib(n):
    a = 1
    b = 1
    for _ in range(2, n):
        b, a = b + a, b
    return b


def fib_repeat(n, num_repeat):
    start = time()

    for _ in range(num_repeat):
        fib(n)

    return time() - start


def run_workers(workers):
    start = time()

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    return time() - start

if __name__ == "__main__":
    num_repeat = 10
    n = 400_000
    with open("artifacts/easy.txt", "w") as file:
        file.write(f"seq: {fib_repeat(n, num_repeat)}\n")
        file.write(f"threading: {run_workers([Thread(target=fib, args=(n,)) for _ in range(num_repeat)])}\n")
        file.write(f"multiprocessing: {run_workers([Process(target=fib, args=(n,)) for _ in range(num_repeat)])}\n")