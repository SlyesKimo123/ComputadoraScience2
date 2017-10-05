# Luke Chase
# Updated Alice_Words program --- Assessment Program
# Computer Science II
# October 1, 2017
try:
    file =  open("Alice's_Adventures_In_Wonderland_via_Gutenberg.txt", "r")
    file = file.read()
    def sort(text):
        dictionary = {}
        alphabetical_dictionary = {}
        word = ""
        for aline in text:
            letter = aline
            if letter!= " ":
                word = word + letter
            else:
                dictionary[word] = text.count(word)
                word = ""
        key_list = list(dictionary.keys())
        key_list = sorted(dictionary)
        begin = key_list.index("A")
        for i in key_list[begin:]:
            alphabetical_dictionary[i] = text.count(i)
        return alphabetical_dictionary

    dictionary = print(sort(file))

    try:
        text_thing = open("GET_WRITTEN_ON_YA_ALICE", "w")
        try:
            text_thing.write(str(dictionary))
        finally:
            text_thing.close()
    finally:
        text_thing.close()
except IOError:
    print("This file is not found.")
