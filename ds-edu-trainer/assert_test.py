def set_age(age: int) -> str:
    assert type(age) == int, "Возраст должен быть целым числом"
    assert age >= 0, "Возраст должен быть положительным"
    assert age <= 120, "Ты столько не проживешь"
    s = f"Ваш возраст: {age}"
    return s

print(set_age(132))