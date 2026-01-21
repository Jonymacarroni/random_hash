import hashlib
import random
import string

def random_string(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

found = False
for _ in range(1000):
    s = random_string()
    h = hashlib.md5(s.encode()).hexdigest()  # Genera un hash de 32 caracteres
    if h.startswith("00"):
        print(f"Found hash: {h} from string: {s}")
        found = True
        break

if not found:
    print("No hash starting with '00' was found in 1000 tries.")
