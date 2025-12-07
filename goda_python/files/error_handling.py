file_name = input("Ente the file name : ")
file_handelr = open(file_name)
count=0
try:
    file_handelr = open(file_name)

except:
    print(f"{file_name} not found")
    print("non numeric data")
    quit()

for line in file_handelr:
    if line.__contains__("Java")or line.__contains__("java"):
        count+=1

print(f"the count of python word = {count}")