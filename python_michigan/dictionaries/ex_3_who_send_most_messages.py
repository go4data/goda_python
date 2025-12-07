"""
Exercise 3: Add code to the above program to figure out who has sent the most
 messages in the file. After all the data has been read and the dictionary has
 been created, look through the dictionary using a maximum loop (see Chapter 5:
 Maximum and minimum loops) to find who has the most messages and print how
 many messages the person has.
 Enter a file name: mbox-short.txt
 cwen@iupui.edu 5
 Enter a file name: mbox.txt
 zqian@umich.edu 195
"""

bigword = None
bigcount = None
email_count = dict()

file_name = input("Enter the file name: ")
with open(file_name, "r")as handler:
    for line in handler:
        if line.startswith("From:"):
            email = line[6:].strip()
            email_count[email] = email_count.get(email, 0) + 1

for key, count in email_count.items():
    if bigcount == None or bigcount < count:
        bigword = key
        bigcount = count
print(f"{bigword} , {bigcount}")