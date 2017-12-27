#Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.




def isbalance(n):
    n = str(n)
    new = list(n)
    balance = 0
    l = new.count("[")
    r = new.count("]")
    lenth = 0
    if r - l == 0:
        for bracket in new:
            lenth += 1

            if bracket == "[":
                balance += 1
            elif bracket == "]":
                balance -= 1

                if balance < 0:
                    print(n + " NOT OK")
                    exit()
                elif balance == 0 and lenth == len(new):
                    print(n + " OK")
                    exit()
    else:
        print(n + " NOT OK")

isbalance("[[][]]")