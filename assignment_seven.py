

def encode():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    phrase = input("What phrase would you like to encode?: ")

    phrase = phrase.lower()

    phrase = phrase.replace(" ", "")

    key = input("What key would you like to use?: ")

    key_count = 0

    code = ""

    for x in phrase:
        thing = alphabet.index(x) + alphabet.index(key[key_count % len(key)])
        if thing >= 26:
            code = code + alphabet[thing % 26]
        else:
            code = code + alphabet[thing]
        key_count = key_count + 1

    print("Your code is: ", code)


def decode():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    code = input("What code would you like to decode?: ")

    key = input("What is the key?: ")

    key_count = 0

    phrase = ""

    for x in code:
        thing = alphabet.index(x) - alphabet.index(key[key_count % len(key)])
        if thing < 0:
            phrase = phrase + alphabet[thing + 26]
        else:
            phrase = phrase + alphabet[thing]
        key_count = key_count + 1

    print("Your phrase is: ", phrase)


def main():
    while True:
        print(" ")
        edq = input("Encode, decode or quit? (E/D/Q): ")
        if edq == "E" or edq == "e":
            encode()
        elif edq == "D" or edq == "d":
            decode()
        elif edq == "Q" or edq == "q":
            print("Good bye!")
            break
        else:
            print("Please enter a valid answer.")


main()
