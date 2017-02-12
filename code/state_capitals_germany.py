capitals_dict = {
'Schleswig-Holstein': 'Kiel',
'Hamburg': 'Hamburg',
'Mecklenburg-Vorpommern': 'Schwerin',
'Brandenburg': 'Potsdam',
'Berlin': 'Berlin',
'Sachsen': 'Dresden',
'Bayern': 'München',
'Baden-Wuerttemberg': 'Stuttgart',
'Rheinland-Pfalz': 'Mainz',
'Saarland': 'Saarbruecken',
'Nordrhein-Westfalen': 'Duesseldorf',
'Niedersachsen': 'Hannover',
'Bremen': 'Bremen',
'Sachsen-Anhalt': 'Magdeburg',
'Thueringen': 'Erfurt',
'Hessen': 'Wiesbaden'
}

import random

states = list(capitals_dict.keys())
correct_answers = 0
wrong_answers = 0

while True:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = input("What is the capital of " + state + "? ")

    if capital_guess == 'quit':
        print("Bye human.")
        print("Stats:")
        print("Correct answers: " + str(correct_answers))
        print("Wrong answers: " + str(wrong_answers))
        break
    elif capital_guess == capital:
        print("Correct! Nice job.")
        correct_answers = correct_answers + 1
    else:
        print("Incorrect. The capital of " + state + " is " + capital + ".")
        wrong_answers = wrong_answers + 1

print("All done")
