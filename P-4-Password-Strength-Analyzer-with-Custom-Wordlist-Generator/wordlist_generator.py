import itertools

def generate_wordlist(name, pet, birth_year):

    base_words = [name, pet, birth_year]

    leets = {
        "a":"4",
        "e":"3",
        "i":"1",
        "o":"0",
        "s":"5"
    }

    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())

        for k,v in leets.items():
            wordlist.add(word.replace(k,v))

    combos = itertools.permutations(base_words,2)

    for combo in combos:
        wordlist.add("".join(combo))
        wordlist.add("".join(combo)+"123")
        wordlist.add("".join(combo)+"2024")

    return wordlist
