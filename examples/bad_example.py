# Student grade program (BAD version: full of smells)

def f1(n, s1, s2, s3, d):
    # calculate
    t = s1 + s2 + s3
    a = t / 3  # divide t by 3
    # print(t)
    if a >= 90:
        g = "A"
    elif a >= 80:
        g = "B"
    elif a >= 70:
        g = "C"
    elif a >= 60:
        g = "D"
    else:
        g = "F"
    if a >= 60:
        r = "PASS"
    else:
        r = "FAIL"
    data = n + ": " + str(a) + " " + g + " " + r
    if d:
        print(data)
    return data


x = 0
x = x + 1  # add 1 to x
f1("Memo", 90, 85, 78, True)
