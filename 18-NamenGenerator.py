import names

while True:
    if input("Druk op enter voor een andere naam. (q to quit)") == "q":
        break
    print(names.get_full_name())