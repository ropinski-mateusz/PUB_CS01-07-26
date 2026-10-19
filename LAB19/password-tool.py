import argparse
import sys
from password_validator import PasswordValidator


def parse_arguments():
    """Funkcja odpowiedzialna za parsowanie argumentow wiersza polecen (CLI)."""
    parser = argparse.ArgumentParser(
        description="Narzędzie CLI do sprawdzania polityki bezpieczenstwa hasel."
    )

    # Argumenty konfiguracji walidatora
    parser.add_argument(
        "--minLength",
        type=int,
        default=12,
        help="Minimalna wymagana dl hasla (domyslnie: 12)"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--password",
        type=str,
        help="Pojedyncze hasło testowe do zwalidowania"
    )
    group.add_argument(
        "--file",
        type=str,
        help="Ścieżka do pliku zawierającego hasła (jedno hasło na linię)"
    )

    return parser.parse_args()


def mask_password(password):
    """Zwraca bezpieczną reprezentację hasła z zachowaniem długości, nie ujawniając znaków wprost."""
    if not password:
        return "<puste>"
    return "*" * len(password)


def validate_single(validator, password):
    """Obsługuje walidację pojedynczego hasła i wypisuje bezpieczny wynik."""
    is_valid, problems = validator.validate_password(password)
    masked = mask_password(password)

    if is_valid:
        print(f"[OK] Hasło ({masked}, długość: {len(password)}) spełnia politykę bezpieczeństwa.")
    else:
        print(f"[BŁĄD] Hasło ({masked}, długość: {len(password)}) NIE spełnia polityki:")
        for problem in problems:
            print(f"  - {problem}")


def validate_from_file(validator, filepath):
    """Obsługuje walidację haseł z pliku linia po linii."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Błąd: Plik '{filepath}' nie został odnaleziony.", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Błąd podczas odczytu pliku '{filepath}': {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Walidacja haseł z pliku: {filepath} (łącznie linii: {len(lines)})\n" + "-" * 50)
    for index, raw_line in enumerate(lines, start=1):
        # Usuwamy znak nowej linii, zachowując ewentualne spacje brzegowe hasła do walidacji
        password = raw_line.rstrip("\r\n")
        is_valid, problems = validator.validate_password(password)
        masked = mask_password(password)

        status = "OK" if is_valid else "BŁĄD"
        print(f"Linia {index:02d} [{status}] Hasło {masked}:")
        if not is_valid:
            for problem in problems:
                print(f"    - {problem}")


def main():
    args = parse_arguments()

    # Tworzenie walidatora na podstawie argumentów CLI z obsługą błędnej konfiguracji
    try:
        validator = PasswordValidator(minLength=args.minLength)
    except ValueError as exc:
        print(f"Błąd konfiguracji walidatora: {exc}", file=sys.stderr)
        sys.exit(1)

    # Sprawdzanie pojedynczego hasła lub pliku
    if args.password is not None:
        validate_single(validator, args.password)
    elif args.file is not None:
        validate_from_file(validator, args.file)


if __name__ == "__main__":
    main()