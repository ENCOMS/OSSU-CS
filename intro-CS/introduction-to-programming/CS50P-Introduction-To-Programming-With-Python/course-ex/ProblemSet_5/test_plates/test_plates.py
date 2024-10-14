from plates import is_valid


# Invalid Tests
def test_min_char_str():
    assert is_valid("a") == False


def test_min_char_int():
    assert is_valid("1") == False


def test_max_len():
    assert is_valid("asdd1245") == False


def test_not_start_two_letters():
    assert is_valid("c1") == False


def test_start_two_letters2():
    assert is_valid("12sd") == False


def test_start_not_middle_numbers():
    assert is_valid("asa12s") == False


def test_not_start_in_0():
    assert is_valid("as02") == False


def test_spaces():
    assert is_valid("as 12") == False


def test_punctuation():
    assert is_valid("as.12") == False


def test_periods():
    assert is_valid("as,12") == False


def test_accent():
    assert is_valid("as'12") == False


# Valid tests
def test_min_char_str_2():
    assert is_valid("cs") == True


def test_min_char_int_2():
    assert is_valid("cs1") == True


def test_max_len_2():
    assert is_valid("asd124") == True


def test_start_two_letters_2():
    assert is_valid("cs12") == True


def test_str_all_char_2():
    assert is_valid("cscs") == True


def test_start_not_middle_numbers2():
    assert is_valid("asas21") == True
