print("Name: Arthur Sommer")
file_text = ""
with open("slicing-file.txt", "r") as file:
    file_text = file.readlines()
var1 = file_text[-3]
var2 = file_text[2:5]
var3 = file_text[-10:-15:-2]
var4 = file_text[10:13]
var5 = file_text[-19:-22:-1]
quote = var1 + " " +  " ".join(var2) + " " + " ".join(var3) + " " + " ".join(var4) + " " + " ".join(var5)
quote = quote.replace("\n", "")
print(quote)
