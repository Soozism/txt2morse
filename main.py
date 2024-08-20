txt = input("pleas inport your text :")
txt.lower()
morse_code = ""
for letter in txt:
    match letter:
        case "a":
            morse_code += ".-"
        case "b":
            morse_code += "-..."
        case "c":
            morse_code += "-.-."
        case "d":
            morse_code += "-.."
        case "e":
            morse_code += "."
        case "f":
            morse_code += "..-."
        case "g":
            morse_code += "--."
        case "h":
            morse_code += "...."
        case "i":
            morse_code += ".."
        case "j":
            morse_code += ".---"
        case "k":
            morse_code += "-.-"
        case "l":
            morse_code += ".-.."
        case "m":
            morse_code += "--"
        case "n":
            morse_code += "-."
        case "o":
            morse_code += "---"
        case "p":
            morse_code += ".--."
        case "q":
            morse_code += "--.-"
        case "r":
            morse_code += ".-."
        case "s":
            morse_code += "..."
        case "t":
            morse_code += "-"
        case "u":
            morse_code += "..-"
        case "v":
            morse_code += "...-"
        case "x":
            morse_code += "-..-"
        case "y":
            morse_code += "-.--"
        case "z":
            morse_code += "--.."
        case "1":
            morse_code += ".----"
        case "2":
            morse_code += "..---"
        case "3":
            morse_code += "...--"
        case "4":
            morse_code += "....-"
        case "5":
            morse_code += "....."
        case "6":
            morse_code += "-...."
        case "7":
            morse_code += "--..."
        case "8":
            morse_code += "---.."
        case "9":
            morse_code += "----."
        case "0":
            morse_code += "----"
        case " ":
            morse_code += "/  "
        case "":
            morse_code += ""
        case _:
            pass

    morse_code += " "

print(morse_code)