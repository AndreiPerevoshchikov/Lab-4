import random
import string


def key():
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    f = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    h = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    j = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    k = ''.join(g)
    l = f + h + j + k
    return l


