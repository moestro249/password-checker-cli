def check_password(password):
    problems = []
    if len(password) < 8:
        problems.append("too short")
    return problems
    