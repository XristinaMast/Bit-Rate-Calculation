print("Please enter the average size of the package (L)")
L = float(input("L: "))
if L < 0:
    while L < 0:
        print("Please enter the average size of the package, again (L)")
        L = float(input("L: "))

print("Please enter the max value of delay (D_max)")
D_max = float(input("D_max: "))
if D_max < 0:
    while D_max < 0:
        print("Please enter the max value of delay, again (D_max)")
        D_max = float(input("D_max: "))

print("Please enter the value of delay (D_max)")
prop = float(input("prop: "))
if prop < 0:
    while prop < 0:
        print("Please enter the value of delay (D_max)")
        prop = float(input("prop: "))

if prop > D_max:
    while prop > D_max:
        print("Please enter the max value of delay, again (D_max)")
        D_max = float(input("D_max: "))
        if D_max < 0:
            while D_max < 0:
                print("Please enter the max value of delay, again (D_max)")
                D_max = float(input("D_max: "))

        print("Please enter the value of delay, again (D_max)")
        prop = float(input("prop: "))
        if prop < 0:
            while prop < 0:
                print("Please enter the value of delay (D_max)")
                prop = float(input("prop: "))

print("Please enter the time (t1,t2)")
t1 = float(input("t1: "))
t2 = float(input("t2: "))

if t1 < 0:
    while t1 > 0:
        print("Please enter the time, again (t1)")
        t1 = float(input("t1: "))

if t2 < 0:
    while t2 > 0:
        print("Please enter the time, again (t2)")
        t1 = float(input("t2: "))

if t2 < t1:
    while t2 < t1:
        print("Please enter the time (t1,t2)")
        t1 = float(input("t1: "))
        t2 = float(input("t2: "))

        if t1 < 0:
            while t1 > 0:
                print("Please enter the time, again (t1)")
                t1 = float(input("t1: "))

        if t2 < 0:
            while t2 > 0:
                print("Please enter the time, again (t2)")
                t1 = float(input("t2: "))

Bit_Rate = L/(abs(D_max - prop))

print("The Bit-Rate is: ", Bit_Rate)
print("The number of bits of the package: ", Bit_Rate*(t2-t1))
