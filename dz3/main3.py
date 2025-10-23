import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows
init(autoreset=True)


def print_directory_tree(path: Path, indent: str = ""):
    """
    Рекурсивно обходить директорію та виводить файли з піддиректорії.
    :param path: Path — шлях до директорії
    :param indent: відступ для візуалізації вкладеності
    """
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                # Директорії — яскраво синім кольором
                print(f"{indent}{Fore.CYAN}📂 {item.name}{Style.RESET_ALL}")
                print_directory_tree(item, indent + "    ")
            else:
                # Файли — жовтим кольором
                print(f"{indent}{Fore.YELLOW}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено: {path}]{Style.RESET_ALL}")


def main():
    # Якщо аргумент не передано — використовуємо поточну директорію
    if len(sys.argv) < 2:
        dir_path = Path.cwd()

        print(f"{Fore.MAGENTA}Не вказано шлях. Використовується поточна директорія: {dir_path.name}{Style.RESET_ALL}")
    else:
        # Отримуємо шлях з аргументу
        dir_path = Path(sys.argv[1]).expanduser().resolve()

    # Нормалізація шляху для Windows
    dir_path = Path(os.path.normpath(str(dir_path)))

    # Перевірки
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка:{Style.RESET_ALL} шлях '{dir_path}' не існує.")
        sys.exit(2)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка:{Style.RESET_ALL} '{dir_path}' не є директорією.")
        sys.exit(3)

    # Вивід структури директорії
    print(f"\n{Fore.GREEN}📦 Структура директорії: {dir_path.name}{Style.RESET_ALL}")
    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()

    # якщо чесно, то взагалі не знаю, що тут написати. тут попрацював за мене штучний інтелект    