print("Name: Arthur Sommer")
password_database = {
            "Username": "dnedry",
            "Password": "please"
        }
command_database = {
            "reboot": "OK. I will reboot all park systems.",
            "shutdown": "OK. I will shutdown all park systems.",
            "done": "I hate all this hacker stuff"
        }
white_rabbit_object = 0
counter = 0
while(white_rabbit_object == 0 and counter < 3):
    input_user = input("Username: ")
    input_password = input("Password: ")
    if(input_user == password_database.get("Username") and input_password == password_database.get("Password")):
        white_rabbit_object = 1
        print("\nHi Dennis. You're still the best hacker in Jurassic Park.")
    else:
        counter = counter + 1
        if(counter != 3):
            print(f"\nYou didn't say the magic word. {counter}\n")
if(white_rabbit_object == 1):
    print("Enter command: \n")
    for command in command_database.keys():
        print(command)
    input_command = input("\n> ")
    if(input_command == "reboot"):
        print(f"\n{command_database.get('reboot')}")
    elif(input_command == "shutdown"):
        print(f"\n{command_database.get('shutdown')}")
    elif(input_command == "done"):
        print(f"\n{command_database.get('done')}")
    else:
        print("\nThe Lysine Contigency has been put into effect.")
if(counter == 3):
    print("\n")
    for i in range(25):
        print("You didn't say the magic word")
