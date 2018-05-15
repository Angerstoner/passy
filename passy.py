import random
rand = random.SystemRandom()

words = {}
with open("wordlist.txt") as file:
    for line in file:
       (key, val) = line.split()
       words[key] = val

def generatePhrase(count=4):
    phrase = ""
    for roll in range(count):
        dice = ""
        for i in range(5):
            dice += str(rand.randrange(1,7))
        phrase += words[dice] + " "
    print(phrase)

generatePhrase();
