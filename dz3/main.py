import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для роботи на Windows
init(autoreset=True)


def print_directory_tree(path: Path, indent: str = ""):
    """
    Рекурсивно обходить директорію та виводить файли й піддиректорії.
    :param path: Path — шлях до директорії
    :param indent: відступ для візуалізації вкладеності
    """
    try:
        # Сортуємо для стабільного виводу
        for item in sorted(path.iterdir()):
            if item.is_dir():
                # Директорії виділяємо синім кольором
                print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                print_directory_tree(item, indent + "    ")
            else:
                # Файли виділяємо зеленим кольором
                print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено до {path}]{Style.RESET_ALL}")


def main():
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка:{Style.RESET_ALL} не вказано шлях до директорії.")
        print(f"Використання: python {Path(sys.argv[0]).name} <шлях_до_директорії>")
        sys.exit(1)

    # Отримання шляху
    dir_path = Path(sys.argv[1]).expanduser().resolve()

    # Перевірки
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка:{Style.RESET_ALL} шлях '{dir_path}' не існує.")
        sys.exit(2)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка:{Style.RESET_ALL} '{dir_path}' не є директорією.")
        sys.exit(3)

    # Вивід структури директорії
    print(f"{Fore.CYAN}📦 {dir_path.name}{Style.RESET_ALL}")
    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()