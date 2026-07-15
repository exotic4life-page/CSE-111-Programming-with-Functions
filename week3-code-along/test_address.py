from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    full_address = "525 S Center St, Rexburg, ID 83460"
    expected_city = "Rexburg"
    city = extract_city(full_address)
    assert city == expected_city
    
    
def test_extract_state ():
    full_address = "525 S Center St, Rexburg, ID 83460"
    expected_state = "ID"
    state = extract_state(full_address)
    assert state == expected_state
    
    
def test_extract_zipcode():
    full_address = "525 S Center St, Rexburg, ID 83460"
    expected_zipcode = "83460"
    zipcode = extract_zipcode(full_address)
    assert zipcode == expected_zipcode
    
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])