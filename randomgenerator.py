import random
import string


def generate_random_key():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(63))


if __name__ == '__main__':
    print(generate_random_key())
