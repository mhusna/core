from core_calculators import calculate_total


def test_calculate_total_sums_item_amounts() -> None:
    assert calculate_total([12.5, 7.5, 10]) == 30


def test_calculate_total_returns_zero_for_empty_input() -> None:
    assert calculate_total([]) == 0
