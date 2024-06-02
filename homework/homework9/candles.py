"""Candles.
This program calculate count candles from residue .
"""


def total_candles(candles_number: int, make_new: int) -> int:
    """Calculates the total number of candles that can be burned given
    an initial number of candles and the ability to make new candles
    from the remainders.

    Args:
        candles_number (int): The initial number of candles.
        make_new (int): The number of remainders needed to make a new candle.

    Returns:
        int: The total number of candles that can be burned.
    """
    def burn_candles(candles, burned, remaining):
        """This a recursive function that takes
        the current number of candles, the total number of candles burned
        and the number of remaining remainders.

        Args:
            candles (int): The current number of candles.
            burned (int): The total number of candles burned so far.
            remaining (int): The number of remaining remainders.

        Returns:
            int: The total number of candles burned including those
            made from remainders.
        """

        if candles == 0:
            return burned
        burned += candles
        remaining += candles
        new_candles = remaining // make_new
        remaining %= make_new
        return burn_candles(new_candles, burned, remaining)

    return burn_candles(candles_number, 0, 0)


assert total_candles(5, 2) == 9, \
    'count candles must be = 9'
assert total_candles(1, 2) == 1, \
    'count candles must be = 1'
assert total_candles(15, 5) == 18, \
    'count candles must be = 18'
assert total_candles(12, 2) == 23, \
    'count candles must be = 23'
assert total_candles(6, 4) == 7, \
    'count candles must be = 7'
assert total_candles(13, 5) == 16, \
    'count candles must be = 16'
assert total_candles(2, 3) == 2, \
    'count candles must be = 2'
