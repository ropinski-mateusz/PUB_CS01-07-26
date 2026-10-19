# Python CLI — cheatsheet do labu 19

## `venv`

Utworzenie środowiska:

```bash
python3 -m venv venv
```

Aktywacja Linux/macOS:

```bash
source venv/bin/activate
```

Aktywacja Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Dezaktywacja:

```bash
deactivate
```

## `pip`

Instalacja pakietu w aktywnym środowisku:

```bash
python -m pip install nazwa-pakietu
```

Lista pakietów:

```bash
python -m pip list
```

Instalacja zależności z pliku:

```bash
python -m pip install -r requirements.txt
```

## Moduły

Import całego modułu:

```python
import module_name
```

Import konkretnej klasy lub funkcji:

```python
from module_name import SomeClass
```

Unikaj:

```python
from module_name import *
```

## Punkt wejścia programu

Typowy wzorzec:

```python
def main():
    pass


if __name__ == "__main__":
    main()
```

Kod pod tym warunkiem uruchamia się przy bezpośrednim wykonaniu pliku, ale nie przy imporcie modułu.

## `argparse`

Minimalny schemat:

```python
import argparse

parser = argparse.ArgumentParser(description="Opis programu")
parser.add_argument("--option")
args = parser.parse_args()
```

Argument liczbowy:

```python
parser.add_argument("--min-length", type=int, default=12)
```

Flaga logiczna:

```python
parser.add_argument("--verbose", action="store_true")
```

Pomoc:

```bash
python password_tool.py --help
```

Jeżeli argument ma nadpisywać wartość z opcjonalnego pliku konfiguracyjnego, parser może używać `None`, aby można było rozpoznać, że użytkownik nie podał argumentu:

```python
parser.add_argument("--min-length", type=int, default=None)
```

## JSON

Odczyt obiektu JSON z pliku UTF-8:

```python
import json

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
```

Podstawowe typy:

| JSON | Python |
|---|---|
| obiekt `{}` | `dict` |
| tablica `[]` | `list` |
| tekst | `str` |
| liczba całkowita | `int` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

## Dobre praktyki projektu

- Logika walidacji powinna być oddzielona od CLI.
- Moduł z logiką nie powinien uruchamiać programu przy imporcie.
- Katalog `venv` nie powinien trafiać do repozytorium.
- Zależności powinny być jawne.
- Raport nie powinien wypisywać haseł wprost.
