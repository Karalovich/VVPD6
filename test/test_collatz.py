from .. import collatz
import pytest

@pytest.mark.parametrize("value, result", [(3, [3, 10, 5, 16, 8, 4, 2, 1]),
                                           (5, [5, 16, 8, 4, 2, 1]),
                                           (6, [6, 3, 10, 5, 16, 8, 4, 2, 1]),
                                           (2, [2, 1]),
                                           (4, [4, 2, 1])])


def test_sequence_good(value, result):
    """
    функция тестирует sequence
    """
    assert collatz.sequence(value) == result


@pytest.mark.parametrize("value, result", [(3, 16), (5, 16), (4, 4), (7, 52), (9, 52)])
def test_maxim_good(value, result):
    """
        функция тестирует maxim
        """
    assert collatz.maxim(value) == result
