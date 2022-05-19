import names

a = 0 
while True:

    input("druk op enter voor een andere naam.")
    for i in range(1):
        print(names.get_full_name(i))
        a +=1