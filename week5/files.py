print("\t1")
fp = open("/etc/passwd", "r")
fs = fp.read()
print(fs)
print(len(fs))
print("the len() function when used on a string returns the number of characters that exist in the string")
print("you would .read() for gathering a file into one string")

print("\n\t2")
fp = open("/etc/passwd", "r")
fl = fp.readlines()
print(fl)
print(len(fl))
print("the len() function when used on a list returns the number of elements that exist in the list")
print("you would use .readlines() for gathering each line in a file into one list")

print("\n\t3")
lines = []
with open("/etc/passwd", "r") as file:
    for line in file:
        lines.append(line)
num_chars = 0
for line in lines:
    num_chars = num_chars + len(line)
print("the number of characters in /etc/passwd: " + str(num_chars))
print("you would add each line to a list individually if preprocessing must be done to each line")
