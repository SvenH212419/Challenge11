import random
red   = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
black = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
  
while True:
    if input("Druk op Enter om door te gaan of 'q' om te stoppen: ") == 'q':
        break
    number = random.randrange(0, 37)
    print('\nNummer is: ', number)
  
    if 1 <= number <= 17:
        print('Nummer is klein')
    else:
        print('Nummer is groot')
    if number in red:
        print('Nummer is rood')
    else:
        print('nummer is zwart')
    if number % 2 == 0: 
        print('Nummer is even ')
    else: 
        print('Nummer is oneven')