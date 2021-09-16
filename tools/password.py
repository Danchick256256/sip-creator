import string
import random


def create_pass():
    return''.join(random.choice(string.ascii_lowercase))+''.join(random.choice(string.digits))+''\
        .join(random.choice(string.ascii_uppercase))+''.join(random.choice(string.ascii_lowercase))+''\
        .join(random.choice(string.digits))+''.join(random.choice(string.ascii_uppercase))
