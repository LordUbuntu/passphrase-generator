# Jacobus Burger <therealjacoburger@gmail.com>
# 2021-04-10
from random import choice

# generate a list of words from the dictionary
words = [
    word
    for line in open("./dictionary", "r").readlines()
    for word in line.lower().strip("\n").split()
]


def passphrase(length):
    # select $length random words, avoiding repetitions
    phrase = []
    while len(phrase) < length:
        word = choice(words)
        if word not in phrase:
            phrase.append(word)

    # return the phrase as a space-delimited string
    return " ".join(phrase)


def main():
    # get user input, ensuring it's valid
    try:
        phrases = int(input("how many passphrases should be generated (>0)? "))
        length = int(input("how many words in each passphrase (>4)? "))
    except ValueError:
        phrases = 1
        length = 5
    phrases = phrases if phrases > 0 else 1
    length = length if length > 4 else 5

    # generate and display passphrases
    output = "\n\n"
    for _ in range(phrases):
        phrase = passphrase(length)
        output += phrase + "\n"
    print(output)


if __name__ == "__main__":
    main()
