def f_to_c(f):
    return ((f-32)*5/9)
def main():
    f = input("Input temperature in degrees Fahrenheit: ")
    print(f_to_c(int(f)))
if __name__ == "__main__":
    main()
