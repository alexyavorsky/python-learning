# 2
def check_winners(scores, student_score) -> None:
    scores.append(student_score)
    sorted_scores = sorted(scores)
    if student_score in sorted_scores[-3:]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


# 3
def print_pack_report(count) -> None:
    for c in range(count, 0, -1):
        if c % 3 == 0 and c % 5 == 0:
            print(c, "- расфасуем по 3 или по 5")
        elif c % 3 == 0:
            print(c, "- расфасуем по 3")
        elif c % 5 == 0:
            print(c, "- расфасуем по 5")
        else:
            print(c, "- не заказываем")


# 4
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class PasswordSettings:
    lower = 0
    upper = 1
    symbols = 2
    digits = 3
    length = 4


def generate_password(settings=(1, 1, 1, 1, 20)):
    try:
        pull = ""
        length = settings[PasswordSettings.length]
        if settings[PasswordSettings.lower] == 1:
            pull += ascii_lowercase
        if settings[PasswordSettings.upper] == 1:
            pull += ascii_uppercase
        if settings[PasswordSettings.symbols] == 1:
            pull += punctuation
        if settings[PasswordSettings.digits] == 1:
            pull += digits
        password = [random.choice(pull) for _ in range(length)]
        for _ in range(3):
            random.shuffle(password)
        return password
    except ValueError:
        return 0


def main():
    print("=== Генератор паролей ===")
    lower = int(input("Строчные буквы?   1 - да, 0 - нет: "))
    upper = int(input("Заглавные буквы?  1 - да, 0 - нет: "))
    symbols = int(input("Символы?          1 - да, 0 - нет: "))
    digits_ = int(input("Цифры?            1 - да, 0 - нет: "))
    length = int(input("Длина пароля: "))

    settings = [lower, upper, symbols, digits_, length]
    sum_settings = sum(settings[:4])
    if sum_settings == 0:
        print("вы не выбрали никакие настройки")
        return
    if length == 0:
        print("длина должна быть больше 0")
        return
    if sum_settings > length:
        print("недостаточно длины для пароля с вашими функциями")
        return
    while True:
        password = generate_password(settings=settings)
        if password != 0:
            if lower and not any(symbol in ascii_lowercase for symbol in password):
                continue
            if upper and not any(symbol in ascii_uppercase for symbol in password):
                continue
            if symbols and not any(symbol in punctuation for symbol in password):
                continue
            if digits and not any(symbol in digits for symbol in password):
                continue

            print("Ваш пароль:", "".join(password))
            break

# 5
print("игра")