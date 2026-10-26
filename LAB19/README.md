password-tool

Narzędzie CLI w Pythonie do walidacji haseł testowych w oparciu o obiektowy walidator i konfigurację JSON.

Uwaga: Używać wyłącznie z danymi testowymi. Prawdziwych haseł nie należy przekazywać jako argumenty CLI.

Wymagania

Python 3.8+

Wyłącznie biblioteka standardowa (argparse, json, os, sys)

Konfiguracja środowiska

python3 -m venv venv
source venv/bin/activate


Użycie CLI

Opcje:

--password TEKST – walidacja pojedynczego hasła

--file SCIEZKA – walidacja haseł z pliku linia po linii

--min-length N – nadpisanie minimalnej długości hasła

--config SCIEZKA – wskazanie własnego pliku konfiguracyjnego JSON

--verbose – wyświetlenie zastosowanej konfiguracji walidatora

Uwaga: Opcje --password i --file wykluczają się wzajemnie.

Przykłady poleceń:

# Pojedyncze hasło z domyślną konfiguracją (z config.json lub 16 znaków)
python password_tool.py --password 'SuperHaslo123!'

# Zmiana minimalnej długości z CLI i podgląd szczegółowy
python password_tool.py --min-length 8 --password 'Krotkie1!' --verbose

# Walidacja haseł z pliku
python password_tool.py --file passwords-sample.txt

# Jawne wskazanie pliku konfiguracyjnego
python password_tool.py --config config.json --file passwords-sample.txt


Konfiguracja (config.json)

Program automatycznie wczytuje plik config.json, jeśli znajduje się on w katalogu roboczym.

Hierarchia priorytetów:

Argument --min-length z CLI

Wartość min_length z pliku JSON

Wbudowana wartość domyślna (16 znaków)

Przykładowy format JSON:

{
  "min_length": 14,
  "require_lower": true,
  "require_upper": true,
  "require_digit": true,
  "require_special": true,
  "special_chars": "!@#$%^&*"
}


Niepoprawny format, nieobsługiwane klucze lub brak pliku wskazanego przez --config skutkują przerwaniem działania programu z czytelnym komunikatem błędu.