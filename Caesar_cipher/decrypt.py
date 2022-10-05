with open("words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words


alphabet = "abcdefghijklmnopqrstuvwxyz"

def break_cipher(text):

    text = text.lower()

    for i in range(1, 26):
        output = " "

        for letter in text:

            if letter == " ":
                output += " "
                continue

            output += alphabet[ (alphabet.index(letter) + i) % 26 ]

        output = output.split()

        if is_english_word(output[0]) and is_english_word(output[-1]):
            return ' '.join(output)


