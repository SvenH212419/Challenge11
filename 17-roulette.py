import random

print('-' * 50)
print('Welkom bij mijn casino')
print('-' * 50)


initial_balance_is_valid = False

while not initial_balance_is_valid:
    try:
        initial_balance = float(input('Hoeveel wil je inzetten?: '))
        if initial_balance > 0:
            initial_balance_is_valid = True
        else:
            print("Je kan niet 0 of een negatief nummer van geld invullen!")
    except ValueError:
        print('Vul een nummer in bijvoorbeeld 20 of 57.')

print('-' * 50)
print("Nice, laten we beginnen.")
print('-' * 50)

game_is_playing = True
gains = []

while game_is_playing:

    bet_is_valid = False

    while bet_is_valid is not True:
        try:
            bet = float(input('Hoeveel geld wil je inzetten op deze enkele roulette beurt?: '))
            if bet <= initial_balance + sum(gains) and bet > 0:
                bet_is_valid = True
            else:
                print("U kunt geen 0 inzetten, een negatief bedrag of geld dat u niet heeft! ")
        except ValueError:
            print('Asjeblieft vul een geldige nummer in.')

    guess_number_is_valid = False

    while not guess_number_is_valid :
        try:
            guess_number = float(input('Raad het nummer?: '))
            if 0 <= guess_number <= 49:
                guess_number_is_valid = True
            else:
                print("Je moet een getal tussen 0 en 49 invullen! ")
        except ValueError:
            print('Gelieve een geldig nummer invoeren: ')

    winning_number = random.randint(0, 49)

    if random.randint(0, 1) == 0:
        black_or_red = 'black'
    else:
        black_or_red = 'red'

    if guess_number == winning_number:
        gain = bet * 3
    elif black_or_red == 'black' and 0 <= guess_number <= 24:
        gain = bet * 0.5
    else:
        gain = -bet

    if gain > 0:
        print('Jij wint', gain)
        gains.append(gain)

    else:
        print('Jij verliest', -gain)
        gains.append(gain)

    balance_final = initial_balance + sum(gains)
    print('Je balans is nu', balance_final)

    if balance_final == 0:
        print('-' * 50)
        print('Sorry, maar geen geld in de pocket.')
        break

    replay_is_valid = False

    while not replay_is_valid :
        replay = input('Wil je opnieuw spelen type ja of nee: ')
        if replay == 'nee':
            game_is_playing = False
            print('-' * 50)
            print('Initial balance:', initial_balance)
            if gain <=0:
                print('Loss: ', -sum(gains))
            else:
                print('Gain: ', sum(gains))




            print('Balance:', balance_final)
            print('-' * 50)
            print('Tot de volgende keer.')
            break
        elif replay == 'ja' or replay == 'nee':
            replay_is_valid = True
        elif replay == 'ja':
            game_is_playing = True

        else:
            print('Asjeblieft type ja of nee.')