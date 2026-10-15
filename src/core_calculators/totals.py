from collections.abc import Iterable


def calculate_total(items: Iterable[float]) -> float:
    """Return the sum of item amounts."""
    return sum(items)
