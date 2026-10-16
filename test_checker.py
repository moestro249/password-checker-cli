from checker import check_password

def test_short_password():
    assert "too short" in check_password("Ab1!")
    
    
def test_long_enough_password():
    assert "too short" not in check_password("Abcdefg1!")
