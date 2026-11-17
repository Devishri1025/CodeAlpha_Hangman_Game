import random
words = ['APPLE','TIGER','PYTHON','CASTLE','GUITER']
categoris = ['Fruit','Animal','Technology','Place','Music']
hint = [ "A fruit that keeps the doctor away",
          "The national animal of India",
          "A popular programming language",
          "A home where kings and queens live",
          "A musical instrument with strings"]


index = random.randint(0,4)

word = words[index]
category = categoris[index]
hint = hint[index]

guessed_letters = []
attempts = 6
hint_count = 1

print('======HANGMAN=====\n')
print('type "hint" for hint')
print('Category:'+category)

while attempts > 0:
    display =""
    
    for letter in word:
        if letter in guessed_letters:
            display += letter +" "
        else:
            display += "_ "

    print('\n'+ display)
    print()

    guess = input('Guess a letter: ').upper()

    if guess == 'HINT':
        if hint_count >0:
            print('hint:',hint)
            hint_count -=1
        else:
            print('no hints left')
            continue
    if len(guess)!=1 or not guess.isalpha():
        if guess=='HINT':
            continue
        else:
            print('please enter a single letter')
            continue
    if guess in guessed_letters:
        print('Woops! you already guessed it, try another letter')
        continue

    
    guessed_letters.append(guess)

    if guess in word:
        print('Correct!\U0001F973' )
    else:
        print('Wrong \u274C')
        attempts -=1


    if all(letter in guessed_letters for letter in word):
         print('\U0001F973 Congratulations! you won')
         break
    

    print(f'\U0001F4A1{hint_count}')
    for i in range(6):
        if i<attempts:
            print('\u2764\ufe0f',end='')
        else:
            print('\u2661',end='')

    print()        
    print('============')




if attempts ==0:
    print('you lost!')
    print('correct word was: ',word)
    

















    
