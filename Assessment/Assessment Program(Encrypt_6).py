# Luke Chase
# Encrypt_6()

def encrypt(final, dict):
    dict = {}
    dict["a"] = "u"
    dict["b"] = "v"
    dict["c"] = "w"
    dict["d"] = "x"
    dict["e"] = "y"
    dict["f"] = "z"
    dict["g"] = "a"
    dict["h"] = "b"
    dict["i"] = "c"
    dict["j"] = "d"
    dict["k"] = "e"
    dict["l"] = "f"
    dict["m"] = "g"
    dict["n"] = "h"
    dict["o"] = "i"
    dict["p"] = "j"
    dict["q"] = "k"
    dict["r"] = "l"
    dict["s"] = "m"
    dict["t"] = "n"
    dict["u"] = "o"
    dict["v"] = "p"
    dict["w"] = "q"
    dict["x"] = "r"
    dict["y"] = "s"
    dict["z"] = "t"

    list_user_input = []
    for letter in final:
        if letter in dict:
            list_user_input.append(dict[letter])
        else:
            list_user_input.append(letter)
    print(" ".join(list_user_input))

final = str(input("Write a random string here and I will encrypt it for you (no caps pls)\n "))
encrypt(final, dict)

# This is pretty much the same thing as the Pirate program we made
