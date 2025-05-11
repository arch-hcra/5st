from login import check_cred

def test_check_cred():
    
    assert check_cred("user", "pass") == False
    assert check_cred("user", "password") == False
    assert check_cred("admin", "pass") == False
    assert check_cred("user", "12345") == True

  
    assert check_cred("", "") == False 
    assert check_cred("user", "") == False 
    assert check_cred("", "password") == False 
    assert check_cred("admin", "admin123") == False  
    assert check_cred("user", "123456") == False 
    assert check_cred("user", "pass123") == False 
    assert check_cred("admin", "password") == False  
    assert check_cred("user", "12345") == False 
