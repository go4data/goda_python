file_name = input("Enter the file name: ")
count=0
float_numbers=[]
sum=0
try:
    fhand=open(file_name)
except:
    print("This file is not exist")
    quit()

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find('0.')
        float_num = float(line[index:])
        float_numbers.append(float_num)
        print(float_num)

for item in float_numbers:
    sum += item
    count +=1

avg= sum/count
print(f"There are {count} lines in the file starts with X-DSPAM-Confidence")
print(f"the average of X-DSPAM-Confidence numbers = {avg}")