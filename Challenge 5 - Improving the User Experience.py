"""https://www.askpython.com/python/python-import-statement"""

"""https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Step%205#R7VtdW6M4FP41ffZqfcpn62XrOOqszjrq6nq1TywpMALphrS28%2Bs3gYSPBBUtFLR7VXJIgJw35z0fSQfGUbg%2BwWDhXSAHBgN96KwHxpeBrmtDbUh%2FmGSTSiz7MBW42Hd4p1xw7f%2BCYiSXLn0HxqWOBKGA%2BIuycIaiCM5ISQYwRk%2FlbnMUlN%2B6AC5UBNczEKjSO98hXiod66Ncfgp91xNv1sT8QiA685nEHnDQU0FkHA%2BMI4wQSa%2FC9REMmPKEXu7ONnfB%2BaN98u1H%2FC%2F4a%2FrHzffb39OHfX3LkGwKGEbk3Y%2BGehTa4Ofq8ZKsVtduPNXWG%2FHoFQiWXF98rmQjFAgdqk%2FeRJh4yEURCI5z6RSjZeRA9pohbeV9zhFaUKFGhT8hIRu%2BOMCSICrySBjwuzXnxz82Rks8gy%2F0M%2FgyA9iF5IXJc1zZBAtrhWvvBKIQEryhHTAMAPFX5QUF%2BLp0s3657ukFV%2F8bUDYUKK5vJlc3Ch65tpnqnjyfwOsFSBTyRE24rNk5ighXu0anNnUDEMccqJhg9JgZBeudrfDhm0FZQUzg%2BkU1irs21zsnFIM3n3Lr1ITJeQXLNIfbK75yGaiK%2F1g28NLaftUG9K5soJqO9hoLrTMwfujfkHexml4g78dkeTY2rm7X2fR2qnq49snfbPiBxVv3hTtf1vzJSWMjGhGdbmEQa94X7%2BXDkpYYV6ntdnGvVPRwS5T50Evk08%2FOeDaLWzjPaiOJQNPv4qOktZJ9xvtteaiY8gmMIAYEsm9g8wORg0LG%2FAg7LLTDScsDkRuC6B8mjQ8Wm84c4NwPgiMUIJy81nAAHM9n2bDCHXs2hg%2FzHbpMTevaZwqqegbdOImfIzaFhwBEj7EQBtT4IWZXfpQh%2F9kCHKuMVoZCES1zl2hZvfCq29F0Y6ys1%2FTGdtPOuB5Nm0ZrNF3pfIyP4uXb9tb6TuA17N16YZWnJ%2FEjW%2F4eI%2BplDHFSkEkKNTCOuWtOafrzMbOcenbuR8f%2FM7PCuK8y82E3zGxZ9Ux3gjHYFLotWIf4%2BfdosgewhtK6Sp%2FYKC9o4y55Xyuwfu4D2sjudr44tVHTq3MrgrEVgjmLM%2FpPKB%2By3Gug2wGd1fSBkr7tsivhAtJAPe2fhOvGV9UveCh8WMav%2B4TWiF0Kuc0qYq8KucdtEbtufZS4qif2dVjTvnSzV%2FZ1qNjXFVwEbP0Lo0kS4GQp0pUohE0EWG0ZkxQkWXWDJDlxaa7YoOav9zBWlEenR8oaKldqIhRBqazDRSDw3Yg2Z1STFBVjypTlz0Aw4TdC33ESC62CpGy1baEylhjOVlGpIji9NYLbk%2FJwYwQnAoPXGa6zfcnKAoG9Hzi3V1ioAr5S02aXjkx8ZYFkz1EsavWBP08uIxYsLnCav%2FBK%2FUAp3QNMti%2Fc96b6LjtE87CmQ5TzxeawUqOO72jP%2FKEhZ82dO8QPU0ntiUMUSLzuEPVehfxGNzW6bUonWgnmHPW%2BAd0rnMVnF1j2FKx4Ypd8xjKqLJ2gJfOOaJ74zRU7%2FNjDkokulUzs7ksm6l7FyeTimEr%2BvD2%2B2i6aaEuL8o7CqGqvd6c7Cnqnhd23b%2Bg1xzKNF4bqbQuMZChb3tEzuk283%2BN%2BskY37sf8mO7HVOhwgpMkLBmb1BFtEDKiix7iRaI32RNlh29YkA%2F7WbuXy42jmgzanh9Ss6v9KzfKm5J21%2BmVoUZj%2B4eKXAUeDbtGRT2wvX%2BViHHfTEX1HHsHiilhou8Ok%2BfPeJcgueRV1NOsihrQmGzQq2Kqou%2B6UNVOmLRxTXffxO5iJTJq1nkD8whLHJHz5zzv%2F22VxmAYAofNKz9DQTzA8Gzk7Fx%2F8DKtEl5GBbllpy92gpdKblV4lbfZRcVm5qVbGj6LiSPE4JKOtxx8FuBkBrSqgLOrgLPeDBxt5n%2BDTfPc%2FM%2FExvF%2F"""


#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
    
    
    
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

                                         
                             
                             
