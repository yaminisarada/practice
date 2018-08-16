def factors():
    try:
        n = input("Enter a positive integer: ")
        m = int(n)
        num_range = range(1,m+1)
        for i in num_range:
            k = num_range%i
            if k == 0:
                print("{0} is a divisor of {1}".format(i, m))
    except(TypeError):
        print("There is an range and int problem")

factors()
    
def factor():
    try:
        n = input("Enter a positive integer: ")
        m = int(n)
        num_range = range(1,m+1)
        for i in num_range:
            k = m%i
            if k == 0:
                print("{0} is a divisor of {1}".format(i, m))
    except(TypeError):
        print("There is an range and int problem")

factor()
