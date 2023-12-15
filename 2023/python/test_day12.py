from day12 import count


def test_all_dot() -> None:
    result = count("......", (1,))
    assert result == 0


def test_no_left_valid() -> None:
    result = count("..??.?.?", tuple[int]())
    assert result == 1


def test_no_left_invalid() -> None:
    result = count("..?.?#?.", tuple[int]())
    assert result == 0


def test_sharp_invalid_too_short() -> None:
    result = count("#?", (3,))
    assert result == 0


def test_sharp_invalid_dots() -> None:
    result = count("#.#", (3,))
    assert result == 0


def test_sharp_valid_exact_length() -> None:
    result = count("###", (3,))
    assert result == 1


def test_sharp_valid_exact_length_with_qm() -> None:
    result = count("#???", (4,))
    assert result == 1


def test_sharp_invalid_no_separator() -> None:
    result = count("#?#", (2,))
    assert result == 0


def test_multiple_valid_sharp() -> None:
    result = count("###.#?#", (3, 3))
    assert result == 1


def test_impossible_too_short() -> None:
    result = count("??????????", (3, 3, 3))
    assert result == 0


def test_example_0() -> None:
    result = count("???.###", (1, 1, 3))
    assert result == 1


def test_example_1() -> None:
    result = count(".??..??...?##.", (1, 1, 3))
    assert result == 4


def test_example_2() -> None:
    result = count("?#?#?#?#?#?#?#?", (1, 3, 1, 6))
    assert result == 1


def test_example_3() -> None:
    result = count("????.#...#...", (4, 1, 1))
    assert result == 1


def test_example_4() -> None:
    result = count("????.######..#####.", (1, 6, 5))
    assert result == 4


def test_example_5() -> None:
    result = count("?###????????", (3, 2, 1))
    assert result == 10
