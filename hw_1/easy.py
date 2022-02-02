def fibonacci(n: int) -> list:
    if n <= 0:
        return [0]

    a = 0
    b = 1
    res =[0, 1]

    for i in range(2, n + 1):
        tmp = b
        b += a
        a = tmp
        res.append(b)
    
    return res

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))