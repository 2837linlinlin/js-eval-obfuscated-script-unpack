import re


def base10_2_n_string(d, n):
    s, t = "", d
    if t == 0: return "0"
    while t > 0:
        v = t % n
        s += (chr(v + 87), str(v))[v <= 9]
        t = int(t / n)
    return s[::-1]


def eval_unpack(p, a, c, k, e, d):
    def e(c):
        c = int(c)
        if c < a:
            pad = ''
        else:
            pad = e(c/a)
        c = c % a
        if c > 35:
            return pad + chr(c + 29)
        else:
            return pad + base10_2_n_string(c, 36)

    while c:
        c -= 1
        d[e(c)] = k[c] or e(c)

    return re.sub("\w+", lambda e: d.get(e.group()) or e.group(), p)
