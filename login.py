def check_cred(username,password):
    correct_username = "user"
    correct_password = "12345"

    if username == correct_username and password == correct_password:
        return True
    return False

def main():
    username = input("Enter Login: ")
    password = input("Enter password: ")

    if check_cred(username,password):
        print("Hello word!!!")
    else:
        print("Bye is loser!!!")

if __name__ == "__main__":
    main()