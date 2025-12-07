"""
 Exercise 1: Revise a previous program as follows: Read and parse the “From”
 lines and pull out the addresses from the line. Count the number of messages from
 each person using a dictionary.
 After all the data has been read, print the person with the most commits by
 creating a list of (count, email) tuples from the dictionary. Then sort the list in
 reverse order and print out the person who has the most commits.
 Sample Line:
 From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
 Enter a file name: mbox-short.txt
 cwen@iupui.edu 5
"""
mail_count = dict()
lst = list()
file_name = input("Enter the file name: ")
with open(file_name, "r") as handler:
    for line in handler:
        if line.startswith("From "):
            words = line.split(" ")
            user_mail = words[1]
            mail_count[user_mail] = mail_count.get(user_mail, 0) + 1

mail_count = mail_count.items()
lst = [(y, x) for(x, y) in mail_count]
lst_sorted = sorted(lst, reverse=True)
highest_mail = lst_sorted[0]#(y, x) for (x, y) in lst_sorted:


print(highest_mail[1], highest_mail[0])