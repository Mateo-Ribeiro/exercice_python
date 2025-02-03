def futur():
    h = int(input("enter current hour: "))
    m = int(input("enter current minute: "))
    if h == 23 and m == 59:
        h, m = (0, 0)
    elif m == 59:
        h += 1
        m = 0
    else:
        m += 1
    print(f"in a minute, it'll be {h}:{m}")


def futur_v2():
    h = int(input("enter current hour: "))
    m = int(input("enter current minute: "))
    s = int(input("enter current seconds: "))
    if h == 23 and m == 59 and s == 59:
        h, m, s = (0, 0, 0)
    elif m == 59 and s == 59:
        h += 1
        m, s = (0, 0)
    elif s == 59:
        m += 1
        s = 0
    else:
        s += 1
    print(f"in a second, it'll be {h}:{m}:{s}")


def fact():
    nb = int(input("how many copy to do? "))
    if nb < 11:
        price = nb * 0.1
    elif nb < 31:
        price = 10 * 0.1 + (nb - 10) * 0.09
    else:
        price = 10 * 0.1 + 20 * 0.09 + (nb - 30) * 0.08
    return price


def elec(a, b, c, d):
    if a + b + c + d > 100:
        print("fraude électorale")
    elif a > 50:
        print("il est élu")
    elif b > 50 or c > 50 or d > 50 or a <= 12.5:
        print("il est battu")
    elif a > b and a > c and a > d:
        print("Il se trouve en ballottage favorable")
    else:
        print("Il se trouve en ballottage défavorable")


def greg():
    d = int(input("choose a day: "))
    m = int(input("choose a month: "))
    y = int(input("choose a year: "))
    if 1900<=y<=2050:
        print("this date is invalid")
    elif m in [1,3,5,7,8,10,12]:
        if 0<d<=31:
            print("this date is valid")
        else:
            print("this date is invalid")
    elif m in [4,6,9,11]:
        if 0<d<=30:
            print("this date is valid")
        else:
            print("this date is invalid")
    else:
        if y%400==0 or (y%4==0 and y%100!=0):
            if 0<d<=29:
                print("this date is valid")
            else:
                print("this date is invalid")
        else:
            if 0<d<=28:
                print("this date is valid")
            else:
                print("this date is invalid")