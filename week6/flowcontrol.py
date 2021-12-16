#!/usr/bin/env python3

print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("-> ")

# == Door Number 1 Logic ========================
if door == "1":

    print("There is a giant, hungry bear.")
    print("what do you do?\n")

    print("1. Feed it cake.")
    print("2. Scream at the bear.")

    # == Bear Logic =============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =========================
elif door == "2":
    print("You stare into an endless abyss in your new minecraft world.\n")

    print("1. JUMP.")
    print("2. Scream.")
    print("3. walk away, you never saw anything.")

    # == Insanity Logic ===========================
    insanity = input("-> ")

    if insanity == "1":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    elif insanity == "2":
        print("2) You hear the echos of your scream for the rest of eternity.")
        print("2) Good job!")
    else:
        print("N) huh?")

# == Door Number 3 Logic ============================
elif door == "3":
    print("You win $10,000! What is your next move?\n")

    print("1. Donate the money.")
    print("2. Pocket the money.")

    # == Goodness Logic ==============================
    goodness = input("-> ")

    if goodness == "1":
        print("1) you walk away, your job is done.")
    elif goodness == "2":
        print("2) Goodbye.")
    else:
        print("N) Congratulations!")
else:
    print("you did not select a door??? Good Call :)")
