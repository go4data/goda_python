"""
 Exercise3:Write a program that reads a file and prints the letters in decreasing
 order of frequency.
 Your program should convert all the input to lowercase and only count the letters
 a-z.Your program should not count spaces, digits, punctuation, or any thing other
 than the letters a-z. Find text samples from several different languages and see
 how letter frequency varies between languages.
"""
import string
lst=list()
counts=dict()
file_name = input("Enter the file name: ")
with open(file_name,"r")as fhandler:
    for line in file_name:
         line = line.translate(str.maketrans('','', string.punctuation))
         line = line.lower()
         words = line.split()
         for word in words:
              for letter in word:
                   counts[letter] = counts.get(letter, 0)+1
    

for key,val in list(counts.items()):
     lst.append((val, key))
     
lst = lst.sort(reverse = True)

for key,val in lst:
     print(val,key)