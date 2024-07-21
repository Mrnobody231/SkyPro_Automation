from string_utils import StringUtils
import pytest

string_utils = StringUtils()

        #CAPITALIZE #
@pytest.mark.parametrize("write_data, get_result", [
   ("skypro", "Skypro"),
       ("147", "147")])  
def test_capitalize(write_data, get_result ):
   assert string_utils.capitilize(write_data) == get_result

@pytest.mark.xfail
def test_negative_capitalize():
    assert string_utils.capitilize("edgar a") == "Edgar A"


        # TRIM #
@pytest.mark.parametrize("write_data, get_result", [
   (" skypro", "skypro"),
     ("  skypro", "skypro"),
       (" skypro ", "skypro "), 
         (" 123", "123") 
           ])
def test_trim(write_data, get_result):
   assert string_utils.trim(write_data) == get_result

@pytest.mark.xfail
def test_negative_trim_1():
    assert string_utils.trim(123) == 123

pytest.mark.xfail
def test_negative_trim_2():
    assert string_utils.trim("--Edgar") == "--Edgar"


        # TO_LIST #
@pytest.mark.parametrize("write_data, delimeter, get_result", [
   ("a,b,c,d", "" , ["a", "b", "c", "d"]),
   ("1,2,3,4", "," , ["1", "2", "3", "4"]),
   ("a,b,c,d", "#" , ["a", "b", "c", "d"])
    ])
def test_to_list(write_data, delimeter, get_result):
   assert string_utils.to_list(write_data, delimeter) == get_result


      # CONTAINS #
@pytest.mark.parametrize("write_data, symbol, get_result", [
    ("Edgar", "g", True),
    ("Žodis", "Ž", True),
    ("", "", True)
    ])
def test_positive_contains(write_data, symbol, get_result):
    assert string_utils.contains(write_data, symbol) == get_result

@pytest.mark.xfail
def test_negative_contains_1():
    assert string_utils.contains("Edgar", "e", False)

@pytest.mark.xfail
def test_negative_contains_2():
    assert string_utils.contains("", "e", False)

@pytest.mark.xfail
def test_negative_contains_3():
    assert string_utils.contains("Edgar", "rr", False)

@pytest.mark.xfail
def test_negative_contains_4():
    assert string_utils.contains("123", "3", False)


     # DELETE_SYMBOL #
@pytest.mark.parametrize("write_data, symbol, get_result", [
    ("Edgar", "d", "Egar"),
    ("Edgar", "r", "Edga"),
    ("Edgar", "E", "dgar"),
    ("Edgarr", "rr", "Edga"),
    ("#Edgar", "#E", "dgar")
    ])
def test_positive_delete_symbol(write_data, symbol, get_result):
   assert string_utils.delete_symbol(write_data, symbol) == get_result

@pytest.mark.xfail
def test_negative_delete_symbol_1():
    assert string_utils.delete_symbol("Edgarr", "rra", "Edga")

@pytest.mark.xfail
def test_negative_delete_symbol_2():
    assert string_utils.delete_symbol(123, 2, 13)


        # STARTS_WITH #
@pytest.mark.parametrize("write_data, symbol, get_result", [
    ("Edgar", "E", True),
    ("123", "1", True),
    ("!Edgar", "!", True),
    ("", "", True),
    (" ", " ", True)
    ])
def test_positive_starts_with(write_data, symbol, get_result):
    assert string_utils.starts_with(write_data, symbol) == get_result

@pytest.mark.xfail
def test_negative_starts_with_1():
    assert string_utils.starts_with("Edgar", "d", False)

@pytest.mark.xfail
def test_negative_starts_with_2():
    assert string_utils.starts_with("", "d", False)

@pytest.mark.xfail
def test_negative_starts_with_3():
    assert string_utils.starts_with(12, 1, False)


        # ENDS_WITH #
@pytest.mark.parametrize("write_data, symbol, get_result", [
    ("Edgar", "r", True),
    ("123", "3", True),
    ("!Edgar", "r", True),
    ("", "", True),
    (" ", " ", True)
    ])
def test_positive_end_with(write_data, symbol, get_result):
    assert string_utils.end_with(write_data, symbol) == get_result

@pytest.mark.xfail
def test_negative_end_with_1():
    assert string_utils.end_with("Edgar", "d", False)

@pytest.mark.xfail
def test_negative_starts_with_2():
    assert string_utils.end_with("", "d", False)

@pytest.mark.xfail
def test_negative_starts_with_3():
    assert string_utils.end_with(12, 1, False)


        # IS_EMPTY #

@pytest.mark.parametrize("write_word, get_result", [
    ("", True),
    (" ", True),
    ("@", False),
    ("Edgar", False),
    ("123", False),
    ("  ", True),
    ("      ", True)
    ])
def test_is_empty(write_word, get_result):
    assert string_utils.is_empty(write_word) == get_result

    # LIST_TO_STRING #

@pytest.mark.parametrize("write_massive, joiner, get_result", [
    (["Counter", "Strike"], "-", "Counter-Strike"),
    (["gmail", "com"], ".", "gmail.com"),
    (["fork", "yandex", "ru"], ".", "fork.yandex.ru"),
    (["Homework", "1"], "Homework, 1")
])
def test_positive_list_to_string(write_massive, joiner, get_result):
    assert string_utils.list_to_string(write_massive, joiner) == get_result

@pytest.mark.xfail
def test_negative_list_to_string():
    assert string_utils.list_to_string(["String, args"], "[]", "String[] args")