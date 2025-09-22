from unidecode import unidecode

#### Fonction secondaire


def ispalindrome(p):
    """
    Fonction permettant de vérifier si un mot ou une phrase est un palyndrome.
    p doit être une chaîne de character.
    """
    p = unidecode(p.lower())
    p = [i for i in p if i not in {" ",":", ";", "!", "?", ",", ".","'","-"}]
    for i in range(len(p)):
        if p == p[::-1]:
            return True
    return False

#### Fonction principale


def main():

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
