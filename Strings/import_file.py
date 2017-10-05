file = open("guido_vonRossum_speech.txt", "r")
data = file.read()

def remove_letter(theLetter, theString):
    new = theString.replace(theLetter, "")
    print(new)
    return new


remove_letter("a", data)
