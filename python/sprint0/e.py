from typing import List, Optional, Tuple


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Здесь реализация вашего решения
    previous = set()

    for a in arr:
        b = target_sum - a
        if b in previous:
            return b, a
        else:
            previous.add(a)
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


def main():
    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))


if __name__ == '__main__':
    main()
