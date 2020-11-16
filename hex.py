import math
hex_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def decimal_to_hex(n,precision):
    hex = ""
    digits = math.floor(n)
    while digits != 0:
        hex += str(hex_list[digits % 8])
        digits = digits // 8

    hex = hex[::-1]
    if n - int(n) != 0 and precision != 0:
        hex += "."
        for _ in range(precision):
            decimal = n - math.floor(n)
            n = decimal * 8
            hex += str(int(n) % 8) 
    return hex

print(decimal_to_hex(7562.45,10))




