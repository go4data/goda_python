"""
 Exercise 1: Find all unique words in a file
 Shakespeare used over 20,000 words in his works. But how would you determine
 that? How would you produce the list of all the words that Shakespeare used?
 Would you download all his work, read it and track all unique words by hand?
 Let’s use Python to achieve that instead. List all unique words, sorted in alphabet
ical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s
 work.
 To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Cre
ate a list of unique words, which will contain the final result. Write a program to
 open the file romeo.txt and read it line by line. For each line, split the line into a
 list of words using the split function. For each word, check to see if the word is
106
 CHAPTER 8. LISTS
 already in the list of unique words. If the word is not in the list of unique words,
 add it to the list. When the program completes, sort and print the list of unique
 words in alphabetical order.
"""

unique_list = list()
try:
    with open("ex_1_romeo.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            words_in_line = line.split()
            for word in words_in_line:
                if word not in unique_list:
                    unique_list.append(word)
except Exception as e:
    print(f"Error: {e}")

unique_list.sort()
print(unique_list)