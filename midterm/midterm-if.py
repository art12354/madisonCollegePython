print("Name: Arthur Sommer")
total = 0
keywords = ["gmeach18@ed.gov", "248.253.63.149", "Whiteland", "80.222.19.190", "Kayley", "dcassyqw@microsoft.com"]
with open("Midterm-if.txt", "r") as file:
    for line in file:
        split_line = line.strip().split(',')
        for word in split_line:
            for keyword in keywords:
                if word == keyword:
                    total = total + int(split_line[0])
print(f"The total is: {total}")

