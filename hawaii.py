def validWord(word):
    validChar = "abcdefghijklmnopqrstuvwxyz' "
    
    for char in word:
        if char.lower() not in validChar:
            return False
    return True

def hawaii_pronunciation(word):
    pronunciation = ""
    i = 0
    while i < len(word):
        char = word[i].lower()

        if char in "aeiou":

            if i + 1 < len(word) and word[i:i + 2] in ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]:
                pronunciation += word[i:i + 2] + "-"
                i += 2
            elif i + 2 < len(word) and word[i:i + 3] in ["aia", "aie", "aio", "aiu", "eia", "eie", "eio", "eiu",
                                                         "oia", "oie", "oio", "oiu", "uia", "uie", "uio", "uiu"]:
                pronunciation += word[i:i + 3] + "-"
                i += 3
            else:
                pronunciation += vowelRules(char, i, word) + "-"
                i += 1
        else:
            pronunciation += char
            i += 1

    return pronunciation[:-1]  

def vowelRules(char, i, word):

    if char == 'a':
        return 'ah'
    elif char == 'e':
        return 'eh'
    elif char == 'i':
        return 'ee'
    elif char == 'o':
        return 'oh'
    elif char == 'u':
        return 'oo'
    elif char == 'w':

        if i == 0 or (i > 0 and word[i - 1].lower() in "ae"):
            return 'w'
        elif i > 0 and word[i - 1].lower() in "iou":
            return 'v'
    return char  

def main():
    while True:
        word = input("Enter a Hawaiian word: ")

        if validWord(word):
            pronunciation = hawaii_pronunciation(word)
            print(word.upper() + " is pronounced " + pronunciation.capitalize())
        else:
            print("Invalid characters detected. Please enter a valid Hawaiian word.")

        replay = input("Do you want to enter another Hawaiian word? (Y/N): ").lower()
        if replay not in ["y", "yes"]:
            break

if __name__ == "__main__":
    main()
