import f2c
import c2f
t = input("Input temperature scalar: ")
u = input("Input temperature unit (F or C): ")
if u == "F" or u == "f":
    print(f2c.f_to_c(int(t)))
elif u == "C" or u == "c":
    print(c2f.c_to_f(int(t)))
else:
    print("Error: erroneous input")
