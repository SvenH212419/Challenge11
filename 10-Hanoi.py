def hanoi(n, start, help, end):

    if n == 1:
        print(f"Move {start} to {end}.")
        return

    hanoi(n-1, start, end, help)
    print(f"Move {start} to {end}.")
    hanoi(n-1, help, start, end)

while True:
    n = int(input("Hanoi? 0 to quit. "))
    if n == 0:
        break
    hanoi(n, 'a', 'b', 'c')