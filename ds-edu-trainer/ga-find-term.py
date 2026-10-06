def find_term(terms: list[str], term: str) -> int | None:
    low = 0
    high = len(terms) - 1

    while low <= high:
        mid = (low + high) // 2

        if terms[mid] == term:
            return mid

        if terms[mid] > term:
            high = mid - 1

        if terms[mid] < term:
            low = mid + 1
    return None