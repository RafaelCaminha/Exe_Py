A: None
B: None
C: None

def read_integer():
    try:
        # read for Python 2.x
        return int(raw_input())
    except NameError:
        # read for Python 3.x
        return int(input())
def read_line():
    try:
        # read for Python 2.x
        return raw_input()
    except NameError:
        # read for Python 3.x
        return input()
def read_numeric():
    try:
        # read for Python 2.x
        return float(raw_input())
    except NameError:
        # read for Python 3.x
        return float(input())
def read_string():
    try:
        # read for Python 2.x
        return raw_input()
    except NameError:
        # read for Python 3.x
        return input()



Var1 = read_numeric()
Sal = float("{:0.2f}".format((read_numeric())))
Vendas = float("{:0.2f}".format((read_numeric())))

TOTAL = float(Sal + (Vendas * 0.15))

print(str("TOTAL = R$ ") + str("{:0.2f}".format(TOTAL)))
