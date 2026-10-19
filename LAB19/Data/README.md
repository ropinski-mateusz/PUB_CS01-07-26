# Lab 19 — Python cz. 2: klasy, moduły, `venv` i CLI

## Cel laboratorium

W tym laboratorium rozwiniesz walidator hasła z poprzedniej lekcji do małego narzędzia CLI.

Po wykonaniu ćwiczenia powinieneś mieć projekt, który:

- działa w osobnym środowisku wirtualnym `venv`,
- ma podział na moduły,
- zawiera klasę `PasswordValidator`,
- używa `__init__` do konfiguracji walidatora,
- używa bezpiecznej reprezentacji tekstowej obiektu,
- udostępnia CLI zbudowane na `argparse`,
* - potrafi wczytać własną politykę z pliku `config.json`,
- waliduje pojedyncze hasło testowe lub zestaw danych z pliku,
- nie wypisuje prawdziwych sekretów w raporcie,
- obsługuje błędne argumenty i brak pliku wejściowego.

## Założenia

Pracujesz na bazie walidatora z lekcji 18. Jeżeli nie masz swojego kodu, odtwórz najpierw minimalną wersję funkcji walidującej hasło według polityki:

- minimum 12 znaków,
- mała litera,
- wielka litera,
- cyfra,
- znak specjalny z zestawu `!@#$%^&*`,
- brak pustego hasła,
- brak spacji na początku i końcu.

W tym labie nie ma pełnego rozwiązania kodowego. Dostajesz wymagania, strukturę, testy i kryteria akceptacji. Implementację przygotowujesz samodzielnie.

## Struktura docelowa

Utwórz projekt o następującej strukturze:

```text
password-tool/
├── password_tool.py
├── password_validator.py
├── config.json
├── passwords-sample.txt
├── requirements.txt
└── README.md
```

Znaczenie plików:

- `password_validator.py` — klasa `PasswordValidator` i logika walidacji,
- `password_tool.py` — interfejs CLI, `argparse`, `main()`,
- `passwords-sample.txt` — testowe hasła do walidacji,
- `config.json` — opcjonalna polityka walidacji zapisana jako JSON,
- `requirements.txt` — zależności projektu,
- `README.md` — krótka instrukcja uruchomienia narzędzia.

## Materiały w tym labie

W katalogu `materials/` znajdziesz:

- `passwords-sample.txt` — przykładowe dane testowe,
- `config-sample.json` — przykładowa polityka do skopiowania jako `config.json`,
- `project-readme-template.md` — szablon krótkiej dokumentacji projektu,
- `expected-behavior.md` — opis oczekiwanego zachowania narzędzia.

W katalogu `references/` znajdziesz:

- `python-cli-cheatsheet.md` — skrót pojęć i komend używanych w labie.

## Część 1 — przygotowanie projektu

Wykonaj następujące zadania:

1. Utwórz katalog projektu `password-tool`.
2. Wejdź do katalogu projektu.
3. Utwórz środowisko wirtualne `venv`.
4. Aktywuj środowisko.
5. Sprawdź wersję Pythona.
6. Sprawdź, czy `pip` działa w kontekście aktywnego środowiska.
7. Utwórz pliki `password_tool.py` i `password_validator.py`.
8. Skopiuj testowe dane z `/materials/passwords-sample.txt` do pliku `passwords-sample.txt` w katalogu projektu.
9. Skopiuj `/materials/config-sample.json` jako `config.json` w katalogu projektu.

Kryteria akceptacji:

- katalog projektu istnieje,
- środowisko `venv` jest utworzone i aktywne,
- projekt ma dwa główne pliki `.py`,
- testowy plik z hasłami znajduje się w katalogu projektu.
- projekt zawiera przykładowy plik `config.json`.

## Część 2 — moduł `password_validator.py`

W pliku `password_validator.py` przygotuj logikę walidacji.

Wymagania:

1. Zdefiniuj klasę `PasswordValidator`.
2. Dodaj konfigurację walidatora w `__init__`.
3. Konfiguracja powinna obejmować:
   - minimalną długość hasła,
   - wymaganie małej litery,
   - wymaganie wielkiej litery,
   - wymaganie cyfry,
   - wymaganie znaku specjalnego,
   - zestaw dopuszczalnych znaków specjalnych.
4. Dodaj walidację konfiguracji: minimalna długość nie może być mniejsza niż `1`.
5. Dodaj metodę walidującą pojedyncze hasło.
6. Metoda walidująca ma zwracać:
   - informację, czy hasło spełnia politykę,
   - listę problemów, jeśli hasło jest niepoprawne.
7. Dodaj bezpieczną reprezentację tekstową walidatora.

Ograniczenia bezpieczeństwa:

- klasa nie powinna wypisywać hasła w reprezentacji tekstowej,
- klasa nie powinna pobierać danych od użytkownika,
- klasa nie powinna sama czytać argumentów CLI,
- klasa nie powinna uruchamiać programu przy imporcie modułu.

Kryteria akceptacji:

- moduł można zaimportować bez uruchomienia programu,
- obiekt walidatora można utworzyć z konfiguracją domyślną,
- obiekt walidatora można utworzyć z inną minimalną długością,
- błędna minimalna długość powoduje czytelny błąd,
- metoda walidująca zwraca wynik i listę problemów.

## Część 3 — moduł `password_tool.py`

W pliku `password_tool.py` przygotuj punkt wejścia programu CLI.

Wymagania:

1. Zaimportuj klasę `PasswordValidator` z modułu `password_validator.py`.
2. Dodaj funkcję odpowiedzialną za parsowanie argumentów CLI.
3. Dodaj funkcję `main()`.
4. Zabezpiecz uruchomienie programu idiomem `if __name__ == "__main__"`.
5. Utwórz walidator na podstawie argumentów CLI.
6. Obsłuż walidację pojedynczego hasła testowego.
7. Obsłuż walidację haseł z pliku.
8. Zadbaj o czytelne komunikaty błędów.
9. Zadbaj, aby raport nie wypisywał prawdziwych haseł wprost.

Kryteria akceptacji:

- `password_tool.py` uruchamia program,
- `password_validator.py` zawiera logikę walidacji,
- logika walidacji nie jest wymieszana z `argparse`,
- import modułu z walidatorem nie uruchamia programu.

## Część 4 — argumenty CLI

Narzędzie powinno obsługiwać następujące argumenty:

| Argument | Cel |
|---|---|
| `--min-length` | ustawia minimalną długość hasła |
| `--config` | wskazuje opcjonalny plik JSON z polityką walidacji |
| `--password` | przekazuje pojedyncze hasło testowe |
| `--file` | wskazuje plik z hasłami testowymi |
| `--verbose` | włącza bardziej szczegółowy raport bez ujawniania sekretów |

Zasady:

- jeżeli ani CLI, ani `config.json` nie określają minimalnej długości, jej efektywna wartość ma wynosić `16`,
- `--min-length` musi być liczbą całkowitą większą od `0`,
- `--config` przyjmuje ścieżkę do pliku JSON,
- użytkownik może podać `--password` albo `--file`,
- użytkownik nie powinien podawać jednocześnie `--password` i `--file`,
- program ma obsługiwać `--help`,
- program ma czytelnie zgłaszać niepoprawne argumenty.

Uwaga bezpieczeństwa: w realnych systemach nie należy przekazywać prawdziwych haseł jako argumentów CLI. W tym labie `--password` służy wyłącznie do pracy na danych testowych.

## Część 5 — tryb pojedynczego hasła

Zaimplementuj uruchomienie narzędzia dla jednego hasła testowego.

Wymagania:

1. Program przyjmuje hasło przez argument CLI.
2. Program tworzy obiekt `PasswordValidator`.
3. Program waliduje hasło.
4. Program wypisuje, czy hasło spełnia politykę.
5. Program wypisuje listę problemów, jeśli hasło nie spełnia polityki.
6. Program nie wypisuje sprawdzanego hasła w raporcie końcowym.

Przypadki do sprawdzenia:

- hasło za krótkie,
- hasło bez cyfry,
- hasło bez znaku specjalnego,
- hasło poprawne.

## Część 6 — tryb pliku

Zaimplementuj walidację haseł testowych z pliku.

Wymagania:

1. Program przyjmuje ścieżkę do pliku przez argument CLI.
2. Program sprawdza, czy plik istnieje.
3. Program czyta plik linia po linii.
4. Program waliduje każdy wpis osobno.
5. Program raportuje wynik dla każdego wpisu bez wypisywania hasła wprost.
6. Program obsługuje pustą linię jako przypadek testowy.
7. Program obsługuje brak pliku czytelnym komunikatem błędu.

Sugerowany sposób raportowania:

- numer linii,
- status: poprawne lub niepoprawne,
- liczba problemów,
- lista problemów.

Nie raportuj treści hasła.

* - zadanie z gwiazdką
## Część 7 — konfiguracja polityki w `config.json`

Rozbuduj narzędzie tak, aby polityka walidacji nie musiała być na stałe zapisana w kodzie ani przekazywana wyłącznie przez argumenty CLI. Po umieszczeniu w katalogu projektu pliku `config.json` użytkownik powinien móc określić własne wymagania dotyczące sprawdzanych haseł.

Konfiguracja ma opisywać wyłącznie **politykę walidacji**. Nie zapisuj w niej haseł, tokenów, kluczy ani innych sekretów.

### Dozwolone pola

Plik może zawierać następujące pola:

| Pole | Typ | Znaczenie |
|---|---|---|
| `min_length` | liczba całkowita większa od `0` | minimalna liczba znaków |
| `require_lower` | wartość logiczna | wymaga co najmniej jednej małej litery |
| `require_upper` | wartość logiczna | wymaga co najmniej jednej wielkiej litery |
| `require_digit` | wartość logiczna | wymaga co najmniej jednej cyfry |
| `require_special` | wartość logiczna | wymaga znaku z `special_chars` |
| `special_chars` | tekst | zestaw znaków uznawanych za specjalne |

Przykładowy `config.json`:

```json
{
  "min_length": 14,
  "require_lower": true,
  "require_upper": true,
  "require_digit": true,
  "require_special": true,
  "special_chars": "!@#$%^&*"
}
```

JSON używa wartości `true` i `false` zapisanych małymi literami. Nie są to napisy, dlatego nie umieszczaj ich w cudzysłowie.

### Sposób wyboru pliku

Zaimplementuj następujące zachowanie:

1. Jeżeli użytkownik poda `--config SCIEZKA`, program wczytuje wskazany plik.
2. Jeżeli `--config` nie został podany, ale w bieżącym katalogu istnieje `config.json`, program wczytuje go automatycznie.
3. Jeżeli nie podano `--config` i nie istnieje lokalny `config.json`, program używa polityki wbudowanej.
4. Jeżeli użytkownik jawnie podał `--config`, a wskazany plik nie istnieje, program kończy działanie czytelnym błędem. Nie powinien wtedy cicho przechodzić do wartości domyślnych.

Przykładowe uruchomienia:

```bash
python password_tool.py --file passwords-sample.txt
python password_tool.py --config config.json --file passwords-sample.txt
python password_tool.py --config policies/strict.json --password 'TestoweHaslo2026!'
```

Ostatnia komenda zawiera wyłącznie wartość testową. Prawdziwych haseł nie należy przekazywać przez argumenty CLI.

### Kolejność nadpisywania wartości

Przyjmij jednoznaczną kolejność priorytetów:

```text
jawny argument CLI → config.json → wartości wbudowane
```

W obecnym zakresie tylko `--min-length` nadpisuje pojedynczy parametr polityki z pliku. Przykład:

```bash
python password_tool.py \
  --config config.json \
  --min-length 20 \
  --file passwords-sample.txt
```

Jeżeli `config.json` zawiera `"min_length": 14`, efektywna wartość wynosi w tym uruchomieniu `20`.

Aby rozpoznać, czy użytkownik rzeczywiście podał `--min-length`, możesz na poziomie `argparse` użyć wartości `None`, a efektywną wartość `16` zastosować dopiero podczas łączenia konfiguracji. W przeciwnym razie domyślna wartość parsera mogłaby nieświadomie nadpisywać wartość z pliku.

### Podział odpowiedzialności w kodzie

Nie umieszczaj całej obsługi JSON bezpośrednio w `main()`. Wydziel co najmniej funkcję odpowiedzialną za wczytanie konfiguracji, na przykład:

```python
def load_config(config_path):
    ...
```

Możesz również wydzielić funkcje:

```python
def validate_config(config):
    ...


def build_policy(args, config):
    ...
```

Do odczytu użyj modułu `json` z biblioteki standardowej. Otwórz plik jawnie z kodowaniem UTF-8. Nie używaj `eval()` ani wykonywania treści konfiguracji jako kodu.

Po walidacji utwórz `PasswordValidator` z uzyskanych wartości. Logika sprawdzania haseł nadal powinna znajdować się w `password_validator.py`; obsługa pliku i CLI należy do `password_tool.py`.

### Walidacja konfiguracji

Program powinien odrzucać konfigurację, gdy:

- plik nie jest poprawnym dokumentem JSON,
- główną wartością JSON jest lista, tekst albo liczba zamiast obiektu,
- `min_length` nie jest liczbą całkowitą większą od `0`,
- dowolne pole `require_*` nie jest wartością logiczną,
- `special_chars` nie jest tekstem,
- `require_special` ma wartość `true`, ale `special_chars` jest pusty,
- występuje nieznany klucz, na przykład `minimum_lenght` z literówką.

Nie ignoruj nieznanych kluczy. Literówka w nazwie parametru mogłaby spowodować zastosowanie słabszej polityki niż oczekiwana.

Obsłuż osobno co najmniej:

- `FileNotFoundError`,
- błąd dekodowania JSON,
- błąd walidacji wartości polityki.

Komunikat powinien wskazywać plik i rodzaj problemu, ale nie powinien wypisywać danych wejściowych ani sekretów.

### Kryteria akceptacji

- brak `config.json` nie uniemożliwia użycia polityki wbudowanej,
- lokalny `config.json` jest wykrywany automatycznie,
- `--config` pozwala wskazać plik w innym katalogu,
- wartości z poprawnego pliku trafiają do `PasswordValidator`,
- jawne `--min-length` nadpisuje `min_length` z JSON,
- brak jawnie wskazanego pliku kończy program błędem,
- błędny JSON, zły typ, niedozwolona wartość i nieznany klucz są odrzucane,
- komunikaty nie ujawniają sprawdzanych haseł,
- konfiguracja nie zawiera danych wejściowych `password` ani `file`.

## Część 8 — dokumentacja projektu

Przygotuj plik `README.md` w katalogu projektu.

Powinien zawierać:

- nazwę narzędzia,
- krótki opis,
- wymagania,
- instrukcję utworzenia `venv`,
- instrukcję uruchomienia,
- opis argumentów CLI,
- opis formatu i priorytetów `config.json`,
- przykładowe komendy z danymi testowymi,
- ostrzeżenie, że nie należy przekazywać prawdziwych haseł przez argumenty CLI.

Możesz użyć szablonu z `materials/project-readme-template.md`.

## Część 9 — zależności

Podstawowa wersja narzędzia powinna działać wyłącznie na bibliotece standardowej Pythona.

Wymagania:

1. Utwórz plik `requirements.txt`.
2. Jeśli nie używasz pakietów zewnętrznych, zostaw plik pusty albo dodaj komentarz w README, że projekt nie wymaga zależności zewnętrznych.
3. Jeśli dodajesz pakiet zewnętrzny jako rozszerzenie, opisz po co jest potrzebny.
4. Nie dodawaj pakietu tylko po to, żeby “coś zainstalować”.

Opcjonalne rozszerzenie:

- dodać pakiet do estetycznego wyświetlania wyników,
- zapisać go w `requirements.txt`,
- upewnić się, że główna logika walidacji nie zależy od tego pakietu.

## Część 10 — testy ręczne

Przetestuj narzędzie na danych z `passwords-sample.txt`.

Minimalny zestaw testów:

| Test | Oczekiwane zachowanie |
|---|---|
| `--help` | program pokazuje opis użycia |
| poprawna minimalna długość | program używa podanej wartości |
| minimalna długość `0` | program zgłasza błąd konfiguracji |
| minimalna długość ujemna | program zgłasza błąd konfiguracji |
| pojedyncze hasło testowe | program zwraca wynik walidacji |
| plik z hasłami | program waliduje wszystkie linie |
| nieistniejący plik | program zgłasza czytelny błąd |
| jednoczesne `--password` i `--file` | program odrzuca niejednoznaczne wejście |
| brak `config.json` | program używa polityki wbudowanej |
| poprawny `config.json` | program używa wartości z pliku |
| `--min-length` razem z konfiguracją | wartość z CLI nadpisuje wartość z JSON |
| jawnie wskazany brakujący plik konfiguracyjny | program zgłasza czytelny błąd |
| niepoprawny JSON | program zgłasza błąd formatu konfiguracji |
| główna wartość JSON jest listą | program odrzuca konfigurację |
| nieznany klucz w JSON | program odrzuca konfigurację zamiast go ignorować |
| niewłaściwy typ pola | program wskazuje błędny parametr polityki |
| pusty `special_chars` przy wymaganym znaku specjalnym | program odrzuca niespójną politykę |


## Kryteria zaliczenia

Minimalny rezultat:

- istnieje projekt `password-tool`,
- projekt działa w `venv`,
- istnieją pliki `password_validator.py` i `password_tool.py`,
- klasa `PasswordValidator` działa dla domyślnej konfiguracji,
- narzędzie obsługuje `--help`,
- narzędzie waliduje pojedyncze hasło testowe,
- narzędzie zwraca konkretne problemy dla danych niepoprawnych.

Pełny rezultat:

- projekt ma czytelny podział na moduły,
- import modułu z walidatorem nie uruchamia programu,
- narzędzie obsługuje plik wejściowy,
- narzędzie obsługuje błędną konfigurację,
- narzędzie obsługuje brak pliku,
*
- narzędzie wczytuje i waliduje politykę z `config.json`,
- jawny argument CLI ma udokumentowane pierwszeństwo przed konfiguracją,
- nieznane pola i błędne typy konfiguracji są odrzucane,
*
- raport nie ujawnia haseł wprost,
- projekt ma krótkie `README.md`,
- zależności są jawne i uporządkowane.
