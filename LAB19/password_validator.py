class PasswordValidator:
    def __init__(
        self,
        minLength=12,
        requireLowercase=True,
        requireUppercase=True,
        requireDigit=True,
        requireSpecial=True,
        specialCharacters="!@#$%^&*"
    ):

        if minLength < 1:
            raise ValueError("Minimalna dlugosc hasla nie moze byc mniejsza niz 1.")

        self.minLength = minLength
        self.requireLowercase = requireLowercase
        self.requireUppercase = requireUppercase
        self.requireDigit = requireDigit
        self.requireSpecial = requireSpecial
        self.specialCharacters = set(specialCharacters)

    def validate_password(self, password):

        #Inicjacja pustej listy
        problems = []

        #Sprawdzenie czy haslo nie puste
        if not password:
            problems.append("Haslo nie moze byc puste.")
            return False, problems

        #Sprawdzenie czy haslo ma mniej znakow niz minLength
        if len(password) < self.minLength:
            problems.append(f"Haslo ma mniej niz {self.minLength} znakow.")

        # Sprawdzenie spacji na brzegach
        if password.startswith(" ") or password.endswith(" "):
            problems.append("Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu")

        #Inicjalizacja zmiennych logicznych
        isDigit = False
        isLowerCase = False
        isUpperCase = False
        isSpecialCharacter = False


        #Sprawdzenie znakow w hasle
        for char in password:
            if char.islower():
                isLowerCase = True
            elif char.isupper():
                isUpperCase  = True
            elif char.isdigit():
                isDigit = True
            elif char in self.specialCharacters:
                isSpecialCharacter = True

        #dodawanie komunikatow do listy
        if self.requireDigit and not isDigit:
            problems.append("Brak cyfry")
        if self.requireLowercase and not isLowerCase:
            problems.append("Brak malej litery")
        if self.requireUppercase and not isUpperCase:
            problems.append("Brak duzej litery")
        if self.requireSpecial and not isSpecialCharacter:
            problems.append("Brak znaku specjalnego `!@#$%^&*`")

        isValid = len(problems) == 0
        return isValid, problems

    def __repr__(self):
        # Bezpieczna reprezentacja 
        return (
            f"PasswordValidator(minLength={self.minLength}, "
            f"requireLowercase={self.requireLowercase}, "
            f"requireUppercase={self.requireUppercase}, "
            f"requireDigit={self.requireDigit}, "
            f"requireSpecial={self.requireSpecial})"
        )


if __name__ == "__main__":
    # Kod pod tym warunkiem wykona sie TYLKO przy bezposrednim uruchomieniu pliku,
    # nie uruchomi sie, gdy plik bedzie importowany przez inny modul (spelnienie kryterium).
    validator = PasswordValidator()
    print("Domyslny walidator:", validator)
    
    test_pass = "VeryLongPassword123!"
    valid, errors = validator.validate_password(test_pass)
    print(f"Wynik dla hasla testowego: valid={valid}, errors={errors}")