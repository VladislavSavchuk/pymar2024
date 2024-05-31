"""Candles.
This program calculate count candles from residue .
"""


def total_candles(candles_number: int, make_new: int) -> int:
    """This function takes the number of candles and remainders.
    candles_number: int
    make_new: int
    return: int
    """
    def burn_candles(candles, burned, remaining):
        """This a recursive function that takes
        the current number of candles, the total number of candles burned
        and the number of remaining remainders.
        """

        if candles == 0:
            return burned
        burned += candles
        remaining += candles
        new_candles = remaining // make_new
        remaining %= make_new
        return burn_candles(new_candles, burned, remaining)

    return burn_candles(candles_number, 0, 0)


assert total_candles(5, 2) == 9
assert total_candles(1, 2) == 1
assert total_candles(15, 5) == 18
assert total_candles(12, 2) == 23
assert total_candles(6, 4) == 7
assert total_candles(13, 5) == 16
assert total_candles(2, 3) == 2

print("All tests passed!")
