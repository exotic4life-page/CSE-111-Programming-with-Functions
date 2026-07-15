from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Jo", "Li") == "Li; Jo"
    assert make_full_name("Mary-Jane", "Smith-Jones") == "Smith-Jones; Mary-Jane"
    assert make_full_name("Christopher", "Johnson") == "Johnson; Christopher"


def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Li; Jo") == "Li"
    assert extract_family_name("Smith-Jones; Mary-Jane") == "Smith-Jones"
    assert extract_family_name("Johnson; Christopher") == "Johnson"


def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Li; Jo") == "Jo"
    assert extract_given_name("Smith-Jones; Mary-Jane") == "Mary-Jane"
    assert extract_given_name("Johnson; Christopher") == "Christopher"


# Call pytest to run the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])