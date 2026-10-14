┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python --version 
Python 3.14.7

## 1. REPL i pierwsze instrukcje
KOD:
name = 'LearnIT'
print(name)
len = len(name)
print(len)
name = name.upper()
print(name)
if 'L' in name:
    print("Zawiera L")
else:
    print("Nie Zawiera L")

Terminal:
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python LAB18.py 
LearnIT
7
LEARNIT
Zawiera L

## 1A.
KOD:
name = 'LearnIT'
print(name)
len = len(name)
print(len)
name = name.upper()
print(name)

litera = input("Podaj Litere do wyszukania: ")
if litera in name:
    print("Zawiera litere", litera)
else:
    print("Nie Zawiera litery", litera)

Terminal:

┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python LAB18.py
LearnIT
7
LEARNIT
Podaj Litere do wyszukania: R
Zawiera litere R

┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python LAB18.py
LearnIT
7
LEARNIT
Podaj Litere do wyszukania: z
Nie Zawiera litery z
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python LAB18.py
LearnIT
7
LEARNIT
Podaj Litere do wyszukania: l
Nie Zawiera litery l

## 2. Pierwszy plik skryptu
password = input("Podaj haslo do sprawdzenia: ")
passwordLen = len(password)
print(passwordLen)

if passwordLen <=11:
    print("Haslo jest za krotkie")

Terminal: 
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: admin
5
Haslo jest za krotkie
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: VeryLongPassword
16

## 3. Lista problemów
#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")
#Inicjacja listy
problems = []

if not password:
    problems.append("Haslo nie moze byc puste.")

if len(password) < 12:
    problems.append("Haslo ma mniej niz 12 znakow.")

print(problems)

Terminal:
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: admin
['Haslo ma mniej niz 12 znakow.']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: 
['Haslo nie moze byc puste.', 'Haslo ma mniej niz 12 znakow.']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: VeryLongPassword
[]

## 4. Mała litera, wielka litera i cyfra
#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")
#Inicjacja pustej listy
problems = []

#Sprawdzenie czy haslo nie puste
if not password:
    problems.append("Haslo nie moze byc puste.")

#Sprawdzenie czy haslo ma 12 znakow
if len(password) < 12:
    problems.append("Haslo ma mniej niz 12 znakow.")

#Inicjalizacja zmiennych logicznych
isDigit = False
isLowerCase = False
isUpperCase = False

#Sprawdzenie znakow w hasle
for char in password:
    if char.islower():
        isDigit = True
    elif char.isupper():
        isLowerCase = True
    elif char.isdigit():
        isUpperCase = True

#dodawanie komunikatow do listy
if not isDigit:
    problems.append("Brak cyfry")
if not isLowerCase:
    problems.append("Brak malej litery")
if not isUpperCase:
    problems.append("Brak duzej litery")

print(problems)

Terminal:
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: ___
['Haslo ma mniej niz 12 znakow.', 'Brak cyfry', 'Brak malej litery', 'Brak duzej litery']

## 5. Znak specjalny i set
#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")
#Inicjacja pustej listy
problems = []

#Sprawdzenie czy haslo nie puste
if not password:
    problems.append("Haslo nie moze byc puste.")

#Sprawdzenie czy haslo ma 12 znakow
if len(password) < 12:
    problems.append("Haslo ma mniej niz 12 znakow.")

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

print(problems)

Terminal:
──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: ___
['Haslo ma mniej niz 12 znakow.', 'Brak cyfry', 'Brak malej litery', 'Brak duzej litery', 'Brak znaku specjalnego `!@#$%^&*`']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: Password123                                                         
['Haslo ma mniej niz 12 znakow.', 'Brak znaku specjalnego `!@#$%^&*`']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: Password123!
[]
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: Password123?
['Brak znaku specjalnego `!@#$%^&*`']

## 6. Spacje na początku lub końcu
#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")
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

print(problems)

Terminal:

└─$ python password_check.py
Podaj haslo do sprawdzenia:  ___ 
['Haslo ma mniej niz 12 znakow.', 'Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu', 'Brak cyfry', 'Brak malej litery', 'Brak duzej litery', 'Brak znaku specjalnego `!@#$%^&*`']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py 
Podaj haslo do sprawdzenia:  Password123!
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: Password123! 
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia:  Password123! 
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']

## 7. Refaktoring do funkcji

KOD:
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

    print(problems)


#Zaczytanie hasla z klawiatury
password = input("Podaj haslo do sprawdzenia: ")

validate_password(password, 12)

Terminal:
──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia:  ___ 
['Haslo ma mniej niz 12 znakow.', 'Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu', 'Brak cyfry', 'Brak malej litery', 'Brak duzej litery', 'Brak znaku specjalnego `!@#$%^&*`']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia:  Password123!
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia: Password123! 
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']
                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/LAB/LAB18]
└─$ python password_check.py
Podaj haslo do sprawdzenia:  Password123! 
['Haslo nie moze zawierac znakow spacji na poczatku czy tez koncu']


