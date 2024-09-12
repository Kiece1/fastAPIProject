from unidecode import unidecode
import re
import random

def generate_qs(val):
    val = val.lower()
    val = val.replace(" ", "-")
    val = unidecode(val)  # Remove accents and special characters
    val = re.sub(r"[^a-z0-9-]", "", val)  # Remove remaining special characters
    return val

def generate_short_code(length: int = 4) -> str:
    return "".join(
        (
            chr(random.randint(97, 122))
            if random.random() < 0.5
            else chr(random.randint(48, 57))
        )
        for _ in range(length)
    )