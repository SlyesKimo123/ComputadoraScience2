try:
    file = open("RandomTextFileofRandomness", "r")
    def return_me(text):
        string = str(text.readlines())
        return string

    def encrypt_6(message):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        newsent = []
        for letter in message:
            if letter in alphabet:
                letter = alphabet.index(letter) + 6
                letter = alphabet[letter:letter+1]
                newsent.append(letter)
            else:
                newsent.append(letter)
        string = ("".join(newsent))
        return string

    def writeStr(string, file):
        file.write(string)

    def flip(text):
        words = text.split()
        final = []
        for word in words:
            new = []
            for letter in word:
                new.append(letter)
            new.reverse()
            new = "".join(new)
            final.append(new)
        string = " ".join(final)
        return string
    try:
        def main():
            string = return_me(file)
            print(type(string))
            string = encrypt_6(string)
            print(type(string))
            string = flip(string)
            print(type(string))
            writeTo = open("CSII_Warmup_File", "w")
            writeStr(string, writeTo)
        main()
    finally:
        file.close()
except IOError:
    print("This file cannot be found.  ¡Sorry ya bastard!")
