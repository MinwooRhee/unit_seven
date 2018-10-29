
alphabet = "abcdefghijklmnopqrstuvwxyz"

phrase = "Python is fun"

phrase = phrase.lower()

phrase = phrase.replace(" ", "")

print(phrase)

key = "apple"

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
