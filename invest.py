def invest(amount, rate, year):
    n = range(1, year+1)
    print("principal amount:{}".format(amount))
    print("annual rate of return: ".format(rate))
    for i in n:
        end_amt = amount*(1+rate)**(i)
        print("year {0}, : ${1}".format(i,end_amt))

invest(100, 0.05, 8)
invest(2000, 0.025, 5)

