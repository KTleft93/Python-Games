SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def letterScore(letter):
    if (letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']):

        return 1

    elif (letter in ['b', 'c', 'm', 'p']):

        return 3

    elif (letter in ['d', 'g']):

        return 2

    elif (letter in ['f', 'h', 'v', 'w', 'y']):

        return 4

    elif (letter in ['j', 'x']):

        return 8

    elif (letter in ['k']):

        return 5

    elif (letter in ['q', 'z']):

        return 10

    else:

        return 0


def wordScore(word):
    for b in word:
        c = SCORES[b]
        letter_values = map(lambda letter: SCORES[letter], word)
        word_value = sum(letter_values)
    return word_value

word = input("Please Enter a word:").lower()
print(wordScore(word))
