def validate_password(password, minLength):

    #Inicjacja pustej listy
    problems = []

    #Sprawdzenie czy haslo nie puste
    if not password:
        problems.append("Haslo nie moze byc puste.")

    #Sprawdzenie czy haslo ma mniej znakow niz minLength
    if len(password) < minLength:
        problems.append(f"Haslo ma mniej niz {minLength} znakow.")

    # Sprawdzenie spacji na brzegach
    if password.startswith(" ") or password.endswith(" "):
        problems.append("Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu")

    #Inicjalizacja zmiennych logicznych
    isDigit = False
    isLowerCase = False
    isUpperCase = False
    isSpecialCharacter = False

    specialCharacters = set("!@#$%^&*")


    #Sprawdzenie znakow w hasle
    for char in password:
        if char.islower():
            isLowerCase = True
        elif char.isupper():
            isUpperCase  = True
        elif char.isdigit():
            isDigit = True
        elif char in specialCharacters:
            isSpecialCharacter = True

    #dodawanie komunikatow do listy
    if not isDigit:
        problems.append("Brak cyfry")
    if not isLowerCase:
        problems.append("Brak malej litery")
    if not isUpperCase:
        problems.append("Brak duzej litery")
    if not isSpecialCharacter:
        problems.append("Brak znaku specjalnego `!@#$%^&*`")

    print(problems)

def test():
    testScenarios = {
    "Puste haslo": "",
    "Za krotkie haslo": "admin",
    "Brak wielkiej litery": "password123!",
    "Brak cyfry": "Passwordtest!",
    "Brak znaku specjalnego": "Password1234",
    "Spacje na koncach": " Password123! ",
    "Poprawne haslo": "VeryLongPassword123!"
    }
    for nazwaTestu, haslo in testScenarios.items():
        validate_password(haslo, 12)
        print("Wynik dla: ", nazwaTestu)

    

def main():
    #test()

    minLengthInput = input("Podaj minimalna dlugosc hasla: (domyslnie 12 znakow): ")
    if minLengthInput.strip() == "":
        minLength = 12
    else:
        try:
            minLength = int(minLengthInput)
        except ValueError:
            print("Niepoprawna wartosc, podaj liczbe calkowita nastepnym razem: ")
            return
        

    #Zaczytanie hasla z klawiatury
    password = input("Podaj haslo do sprawdzenia: ")
    validate_password(password, minLength)

if __name__ == "__main__":
    main()