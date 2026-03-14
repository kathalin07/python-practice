scecret_number = 7
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == scecret_number:
        print('YOU WON!')
        break
    else:
        print('INCORRECT!\nTRY AGAIN')
else:
    print('SORRY,YOU FAILED')    