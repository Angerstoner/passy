import random
rand = random.SystemRandom()

SUBSTITUTIONS = {
        'a' : '@',
        'e' : '3',
        'i' : '!',
        'o' : '0',
        's' : '$',
        }

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
    return phrase

def substitute(prase, count=4):
    subPhrase = ""
    subsPerWord = 0
    for c in phrase:
        if c.lower() in SUBSTITUTIONS and subsPerWord < 2:
            subPhrase += SUBSTITUTIONS[c.lower()]
            subsPerWord += 1
        elif c == ' ':
            subPhrase += c
            subsPerWord = 0
        else:
            subPhrase += c
    return subPhrase

count = 4;
phrase = generatePhrase(count)
subPhrase = substitute(phrase, count)
print(subPhrase);
