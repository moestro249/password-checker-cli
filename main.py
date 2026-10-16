from checker import check_password
from getpass import getpass

def main():
    password = getpass("Password: ")
    problems = check_password(password)

    if not problems:
        print("Password is strong")
    else:
        print("Problems found:")
        for problem in problems:
            print("-", problem)

if __name__ == "__main__":
    main()