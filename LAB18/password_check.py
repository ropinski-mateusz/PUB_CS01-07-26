def validate_password(password, minLength=12):

    #Inicjacja pustej listy
    problems = []

    #Sprawdzenie czy haslo nie puste
    if not password:
        problems.append("Haslo nie moze byc puste.")

    #Sprawdzenie czy haslo ma 12 znakow
    if len(password) < 12:
        problems.append("Haslo ma mniej niz 12 znakow.")

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
            isDigit = True
        elif char.isupper():
            isLowerCase = True
        elif char.isdigit():
            isUpperCase = True
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

    testScenarios = {
    "Puste haslo": "",
    "Za krotkie haslo": "admin",
    "Brak wielkiej litery": "password123!",
    "Brak cyfry": "PasswordTest!",
    "Brak znaku specjalnego": "Password1234",
    "Spacje na brzegach": " Password123! ",
    "Poprawne haslo": "VeryLongPassword123!"
    }


    print(problems)


#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")

validate_password(password, 12)