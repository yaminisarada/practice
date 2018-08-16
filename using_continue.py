def no_multiples_of_3():
    for i in range(1,51):
        if i % 3 == 0:
            continue
        print("{} is not a multiple of 3".format(i))

no_multiples_of_3()
