Num = None
Sal = None
Horas = None
SalPHoras = None
def read_numeric():
    try:
        # read for Python 2.x
        return float(raw_input())
    except NameError:
        # read for Python 3.x
        return float(input())


Num = int((read_numeric()))
Horas = int((read_numeric()))
SalPHoras = float("{:0.2f}".format((read_numeric())))

Sal = float(Horas * SalPHoras)
print(str("NUMBER = ")+str(Num))
print(str("SALARY = U$ ")+str("{:0.2f}").format(Sal))
