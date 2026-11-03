import pytest

from vending_machine import make_change, purchase, select_item


def test_selection_statuses():
    assert select_item("water", {}, 200) == "invalid"
    assert select_item("candy", {"candy": 0}, 200) == "sold_out"
    assert select_item("cola", {"cola": 1}, 100) == "insufficient"
    assert select_item("cola", {"cola": 1}, 150) == "ok"


def test_change_calculation_and_errors():
    assert make_change(0) == []
    assert make_change(190) == [100, 50, 25, 10, 5]
    assert make_change(1) is None
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


def test_purchase_outcomes_and_stock():
    stock = {"cola": 2, "chips": 1, "candy": 0}

    assert purchase("water", stock, 200) == ("invalid", [])
    assert purchase("cola", stock, 151) == ("no_exact_change", [])
    assert stock["cola"] == 2
    assert purchase("cola", stock, 250) == ("dispensed", [100])
    assert stock["cola"] == 1
