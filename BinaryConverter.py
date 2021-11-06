from math import log, ceil


class BinaryConverter:
    @staticmethod
    def int_to_binary_list(n: int, total_bits: int) -> list[str]:
        binary_list = list(f"{n:b}")
        return (['0' for i in range(total_bits)] + binary_list)[-total_bits:]

    @staticmethod
    def binary_list_to_int(binary_list: list[str]) -> int:
        to_strings = [str(i) for i in binary_list]
        return int("".join(to_strings), 2)

    @staticmethod
    def bits_needed(count: int) -> int:
        return ceil(log(count, 2))

    @staticmethod
    def chunk_list(binary_list: list[str], bits_per_chunk: int) -> list:
        for i in range(0, len(binary_list), bits_per_chunk):
            yield binary_list[i:i + bits_per_chunk]
