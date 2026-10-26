import argparse
import json
import os
import sys
from password_validator import PasswordValidator

# Zbiór wszystkich dozwolonych kluczy w pliku JSON
ALLOWED_CONFIG_KEYS = {
    "min_length",
    "require_lower",
    "require_upper",
    "require_digit",
    "require_special",
    "special_chars",
}


def parse_arguments():
    """Parsuje argumenty CLI."""
    parser = argparse.ArgumentParser(
        description="Narzędzie CLI do sprawdzania polityki bezpieczeństwa haseł."
    )
    # Domyślnie None, aby odróżnić brak podania flagi od jawnej wartości
    parser.add_argument(
        "--min-length",
        type=int,
        default=None,
        dest="min_length",
        help="Minimalna wymagana długość hasła (liczba całkowita > 0)",
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Ścieżka do pliku JSON z polityką walidacji",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Włącza bardziej szczegółowy raport bez ujawniania haseł",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--password",
        type=str,
        help="Pojedyncze hasło testowe do zwalidowania",
    )
    group.add_argument(
        "--file",
        type=str,
        help="Ścieżka do pliku z hasłami testowymi",
    )

    return parser.parse_args()


def load_config(config_path):
    """Wczytuje i waliduje zawartość pliku JSON."""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Błąd: Plik konfiguracyjny '{config_path}' nie istnieje.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as err:
        print(f"Błąd formatu JSON w pliku '{config_path}': {err}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Błąd podczas odczytu pliku '{config_path}': {exc}", file=sys.stderr)
        sys.exit(1)

    # Główna wartość musi być słownikiem / obiektem
    if not isinstance(data, dict):
        print(f"Błąd: Główną wartością w '{config_path}' musi być obiekt JSON (słownik).", file=sys.stderr)
        sys.exit(1)

    # Wykrywanie nieznanych kluczy (np. literówek)
    for key in data:
        if key not in ALLOWED_CONFIG_KEYS:
            print(f"Błąd konfiguracji: Nieznany klucz '{key}' w pliku '{config_path}'.", file=sys.stderr)
            sys.exit(1)

    # Walidacja min_length
    if "min_length" in data:
        val = data["min_length"]
        if not isinstance(val, int) or isinstance(val, bool) or val < 1:
            print(f"Błąd konfiguracji: 'min_length' musi być liczbą całkowitą większą od 0.", file=sys.stderr)
            sys.exit(1)

    # Walidacja flag boolowskich require_*
    for field in ["require_lower", "require_upper", "require_digit", "require_special"]:
        if field in data and not isinstance(data[field], bool):
            print(f"Błąd konfiguracji: Pole '{field}' musi mieć wartość logiczną (true/false).", file=sys.stderr)
            sys.exit(1)

    # Walidacja znaków specjalnych
    if "special_chars" in data and not isinstance(data["special_chars"], str):
        print(f"Błąd konfiguracji: Pole 'special_chars' musi być tekstem.", file=sys.stderr)
        sys.exit(1)

    # Spójność: require_special=true przy pustym special_chars
    req_special = data.get("require_special", True)
    special_chars = data.get("special_chars", "!@#$%^&*")
    if req_special and (special_chars == "" or special_chars is None):
        print(f"Błąd konfiguracji: 'require_special' jest włączone, ale 'special_chars' jest puste.", file=sys.stderr)
        sys.exit(1)

    return data


def build_policy(args):
    """Buduje obiekt PasswordValidator według ustalonej hierarchii."""
    # Walidacja --min-length podanego w CLI
    if args.min_length is not None and args.min_length < 1:
        print("Błąd: Argument '--min-length' musi być liczbą całkowitą większą od 0.", file=sys.stderr)
        sys.exit(1)

    config_data = {}
    if args.config:
        # Jawnie wskazany plik przez flagę --config
        config_data = load_config(args.config)
    elif os.path.exists("config.json"):
        # Automatyczne wykrycie lokalnego config.json
        config_data = load_config("config.json")

    # Ustalenie minimalnej długości: CLI -> JSON -> 16
    if args.min_length is not None:
        effective_min_length = args.min_length
    elif "min_length" in config_data:
        effective_min_length = config_data["min_length"]
    else:
        effective_min_length = 16

    # Pozostałe parametry
    require_lower = config_data.get("require_lower", True)
    require_upper = config_data.get("require_upper", True)
    require_digit = config_data.get("require_digit", True)
    require_special = config_data.get("require_special", True)
    special_chars = config_data.get("special_chars", "!@#$%^&*")

    return PasswordValidator(
        minLength=effective_min_length,
        requireLowercase=require_lower,
        requireUppercase=require_upper,
        requireDigit=require_digit,
        requireSpecial=require_special,
        specialCharacters=special_chars,
    )


def mask_password(password):
    """Maskuje hasło gwiazdkami."""
    if not password:
        return "<puste>"
    return "*" * len(password)


def validate_single(validator, password, verbose=False):
    """Walidacja pojedynczego hasła."""
    if verbose:
        print(f"[VERBOSE] Konfiguracja: {validator}")

    is_valid, problems = validator.validate_password(password)
    masked = mask_password(password)

    if is_valid:
        print(f"[OK] Hasło ({masked}, długość: {len(password)}) spełnia politykę bezpieczeństwa.")
    else:
        print(f"[BŁĄD] Hasło ({masked}, długość: {len(password)}) NIE spełnia polityki:")
        for problem in problems:
            print(f"  - {problem}")


def validate_from_file(validator, filepath, verbose=False):
    """Walidacja haseł z pliku linia po linii."""
    if not os.path.exists(filepath):
        print(f"Błąd: Plik '{filepath}' nie istnieje.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as exc:
        print(f"Błąd podczas odczytu pliku '{filepath}': {exc}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"[VERBOSE] Konfiguracja: {validator}")
        print(f"[VERBOSE] Liczba linii do sprawdzenia: {len(lines)}")

    print(f"Walidacja haseł z pliku: {filepath}\n" + "-" * 60)

    for line_no, raw_line in enumerate(lines, start=1):
        password = raw_line.rstrip("\r\n")
        is_valid, problems = validator.validate_password(password)

        if is_valid:
            print(f"Linia {line_no:02d} | Status: POPRAWNE   | Problemy: 0")
        else:
            print(f"Linia {line_no:02d} | Status: NIEPOPRAWNE | Problemy: {len(problems)}")
            for problem in problems:
                print(f"    - {problem}")


def main():
    args = parse_arguments()
    validator = build_policy(args)

    if args.password is not None:
        validate_single(validator, args.password, verbose=args.verbose)
    elif args.file is not None:
        validate_from_file(validator, args.file, verbose=args.verbose)


if __name__ == "__main__":
    main()