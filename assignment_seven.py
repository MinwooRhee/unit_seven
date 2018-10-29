
alphabet = "abcdefghijklmnopqrstuvwxyz"

phrase = input("What phrase would you like to encode?: ")

phrase = phrase.lower()

phrase = phrase.replace(" ", "")

print(phrase)

key = input("What key would you like to use?: ")

key_count = 0

code = ""

for x in phrase:
    thing = alphabet.index(x) + alphabet.index(key[key_count % len(key)])
    print(thing)
    if thing >= 26:
        code = code + alphabet[thing % 26]
    else:
        code = code + alphabet[thing]
    key_count = key_count + 1

print(code)
