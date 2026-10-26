# Password Tool

## Opis

`password-tool` to narzędzie CLI do walidacji haseł testowych zgodnie z prostą polityką bezpieczeństwa.

Narzędzie służy do nauki klas, modułów, środowisk wirtualnych i `argparse`. Nie jest produkcyjnym systemem oceny haseł.

## Wymagania

- Python 3
- środowisko wirtualne `venv`

## Przygotowanie środowiska

1. Utwórz środowisko wirtualne.
2. Aktywuj środowisko.
3. Zainstaluj zależności, jeśli projekt ich wymaga.

## Uruchomienie

Przykładowe tryby użycia:

- wyświetlenie pomocy,
- walidacja pojedynczego hasła testowego,
- walidacja haseł z pliku,
- zmiana minimalnej długości hasła,
- użycie własnej polityki z `config.json`.

## Argumenty CLI

| Argument | Opis |
|---|---|
| `--min-length` | minimalna długość hasła |
| `--config` | ścieżka do pliku JSON z polityką |
| `--password` | pojedyncze hasło testowe |
| `--file` | plik z hasłami testowymi |
| `--verbose` | bardziej szczegółowy raport |

## Konfiguracja polityki

Opisz:

- obsługiwane pola `config.json`,
- sposób automatycznego wykrywania lokalnego pliku,
- użycie argumentu `--config`,
- kolejność priorytetów CLI → konfiguracja → wartości wbudowane,
- zachowanie dla brakującego albo niepoprawnego pliku.

Plik konfiguracji powinien zawierać wyłącznie politykę. Nie zapisuj w nim haseł, tokenów ani innych sekretów.

## Bezpieczeństwo

Nie używaj prawdziwych haseł, tokenów ani sekretów jako argumentów CLI.

W danych testowych używaj wyłącznie przykładowych wartości.

Raport nie powinien wypisywać haseł wprost.

## Ograniczenia

Narzędzie sprawdza formalną zgodność z prostą polityką. Nie zastępuje pełnej oceny bezpieczeństwa uwierzytelniania.
