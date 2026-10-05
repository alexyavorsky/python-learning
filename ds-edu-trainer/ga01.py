"""
Термин в глоссарии
Грокаем алгоритмы → Глава 1. Бинарный поиск и «O-большое»
Сложность: лёгкая · Тип: реализовать · id: ga-find-term

Глоссарий учебника — отсортированный по алфавиту список терминов без
повторов. Напишите `find_term(terms, term)`: функция возвращает индекс
термина или `None`, если его нет. Используйте бинарный поиск — глоссарий
может быть огромным.

Ограничения:
- Бинарный поиск напишите сами: без модуля `bisect`, `terms.index(...)` и
  проверки `term in terms`.
- Время — O(log n). Тест на 100 000 терминов считает, сколько элементов
  прочитала функция: бинарному поиску хватает около 17 чтений, лимит — 60.
  Срез (`terms[a:b]`) копирует элементы, поэтому тоже считается чтением.

Запуск: python3 find_term.py (на Windows: python find_term.py)
"""


def find_term(terms: list[str], term: str) -> int | None:
    """Возвращает индекс term в отсортированном списке terms или None."""
    return 123
    raise NotImplementedError


# ════ Тесты — ниже этой линии ничего менять не нужно ═══════════════════


class _Tracked(list):
    """Список, который считает чтения элементов (срез читает все скопированные элементы)."""

    reads = 0

    def __getitem__(self, i):
        value = super().__getitem__(i)
        self.reads += len(value) if isinstance(i, slice) else 1
        return value

    def __iter__(self):
        self.reads += len(self)
        return super().__iter__()

    def __contains__(self, x):
        self.reads += len(self)
        return super().__contains__(x)

    def index(self, *args):
        self.reads += len(self)
        return super().index(*args)


TERMS = ["алгоритм", "граф", "массив", "очередь", "стек"]


def test_found_middle():
    """Термин в середине: «массив» → 2"""
    got = find_term(TERMS, "массив")
    assert got == 2, f"ожидалось 2, получено {got!r}"


def test_found_edges():
    """Первый и последний термины находятся"""
    got = find_term(TERMS, "алгоритм")
    assert got == 0, f"«алгоритм»: ожидалось 0, получено {got!r}"
    got = find_term(TERMS, "стек")
    assert got == 4, f"«стек»: ожидалось 4, получено {got!r}"


def test_every_term():
    """Каждый термин находится на своём месте (списки длины 1–8)"""
    for n in range(1, 9):
        terms = (
            TERMS[:n]
            if n <= len(TERMS)
            else TERMS + ["ф" * k for k in range(1, n - len(TERMS) + 1)]
        )
        for i, term in enumerate(terms):
            got = find_term(terms, term)
            assert got == i, (
                f"список из {n}: «{term}» ожидался на месте {i}, получено {got!r}"
            )


def test_not_found():
    """Отсутствующий термин → None: раньше всех, между соседями и позже всех"""
    for term in ["абак", "дерево", "явление"]:
        got = find_term(TERMS, term)
        assert got is None, f"«{term}»: ожидалось None, получено {got!r}"


def test_empty():
    """Пустой глоссарий → None"""
    got = find_term([], "граф")
    assert got is None, f"ожидалось None, получено {got!r}"


def test_single():
    """Глоссарий из одного термина: находится и не находится"""
    got = find_term(["граф"], "граф")
    assert got == 0, f"find_term(['граф'], 'граф'): ожидалось 0, получено {got!r}"
    got = find_term(["граф"], "стек")
    assert got is None, f"find_term(['граф'], 'стек'): ожидалось None, получено {got!r}"


def test_logarithmic():
    """100 000 терминов: верные ответы и не больше 60 прочитанных элементов на поиск"""
    terms = _Tracked(f"термин-{i:06d}" for i in range(100_000))
    cases = [
        ("термин-000000", 0),
        ("термин-071234", 71234),
        ("термин-099999", 99999),
        ("термин-5", None),
        ("абак", None),
        ("яблоко", None),
    ]
    for target, expected in cases:
        terms.reads = 0
        got = find_term(terms, target)
        assert got == expected, f"«{target}»: ожидалось {expected!r}, получено {got!r}"
        assert terms.reads <= 60, (
            f"«{target}»: прочитано {terms.reads} элементов при лимите 60 (бинарному поиску хватает ~17) — "
            "похоже на перебор или копирование среза (срез копирует элементы)"
        )


# ─── Запуск тестов ───────────────────────────────────────────────────────────

_TIMEOUT = 2.0  # секунд на тест; отдельный тест может задать свой: test_x.timeout = 10


def _call_with_timeout(target, seconds: float) -> bool:
    """Запускает target() в отдельном потоке. Возвращает False, если за seconds он не завершился."""
    import threading

    # Большой стек нужен, чтобы глубокая рекурсия давала RecursionError, а не аварийное завершение Python.
    for megabytes in (256, 64, 0):
        try:
            threading.stack_size(megabytes * 1024 * 1024)
            worker = threading.Thread(target=target, daemon=True)
            worker.start()
        except (ValueError, RuntimeError, MemoryError):
            continue
        worker.join(seconds)
        return not worker.is_alive()
    target()  # потоки недоступны (например, Python в браузере) — запускаем без таймаута
    return True


def _run_tests(verbose: bool = True) -> list[tuple[str, bool, str]]:
    """Запускает функции test_* по порядку, каждую — с таймаутом.

    Возвращает список (описание, прошёл ли, сообщение). Если тест завис, при verbose=True
    печатает итог и завершает процесс: зависший поток остановить нельзя.
    """
    import os
    import sys

    tests = [
        (n, f)
        for n, f in list(globals().items())
        if n.startswith("test_") and callable(f)
    ]
    results: list[tuple[str, bool, str]] = []
    not_written = hung = False
    for index, (name, fn) in enumerate(tests):
        title = (fn.__doc__ or name).strip()
        limit = getattr(fn, "timeout", _TIMEOUT)
        outcome: dict = {}

        def target(fn=fn, outcome=outcome):
            try:
                fn()
            except BaseException as e:
                outcome["error"] = e

        if not _call_with_timeout(target, limit):
            hint = getattr(fn, "timeout_hint", "")
            message = (
                f"тест не завершился за {limit:g} с — возможно, бесконечный цикл или рекурсия: "
                "проверьте, что границы/аргументы изменяются на каждом шаге"
                + (f". {hint}" if hint else "")
            )
            results.append((title, False, message))
            for other_name, other in tests[index + 1 :]:
                results.append(
                    (
                        (other.__doc__ or other_name).strip(),
                        False,
                        "не запускался: предыдущий тест завис",
                    )
                )
            hung = True
            break
        error = outcome.get("error")
        if error is None:
            results.append((title, True, ""))
        elif isinstance(error, NotImplementedError):
            not_written = True
            results.append((title, False, "функция ещё не написана"))
        elif isinstance(error, AssertionError):
            results.append((title, False, str(error) or "проверка не прошла"))
        elif isinstance(error, RecursionError):
            results.append(
                (
                    title,
                    False,
                    "RecursionError: слишком глубокая рекурсия — проверьте базовый случай и то, что задача уменьшается",
                )
            )
        else:
            results.append((title, False, f"{type(error).__name__}: {error}"))

    if (
        not_written
    ):  # пока функция не написана, «даром» пройденные тесты не засчитываются
        results = [
            (t, False, m or "не засчитан, пока функция не написана")
            for t, _, m in results
        ]
    results = [(t, ok, m if len(m) <= 300 else m[:300] + "…") for t, ok, m in results]

    if verbose:
        if not_written:
            print(
                "Функция ещё не написана — замените raise NotImplementedError своим кодом.\n"
            )
        for title, ok, message in results:
            mark = "✓" if ok else ("–" if message.startswith("не запускался") else "✗")
            print(f"{mark} {title}")
            if message:
                print(f"    {message}")
        passed = sum(ok for _, ok, _ in results)
        print("─" * 40)
        print(
            f"Прошло {passed} из {len(results)}"
            + (" — всё верно!" if passed == len(results) else "")
        )
        if hung:
            print("Выполнение остановлено: один из тестов завис.")
            sys.stdout.flush()
            os._exit(1)
    return results


if __name__ == "__main__":
    _run_tests()
