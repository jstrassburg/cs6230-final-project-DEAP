from math import log, ceil


class BinaryConverter:
    @staticmethod
    def int_to_binary_list(n: int, total_bits: int) -> list[str]:
        binary_list = list(f"{n:b}")
        return (['0' for i in range(total_bits)] + binary_list)[-total_bits:]

    @staticmethod
    def binary_list_to_int(binary_list: list[str]) -> int:
        return int("".join(binary_list), 2)

    @staticmethod
    def bits_needed(count: int) -> int:
        return ceil(log(count, 2))
