# Laboratorium 18 — Python cz. 1: walidator hasła

## Cel laboratorium

W tym laboratorium samodzielnie napiszesz skrypt `password_check.py`, który sprawdza zgodność hasła z prostą polityką bezpieczeństwa. Instrukcja określa wymagane zachowanie programu.

Podczas ćwiczenia wykorzystasz:

- zmienne i podstawowe typy danych,
- instrukcje warunkowe,
- pętle,
- funkcje,
- listy, słowniki i sety,
- podstawową obsługę błędów.

## Wymagania

Potrzebujesz:

- Pythona 3,
- terminala,
- edytora tekstu,
- katalogu roboczego na plik `password_check.py`.

## Polityka hasła

Program ma sprawdzać, czy hasło:

- ma co najmniej 12 znaków,
- zawiera co najmniej jedną małą literę,
- zawiera co najmniej jedną wielką literę,
- zawiera co najmniej jedną cyfrę,
- zawiera co najmniej jeden znak specjalny z zestawu `!@#$%^&*`,
- nie jest puste,
- nie zawiera spacji na początku ani na końcu.

Jeżeli hasło nie spełnia polityki, program ma wypisać wszystkie wykryte problemy. W końcowym raporcie nie wolno wypisywać podanego hasła.

## 0. Sprawdzenie środowiska

Sprawdź wersję Pythona 3:

```bash
python3 --version
```

Jeżeli w Twoim środowisku dostępna jest również komenda `python`, sprawdź ją:

```bash
python --version
```

Przygotuj katalog roboczy i utwórz w edytorze pusty plik `password_check.py`.

Do uruchamiania skryptu w kolejnych częściach używaj:

```bash
python3 password_check.py
```

## 1. REPL i pierwsze instrukcje

Uruchom REPL:

```bash
python3
```

W REPL samodzielnie napisz i wykonaj instrukcje, które:

- utwórz zmienną `name` z wartością `LearnIT`,
- sprawdź długość napisu,
- zamień napis na wielkie litery,
- sprawdź, czy napis zawiera literę `L`,
- zakończ pracę z REPL.

## 2. Pierwszy plik skryptu

Napisz w pliku `password_check.py` pierwszą wersję programu.

Program ma:

- pobrać hasło,
- sprawdzić jego długość,
- wypisać informację, czy hasło ma co najmniej 12 znaków.

Uruchom skrypt:

```bash
python3 password_check.py
```

Przetestuj kolejno:

- `admin`,
- `VeryLongPassword`.

## 3. Lista problemów

Zmień skrypt tak, aby:

- utwórz listę problemów,
- wykrywaj puste hasło,
- wykrywaj hasło krótsze niż 12 znaków,
- po zakończeniu walidacji wypisz wynik oraz wszystkie znalezione problemy.

Uruchom skrypt ponownie:

```bash
python3 password_check.py
```

Przetestuj kolejno:

- pusty Enter,
- `admin`,
- `VeryLongPassword`.

## 4. Mała litera, wielka litera i cyfra

Rozbuduj skrypt:

- dodaj zmienne logiczne opisujące znalezione typy znaków,
- przejdź po wszystkich znakach hasła,
- wykryj małą literę,
- wykryj wielką literę,
- wykryj cyfrę,
- dodaj osobny komunikat dla każdego brakującego wymagania.

Uruchom skrypt:

```bash
python3 password_check.py
```

Przetestuj kolejno:

- `password123`,
- `Password`,
- `PASSWORD123`,
- `Password123`.

## 5. Znak specjalny i set

Rozbuduj skrypt:

- utwórz set zawierający `!@#$%^&*`,
- sprawdź, czy hasło zawiera przynajmniej jeden znak z tego zestawu,
- dodaj komunikat o braku znaku specjalnego.

Uruchom skrypt:

```bash
python3 password_check.py
```

Przetestuj kolejno:

- `Password123`,
- `Password123!`,
- `Password123?`.

Znak `?` nie należy do zestawu używanego w tym ćwiczeniu.

## 6. Spacje na początku lub końcu

Dodaj kontrolę spacji na brzegach hasła:

- wykryj spację na początku albo końcu hasła,
- nie modyfikuj po cichu wartości wpisanej przez użytkownika,
- dodaj odpowiedni problem do listy.

Uruchom skrypt:

```bash
python3 password_check.py
```

Przetestuj kolejno:

- ` Password123!`,
- `Password123! `,
- ` Password123! `.

## 7. Refaktoring do funkcji

Przeprowadź refaktoring:

- utwórz funkcję `validate_password` przyjmującą hasło i minimalną długość,
- wykonaj w niej wszystkie dotychczasowe kontrole,
- zwróć informację o poprawności oraz listę problemów,
- oddziel walidację od prezentacji wyniku,
- ustaw minimalną długość na 12.

Uruchom skrypt:

```bash
python3 password_check.py
```

Powtórz wcześniejsze przypadki i sprawdź, czy po refaktoringu wyniki się nie zmieniły.

## 8. Przypadki testowe

Dodaj słownik przypadków testowych i użyj pętli do ich sprawdzenia.

Słownik ma obejmować:

- puste hasło,
- hasło za krótkie,
- hasło bez wielkiej litery,
- hasło bez cyfry,
- hasło bez znaku specjalnego,
- hasło ze spacjami na brzegach,
- hasło spełniające politykę.

Uruchom skrypt:

```bash
python3 password_check.py
```

Sprawdź, czy raport zawiera nazwę przypadku i wynik, ale nie wypisuje testowanego hasła.

## 9. Obsługa błędu konfiguracji

Dodaj obsługę konfigurowalnej minimalnej długości:

- pobierz minimalną długość od użytkownika,
- dla pustego wejścia zastosuj wartość 12,
- przekonwertuj podaną wartość na liczbę całkowitą,
- obsłuż błędną wartość przez `try` i `except`,
- nie kontynuuj walidacji przy błędnej konfiguracji.

Uruchom skrypt dla każdego wariantu:

```bash
python3 password_check.py
```

Przetestuj konfigurację:

- pusty Enter — program używa wartości `12`,
- `10` — program używa wartości `10`,
- `abc` — program pokazuje błąd konfiguracji.

## 10. Wersja końcowa

Uporządkuj końcową wersję skryptu:

- pozostaw logikę walidacji w funkcji `validate_password`,
- dodaj funkcję `print_result`,
- pobierz i zweryfikuj minimalną długość,
- pobierz hasło tylko przy poprawnej konfiguracji,
- nie wypisuj hasła w raporcie.

Uruchom wersję końcową:

```bash
python3 password_check.py
```

## 11. Test końcowy

Dla każdego przypadku uruchom:

```bash
python3 password_check.py
```

Sprawdź wyniki:

| Przypadek | Wejście | Oczekiwany wynik |
|---|---|---|
| Puste hasło | pusty Enter | błąd: hasło nie może być puste |
| Za krótkie hasło | `admin` | kilka problemów, w tym zbyt krótka długość |
| Brak wielkiej litery | `password123!` | problem z brakiem wielkiej litery |
| Brak cyfry | `PasswordTest!` | problem z brakiem cyfry |
| Brak znaku specjalnego | `Password1234` | problem z brakiem znaku specjalnego |
| Spacje na brzegach | ` Password123! ` | problem ze spacją na początku lub końcu |
| Poprawne hasło | `VeryStrongPassword2026!` | hasło spełnia politykę |

Jeżeli wynik różni się od oczekiwanego, sprawdź:

- czy funkcja zwraca informację o poprawności i listę problemów,
- czy wszystkie warunki dopisują komunikaty do listy problemów,
- czy pętla analizująca znaki hasła znajduje się we właściwym miejscu,
- czy set znaków specjalnych jest zdefiniowany przed użyciem,
- czy końcowy wynik zależy od tego, czy lista problemów jest pusta,
- czy minimalna długość jest przekazywana do funkcji walidującej.

## 12. Sprawdzenie kryteriów zaliczenia

Potwierdź minimalny rezultat:

- istnieje plik `password_check.py`,
- program uruchamia się bez błędów składni,
- program pobiera hasło od użytkownika,
- program rozpoznaje hasło poprawne i niepoprawne,
- program wypisuje listę konkretnych problemów,
- program nie wypisuje podanego hasła w końcowym raporcie.

Potwierdź pełny rezultat:

- logika znajduje się w funkcji `validate_password`,
- funkcja zwraca wynik logiczny i listę problemów,
- skrypt używa listy problemów,
- skrypt używa seta znaków specjalnych,
- skrypt zawiera przypadki testowe w liście lub słowniku,
- skrypt obsługuje błędną minimalną długość przez `try` i `except`.
