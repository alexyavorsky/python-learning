alphabet_list_eng = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
alphabet_list_ru = [
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]
length_eng = len(alphabet_list_eng)
length_ru = len(alphabet_list_ru)


def encode(text, sdvig):
    text = text.lower()
    encoded_text = []
    if text[0] in alphabet_list_eng:
        for symbol in text:
            index = alphabet_list_eng.index(symbol) + sdvig
            new_index = index % length_eng
            encoded_text.append(alphabet_list_eng[new_index])
    else:
        for symbol in text:
            index = alphabet_list_ru.index(symbol) + sdvig
            new_index = index % length_ru
            encoded_text.append(alphabet_list_ru[new_index])
    return "".join(encoded_text)


def decode(encoded_text, sdvig):
    return encode(encoded_text, -sdvig)


print(encode("приветяя", 3))
print(decode("aazzaa", 3))
