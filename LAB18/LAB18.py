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

