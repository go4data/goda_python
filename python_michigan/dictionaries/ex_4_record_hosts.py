"""
 Exercise 5: This program records the domain name (instead of the address) where
 the message was sent from instead of who the mail came from (i.e., the whole email
 address). At the end of the program, print out the contents of your dictionary.
 python schoolcount.py
 Enter a file name: mbox-short.txt
 {media.berkeley.edu: 4, uct.ac.za: 6, umich.edu: 7,
 gmail.com: 1, caret.cam.ac.uk: 1, iupui.edu: 8}
"""
host_count={}
file_name = input("Enter the file name: ")
with open(file_name,"r")as handler:
    for line in handler:
        if line.startswith("From:"):
            From_emails = line.split()
            emails = From_emails[1]
            guy_host = emails.split("@")
            host=guy_host[1]
            host_count[host]=host_count.get(host,0)+1

print(host_count)