from checker import check_password

def test_short_password():
    assert "too short" in check_password("Ab1!")
    
def test_long_enough_password():
    assert "too short" not in check_password("Abcdefg1!")

def test_no_lowercase():
    assert "no lowercase letter" in check_password("ABCDEFG1!")

def test_has_lowercase():
    assert "no lowercase letter" not in check_password("abcdefg1!")

def test_no_uppercase():
    assert "no uppercase letter" in check_password("abcdefg1!")

def test_has_uppercase():
    assert "no uppercase letter" not in check_password("Abcdefg1!")

def test_no_digit():
    assert "no digit" in check_password("Abcdefgh!")

def test_has_digit():
    assert "no digit" not in check_password("Abcdefg1!")

def test_no_special_character():
    assert "no special character" in check_password("Abcdefg12")

def test_has_special_character():
    assert "no special character" not in check_password("Abcdefg1!")
    
def test_not_too_common():
    assert "too common" not in check_password("Abcdefg1!")

def test_is_too_common():
    assert "too common" in check_password("password")

def test_strong_password():
    assert check_password("Abcdef1!") == []