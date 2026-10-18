import string 

COMMON_PASSWORDS = {"password", "123456", "qwerty", "12345678", "letmein"}

def check_password(password):
    problems = []
    if len(password) < 8:
        problems.append("too short")
    if not any(c.islower() for c in password):
        problems.append("no lowercase letter")
    if not any(c.isupper() for c in password):
        problems.append("no uppercase letter")
    if not any(c.isdigit() for c in password):
        problems.append("no digit")
    if not any(c in string.punctuation for c in password):
        problems.append("no special character")
    if password.lower() in COMMON_PASSWORDS:
        problems.append("too common")
    return problems
    