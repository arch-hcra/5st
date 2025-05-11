from login import check_cred

def test_check_cred():
    assert check_cred("user","pass") == False
    assert check_cred("user","password") == False
    assert check_cred("admin","pass") == False
    assert check_cred("user","12345") == True
