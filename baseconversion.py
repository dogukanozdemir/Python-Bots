import math
hex_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def decimal_to_base(n,precision,base):
    hex = ""
    digits = math.floor(n)
    while digits != 0:
        print(str(digits) + " // " + str(base) + " = " + str(digits // base) )
        print(str(digits) + " % " + str(base) + " = " + str(digits % base) )
        hex += str(hex_list[digits % base])
        digits = digits // base

    hex = hex[::-1]
    if n - int(n) != 0 and precision != 0:
        hex += "."
        print("-------------------")
        for _ in range(precision):
            decimal = n - math.floor(n)
            print(str() + " * " + str(base) + " = " + str(decimal * base))
            n = decimal * base
            hex += str(int(n) % base) 
    return hex

def base_to_decimal(n,base):
    n = n.upper()
    decimal = "0"
    multiplier = len(n.split('.')[0]) - 1
    for digit in n:
        if(digit == '.'):
            continue
        decimal =  str(float(decimal) + hex_list.index(digit) * (base**multiplier))
        multiplier -= 1
    return decimal


print(base_to_decimal("15A1.11C",16))


