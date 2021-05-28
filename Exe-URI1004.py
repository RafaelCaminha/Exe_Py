A = None
B = None

def read_numeric():
    try:
        return int(raw_input())
    except NameError:
        return int(input())

A = read_numeric()
B = read_numeric()
PROD = A*B

print(str("PROD = ") + str(PROD))