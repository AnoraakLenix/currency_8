import random
import string


def get_password(lenght: int = 10) -> str:
    """
    generate password for user

    """
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(lenght):
        password += random.choice(chars)

    return password
