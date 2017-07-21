import random, string

# generates random string
def generate_code(length):

    return ''.join(random.choice(string.lowercase) for i in range(length)).upper()