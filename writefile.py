a=input("Enter any text:")
with open("sample.txt",'w') as file:
    file.write("Who are you\n")
    file.write(a)