
# Alright lets make a pizza!
import random

from __future__ import print_function

def getCheese():
    return 'A bit of Mozzarella cheese'

def getSauce():
    return 'some basic Marinara sauce'
def getMushrooms():
    return '%d mushroom slices' % random.randrange(3,10)
    
def getIngredients():
    return [
        getCheese(),
        getSauce(),
        getMushrooms()
    ]

def printPizza():
    ingredients = getIngredients()
    print("Here is our pizza! It has %d ingredient(s)" % (len(ingredients)))
    print("\n".join(
        [str(num + 1) + ': ' + i for (num, i) in enumerate(ingredients)]
    ))

print('''
 ____  __  ____  ____   __     ____  __  _  _  ____
(  _ \(  )(__  )(__  ) / _\   (_  _)(  )( \/ )(  __)
 ) __/ )(  / _/  / _/ /    \    )(   )( / \/ \ ) _)
(__)  (__)(____)(____)\_/\_/   (__) (__)\_)(_/(____)
''')

printPizza()

print('''
 __  __           __
 \ \/ /_ ____ _  / /
  \  / // /  ' \/_/
  /_/\_,_/_/_/_(_)
''')
