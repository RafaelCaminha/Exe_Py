A = None
B = None
MEDIA = None

def read_numeric():
    try:
        # read for Python 2.x
        return float(raw_input())
    except NameError:
        # read for Python 3.x
        return float(input())


A = float("{:0.1f}".format((read_numeric())))
B = float("{:0.1f}".format((read_numeric())))
MEDIA = (A * 3.5 + B * 7.5) / 11
print(str("MEDIA = ")+str("{:0.5f}".format(MEDIA)))
