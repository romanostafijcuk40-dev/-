import string
import secrets

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password
new_password = generate_password(8)
print(f"Ваш надійний пароль: {new_password}")


