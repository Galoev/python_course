def fibonacci(n: int) -> list:
    if n <= 0:
        return [0]
    res =[0, 1]

    for i in range(2, n + 1):
        res.append(res[-1] + res[-2])
    
    return res

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))