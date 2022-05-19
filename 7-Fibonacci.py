def fib(n):
    a, b = 0, 1
    list = [0,1]

    if n == 0:
        return[0]
    elif n == 1:
        return [0, 1]
    else:
        for i in range(n-1):
            a, b = b, a + b
            list.append(b)
        return list

print(fib(int(input("Fib van: "))))