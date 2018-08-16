def Celsium_temp(F):
    C = ((F-32)*5)/9
    return C
def Fahren_temp(C):
    F = (C*9/5)+32
    return F

print("72 degrees of F = {0} degrees in C".format(Celsium_temp(72)))
print("37 degrees of F = {0} degrees in C".format(Fahren_temp(37)))
