SPACE = " "
PLUS, MINUS, CARET = "+", "-", "^"
POWERS= "^{}"
SIGNS = PLUS + MINUS 
PTOKEN, MTOKEN = SPACE + PLUS, SPACE + MINUS


def clean(lexp: str) -> str:
    s = ''.join(ch for ch in lexp if (ch.isalnum() or ch in (POWERS + SIGNS)))
    return s if s[0] in SIGNS else PLUS + s


def add_delims(s: str) -> str:
    return s.replace(PLUS, PTOKEN).replace(MINUS, MTOKEN).strip()


def tokenize(lexp: str) -> [str]:
    return add_delims(clean(lexp)).split()


def canonical(lexp: str) -> str:
    return SPACE.join(reversed(tokenize(lexp)))

data = ["$x^3 +100x -17", "-4x^4+3x^3 +12x^{2} - 76"]

for _ in data:
    print(f'{_} ==> {canonical(_)}')

