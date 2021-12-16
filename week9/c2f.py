def c_to_f(c):
    return ((c*9/5)+32)
def main():
    c = input("Input temperature in degrees Celsius: ")
    print(c_to_f(int(c)))
if __name__ == "__main__":
    main()
